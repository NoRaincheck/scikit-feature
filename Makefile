.PHONY: install test format lint help

help:
	@echo "Available commands:"
	@echo "  make install   - Install project and dev dependencies via uv"
	@echo "  make test      - Run pytest on the tests/ directory"
	@echo "  make format    - Format code with ruff format"
	@echo "  make lint      - Lint code with ruff check"

install:
	uv sync --group dev
	uv pip install -e .

test:
	uv run pytest tests/

format:
	uv run ruff format skfeature/ tests/

lint:
	uv run ruff check skfeature/ tests/
