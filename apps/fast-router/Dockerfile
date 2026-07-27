FROM docker.m.daocloud.io/library/python:3.11-slim

ARG PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN python -m venv "$VIRTUAL_ENV"

COPY apps/fast-router/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --index-url="$PIP_INDEX_URL" -r /app/requirements.txt

COPY apps/fast-router/src /app/apps/fast-router/src
COPY pipelines/catalog-parser/src /app/pipelines/catalog-parser/src
COPY pipelines/indexer/src /app/pipelines/indexer/src
COPY infra/opensearch /app/infra/opensearch
COPY infra/postgres /app/infra/postgres
COPY docs/schemas /app/docs/schemas
COPY scripts /app/scripts

ENV PYTHONPATH=/app/apps/fast-router/src:/app/pipelines/catalog-parser/src:/app/pipelines/indexer/src
CMD ["uvicorn", "fast_router.main:app", "--host", "0.0.0.0", "--port", "8000"]
