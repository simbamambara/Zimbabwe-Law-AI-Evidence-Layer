FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
COPY scripts ./scripts
COPY data ./data
RUN python -m pip install --no-cache-dir -e .
CMD ["python", "scripts/validate_dataset.py"]
