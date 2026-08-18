.PHONY: install test format lint typecheck help serve-docs build-docs

help:
	@echo "Available commands:"
	@echo "  make install    - Install project and dev dependencies via uv"
	@echo "  make test       - Run pytest on the tests/ directory"
	@echo "  make format     - Format code with ruff format"
	@echo "  make lint       - Lint code with ruff check"
	@echo "  make typecheck  - Type-check code with ty"
	@echo "  make serve-docs - Serve documentation locally via mkdocs (http://localhost:8000)"
	@echo "  make build-docs - Build the documentation site into site/"

install:
	uv sync --group dev
	uv pip install -e .

test:
	uv run pytest tests/

format:
	uv run ruff format skfeature/ tests/

lint:
	uv run ruff check skfeature/ tests/

typecheck:
	uv run ty check skfeature/ tests/

serve-docs:
	uv run --group docs mkdocs serve

build-docs:
	uv run --group docs mkdocs build
