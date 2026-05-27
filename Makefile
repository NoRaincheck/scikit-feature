.PHONY: install test format lint help serve-docs

help:
	@echo "Available commands:"
	@echo "  make install    - Install project and dev dependencies via uv"
	@echo "  make test       - Run pytest on the tests/ directory"
	@echo "  make format     - Format code with ruff format"
	@echo "  make lint       - Lint code with ruff check"
	@echo "  make serve-docs - Serve documentation locally via docsify"

install:
	uv sync --group dev
	uv pip install -e .

test:
	uv run pytest tests/

format:
	uv run ruff format skfeature/ tests/

lint:
	uv run ruff check skfeature/ tests/

serve-docs:
	python3 -m http.server 8080 --directory .
