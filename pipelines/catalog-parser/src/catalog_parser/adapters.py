from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from .mit_parser import ParseResult, parse_mit_markdown
from .deep_v2_parser import parse_deep_v2_markdown
from .structured_markdown_parser import parse_structured_markdown
from .structured_markdown_parser import StructuredMarkdownContractError


ParserAdapter = Callable[[str, Path], ParseResult]


class ParserAdapterNotFoundError(ValueError):
    def __init__(self, university_id: str, available: list[str]) -> None:
        choices = ", ".join(available) if available else "none"
        super().__init__(f"No parser adapter registered for university_id={university_id!r}. Available adapters: {choices}.")
        self.university_id = university_id
        self.available = available


def _parse_mit_adapter(university_id: str, path: Path) -> ParseResult:
    return parse_mit_markdown(path)


def _parse_auto_adapter(university_id: str, path: Path) -> ParseResult:
    try:
        return parse_structured_markdown(university_id, path)
    except StructuredMarkdownContractError:
        return parse_deep_v2_markdown(university_id, path)


UNIVERSITY_ADAPTERS: dict[str, ParserAdapter] = {
    "mit": _parse_mit_adapter,
}


NAMED_ADAPTERS: dict[str, ParserAdapter] = {
    **UNIVERSITY_ADAPTERS,
    "auto": _parse_auto_adapter,
    "deep_v2": parse_deep_v2_markdown,
    "generic_structured": parse_structured_markdown,
}


def normalize_university_id(university_id: str) -> str:
    return university_id.strip().lower()


def registered_university_ids() -> list[str]:
    return sorted(UNIVERSITY_ADAPTERS)


def registered_adapter_names() -> list[str]:
    return sorted(NAMED_ADAPTERS)


def get_named_parser_adapter(adapter_name: str) -> ParserAdapter:
    normalized = normalize_university_id(adapter_name)
    try:
        return NAMED_ADAPTERS[normalized]
    except KeyError as exc:
        choices = ", ".join(registered_adapter_names())
        raise ValueError(f"No parser adapter named {adapter_name!r}. Available adapters: {choices}.") from exc


def get_parser_adapter(university_id: str, *, adapter_name: str | None = None, fallback_adapter_name: str | None = None) -> ParserAdapter:
    if adapter_name:
        return get_named_parser_adapter(adapter_name)
    normalized = normalize_university_id(university_id)
    try:
        return UNIVERSITY_ADAPTERS[normalized]
    except KeyError as exc:
        if fallback_adapter_name:
            return get_named_parser_adapter(fallback_adapter_name)
        raise ParserAdapterNotFoundError(normalized, registered_university_ids()) from exc


def parse_school_markdown(
    university_id: str,
    path: Path,
    *,
    adapter_name: str | None = None,
    fallback_adapter_name: str | None = None,
) -> ParseResult:
    normalized = normalize_university_id(university_id)
    return get_parser_adapter(
        normalized,
        adapter_name=adapter_name,
        fallback_adapter_name=fallback_adapter_name,
    )(normalized, path)
