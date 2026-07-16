"""Shared Markdown URL extraction and canonicalization core.

Plan §4 (Markdown Parsing And URL Association) + Task 3. This module is the single
home for URL extraction from Markdown text, URL canonicalization, and the
deterministic ``source_id`` derivation. Both the MIT adapter and the generic
structured adapter import from here (removing the previous reverse coupling where
``structured_markdown_parser`` imported ``add_source`` from ``mit_parser``).

Design constraint (backward compatibility): the existing MIT dataset has 107
sources and 157 catalog entries whose ``source_id`` values were produced by
``stable_id("src", university_id, netloc, path)``. To avoid breaking those
references and the MIT reconciliation gate (SB=55, Minor=17, graduate=85,
total=157), ``source_id_for`` MUST produce the same id for the same netloc+path.
Canonicalization therefore only affects the stored ``canonical_url`` value and
deduplication, not the id algorithm.
"""
from __future__ import annotations

import hashlib
import ipaddress
import re
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

# ---------------------------------------------------------------------------
# Tracking parameters removed during canonicalization (functional params kept).
# Extend conservatively; these are the common analytics/marketing trackers.
# ---------------------------------------------------------------------------
TRACKING_PARAMS: frozenset[str] = frozenset(
    {
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
        "utm_id",
        "gclid",
        "fbclid",
        "msclkid",
        "mc_eid",
        "mc_cid",
        "_ga",
        "yclid",
        "twclid",
        "igshid",
        "ref",
        "ref_src",
    }
)

_PRIVATE_HOST_SUFFIXES = (".local", ".internal", ".localhost", ".test", ".example", ".invalid")


@dataclass
class ExtractedUrl:
    """A URL lifted from Markdown prose, with the heading path it lived under."""

    raw: str
    canonical: str
    heading_path: list[str] = field(default_factory=list)
    context: str = "prose"  # prose | markdown_link | autolink | bare | structured


def slug(value: str) -> str:
    """Lowercase, strip scheme, collapse non-alphanumerics to underscores."""
    value = value.lower()
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def stable_id(prefix: str, *parts: str) -> str:
    """Deterministic, length-bounded id. Signature preserved from mit_parser."""
    raw = "_".join(slug(p) for p in parts if p)
    raw = re.sub(r"_+", "_", raw).strip("_")
    if len(raw) > 80:
        digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
        raw = f"{raw[:60]}_{digest}"
    return f"{prefix}_{raw}"


# ---------------------------------------------------------------------------
# Canonicalization (Plan §4.3)
# ---------------------------------------------------------------------------

def _is_private_or_loopback_host(host: str) -> bool:
    host = host.split("@")[-1].split(":")[0].strip("[]")
    if host in {"localhost"}:
        return True
    if host.endswith(_PRIVATE_HOST_SUFFIXES):
        return True
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        # bare hostname like "myhost" without TLD -> treat as private/internal
        return "." not in host and not host.endswith(_PRIVATE_HOST_SUFFIXES)
    return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved


def is_valid_http_url(url: Any) -> bool:
    """True only for http(s) URLs that are not localhost/private/malformed."""
    if not isinstance(url, str) or not url.strip():
        return False
    parsed = urlparse(url.strip())
    if parsed.scheme.lower() not in {"http", "https"}:
        return False
    if not parsed.netloc:
        return False
    if _is_private_or_loopback_host(parsed.hostname or ""):
        return False
    return True


def canonicalize_url(url: str) -> str:
    """Apply Plan §4.3 canonicalization.

    - normalize scheme + hostname casing
    - drop fragment
    - drop tracking query params, keep functional ones, sorted
    - normalize empty path and trailing slash consistently (no trailing slash
      unless the path is the root)
    """
    raw = (url or "").strip()
    if not raw:
        return raw
    parsed = urlparse(raw)
    scheme = parsed.scheme.lower()
    host = (parsed.hostname or "").lower()
    port = f":{parsed.port}" if parsed.port is not None else ""
    netloc = f"{host}{port}"

    # path normalization: '' and '/' -> ''; strip trailing slash for non-root
    path = parsed.path or ""
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")
    if path == "/":
        path = ""

    # query: drop tracking params, keep functional, stable order
    kept = [(k, v) for (k, v) in parse_qsl(parsed.query, keep_blank_values=True) if k.lower() not in TRACKING_PARAMS]
    query = urlencode(kept, doseq=True)

    return urlunparse((scheme, netloc, path, parsed.params, query, ""))


def source_id_for(university_id: str, canonical_url: str) -> str:
    """Deterministic source_id from university + canonical URL.

    Backward compatible with the prior ``stable_id("src", university_id, netloc,
    path)`` derivation: it keys on netloc+path (which canonicalization leaves
    stable), so existing MIT source_ids are preserved while the stored
    canonical_url value is normalized.
    """
    parsed = urlparse(canonical_url)
    parts = [university_id, parsed.netloc, parsed.path]
    if parsed.query:
        parts.append(parsed.query)
    return stable_id("src", *parts)


