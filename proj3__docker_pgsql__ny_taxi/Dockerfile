FROM python:3.13.11-slim
# Start with slim Python 3.13 image

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
## Copy uv binary from official uv image (multi-stage build pattern)

WORKDIR /app
# Set working directory

ENV PATH="/app/.venv/bin:$PATH" 
# Add virtual environment to PATH so we can use installed packages
# instead of ENTRYPOINT ["uv", "run" ...]

COPY "pyproject.toml" ".python-version" "uv.lock" ./
# Copy dependency files first (better layer caching)

RUN uv sync --locked
# Install dependencies from lock file (ensures reproducible builds)

COPY ingest_data_v3_click.py ./
# Copy application code

ENTRYPOINT ["python", "ingest_data_v3_click.py"]
# Set entry point