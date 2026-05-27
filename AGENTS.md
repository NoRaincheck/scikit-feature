# AGENTS.md

## Project

`skfeature-chappers` — an unofficial fork of the [scikit-feature](https://github.com/jundongl/scikit-feature) repository (originally from DMML Lab@ASU). It provides a collection of feature selection algorithms for Python, built on top of scikit-learn, pandas, and numpy.

The single package lives in `skfeature/` with submodules organized by algorithm family:

| Submodule | Path |
| --- | --- |
| Information-theoretical-based | `skfeature/function/information_theoretical_based/` |
| Similarity-based | `skfeature/function/similarity_based/` |
| Sparse-learning-based | `skfeature/function/sparse_learning_based/` |
| Statistical-based | `skfeature/function/statistical_based/` |
| Streaming | `skfeature/function/streaming/` |
| Structure | `skfeature/function/structure/` |
| Wrapper | `skfeature/function/wrapper/` |
| Utilities | `skfeature/utility/` |

## Workflow

- `uv sync --group dev` — install dependencies
- `make test` — run pytest on the tests/ directory
- `make format` — format code with ruff format
- `make lint` — lint code with ruff check
- `make serve-docs` — serve documentation locally via docsify (open http://localhost:8080)

## Change discipline

Keep changes small and focused. Make one logical change at a time. This prevents
context overload for both humans and automated tools. Do not refactor unrelated
code while working on a task — that can wait.

## Coding rules

- Keep files between 150-500 LoC, functions small and focused
- Prefer explicit over clever; use boring, consistent names
- Leave `__init__.py` empty unless re-exporting public API
- Add comments only when intent isn't clear from the code
- Use `.gitignore` awareness in file-search tools (grep, find)

Ruff is configured with a 120-character line length. It targets Python 3.10+ and enables `E`, `F`, `W`, `I`, `UP`, `B`, `SIM` rulesets (`E203` and `E501` are ignored).

## Testing

Focused tests for core behavior and edge cases. Tests live in `tests/` at the
workspace root, one file per algorithm or feature group. Run via:

```bash
make test          # pytest on tests/
uv run pytest      # same, with coverage flags if configured
```

## Documentation

Documentation lives in `docs/` and is served locally by docsify. The main entry
point is `index.html`. Never embed file-tree listings in README.md files —
describe layout at a high level instead.

## Dependencies

Runtime: `scikit-learn`, `pandas`, `numpy` (Python 3.10+).  
Dev-only: `pytest`, `pytest-cov`, `ruff`, `ty`.
