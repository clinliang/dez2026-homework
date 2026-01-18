# Use Python 3.13 slim base image 
FROM python:3.13.11-slim

# Install uv binary from official image 
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set venv path to /app/.venv (Matches docker-compose volume protection)
ENV UV_PROJECT_ENVIRONMENT=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_PYTHON_PREFERENCE=only-managed

# Set working directory 
WORKDIR /app

# Copy dependency files for caching under WORKDIR
COPY "pyproject.toml" "uv.lock" ./

# Install dependencies (Libraries only, NOT the project itself)
# Added --no-install-project because source code isn't copied yet
RUN uv sync --frozen --no-dev --no-install-project --no-cache

# Copy application source code under WORKDIR
COPY . . 

# Create data directory (Just in case, though volume mount covers it)
RUN mkdir -p /app/data

# Default to bash shell
CMD ["bash"]