# ---------------------------------------------------------------------------
# Markdown URL extraction (Plan §4.2)
# ---------------------------------------------------------------------------

_MARKDOWN_LINK_RE = re.compile(r"\[(?P<label>[^\]]*)\]\((?P<url>\s*(?:https?://|www\.)[^\s)]+)\s*(?:\"[^\"]*\")?\)")
_AUTOLINK_RE = re.compile(r"<(?P<url>(?:https?://|www\.)[^>\s]+)>")
# bare URL: an http(s) URL not already part of a markdown link/autolink; this runs
# after stripping those, so the remaining https?:// tokens are genuinely bare.
_BARE_URL_RE = re.compile(r"(?<![\w\"'\[\]\(<#/])(?:https?://|www\.)[^\s)\]\}<>\|\"'^`]+")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def _normalize_token_url(url: str) -> str:
    """Strip trailing markdown punctuation that is not part of the URL."""
    return url.strip().rstrip(".,);:'\"")


def _current_heading_path(lines: list[str], index: int) -> list[str]:
    """Walk backwards to collect the nearest heading chain (h1..h6 in order).

    For each heading level we keep the LAST title seen before ``index`` (a deeper
    section's siblings replace each other, but ancestor levels are preserved).
    """
    path: dict[int, str] = {}
    for line in lines[max(0, index - 2000):index]:
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            path[level] = title  # last title at this level wins
    return [path[level] for level in sorted(path)]


def extract_urls_from_markdown(text: str, *, lines: list[str] | None = None) -> list[ExtractedUrl]:
    """Extract every http(s) URL from Markdown text.

    Sources, in priority order (a URL matched as a markdown link is not also
    reported as bare):
      1. Markdown links ``[label](https://...)``
      2. Autolinks ``<https://...>``
      3. Bare ``https://...`` URLs

    Each result carries the nearest heading path (Plan §4.4: a URL in prose
    inherits the nearest Markdown heading path and topic classification).
    Invalid URLs (non-http(s), localhost, private network, malformed) are rejected.
    """
    if lines is None:
        lines = text.splitlines()

    consumed_spans: list[tuple[int, int]] = []  # (start, end) char offsets already claimed
    results: list[ExtractedUrl] = []

    def _overlaps(start: int, end: int) -> bool:
        return any(not (end <= s or start >= e) for (s, e) in consumed_spans)

    def _line_index_for_offset(offset: int) -> int:
        # cheap mapping: count newlines before offset
        return text.count("\n", 0, offset)

    # 1. Markdown links
    for m in _MARKDOWN_LINK_RE.finditer(text):
        url = _normalize_token_url(m.group("url"))
        canonical = canonicalize_url(url)
        if not is_valid_http_url(canonical):
            continue
        consumed_spans.append((m.start(), m.end()))
        results.append(
            ExtractedUrl(
                raw=url,
                canonical=canonical,
                heading_path=_current_heading_path(lines, _line_index_for_offset(m.start())),
                context="markdown_link",
            )
        )

    # 2. Autolinks
    for m in _AUTOLINK_RE.finditer(text):
        if _overlaps(m.start(), m.end()):
            continue
        url = _normalize_token_url(m.group("url"))
        canonical = canonicalize_url(url)
        if not is_valid_http_url(canonical):
            continue
        consumed_spans.append((m.start(), m.end()))
        results.append(
            ExtractedUrl(
                raw=url,
                canonical=canonical,
                heading_path=_current_heading_path(lines, _line_index_for_offset(m.start())),
                context="autolink",
            )
        )

    # 3. Bare URLs (anything not already consumed)
    for m in _BARE_URL_RE.finditer(text):
        if _overlaps(m.start(), m.end()):
            continue
        url = _normalize_token_url(m.group(0))
        canonical = canonicalize_url(url)
        if not is_valid_http_url(canonical):
            continue
        consumed_spans.append((m.start(), m.end()))
        results.append(
            ExtractedUrl(
                raw=url,
                canonical=canonical,
                heading_path=_current_heading_path(lines, _line_index_for_offset(m.start())),
                context="bare",
            )
        )

    return results


def deduplicate_extracted(extracted: list[ExtractedUrl]) -> dict[str, ExtractedUrl]:
    """Merge repeated URLs: keep the first occurrence, preserve all heading paths.

    Plan §4.4: repeated URLs merge topics and entry links instead of creating
    duplicate sources. Returns canonical_url -> representative ExtractedUrl.
    """
    merged: dict[str, ExtractedUrl] = {}
    for item in extracted:
        if item.canonical not in merged:
            merged[item.canonical] = item
        else:
            existing = merged[item.canonical]
            for heading in item.heading_path:
                if heading not in existing.heading_path:
                    existing.heading_path.append(heading)
    return merged


__all__ = [
    "ExtractedUrl",
    "TRACKING_PARAMS",
    "slug",
    "stable_id",
    "is_valid_http_url",
    "canonicalize_url",
    "source_id_for",
    "extract_urls_from_markdown",
    "deduplicate_extracted",
]
