# scikit-feature

An open-source **feature selection repository** in Python, originally developed by the
Data Mining and Machine Learning (DMML) Lab at Arizona State University. This fork keeps the
library compatible with modern versions of `scikit-learn`.

`scikit-feature` serves as a platform for feature selection application, research, and
comparative study. It shares widely used feature selection algorithms and offers
researchers and practitioners a convenient way to perform empirical evaluation when
developing new feature selection methods.

## Why scikit-feature?

<div class="grid cards" markdown>

-   :material-chart-box:{ .lg .middle } **Comprehensive**

    Over 35 feature selection algorithms across information-theoretic, similarity-based,
    sparse-learning, statistical, structure, wrapper, and streaming categories.

-   :material-package-variant:{ .lg .middle } **Easy to use**

    Clean, scikit-learn compatible API. Use any scoring function directly with
    `SelectKBest`, or drop streamwise/wrapper methods into your existing pipelines.

-   :material-book-open-page-variant:{ .lg .middle } **Well documented**

    Every algorithm has its own reference page with usage examples, parameters, and
    references to the original papers.

-   :material-sync:{ .lg .middle } **Actively maintained**

    This fork keeps the original algorithms working against current versions of
    `scikit-learn`, `numpy`, and `pandas` (Python 3.10+).

</div>

## Getting started

```bash
pip install skfeature-chappers
```

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.statistical_based import t_score

X, y = load_iris(return_X_y=True)
selector = SelectKBest(score_func=t_score.t_score, k=2)
X_selected = selector.fit_transform(X, y)
```

Head over to the [Getting Started](guide/getting-started.md) guide for installation
instructions and a [Quick Start](guide/quick-start.md) tutorial, or browse the
[algorithm reference](api/algorithms-overview.md) for the full list of available methods.

## Project information

*   **Forked project site** — https://github.com/NoRaincheck/scikit-feature
*   **Original project site** — https://github.com/jundongl/scikit-feature
*   **Original documentation** — http://featureselection.asu.edu/

## License

This project is licensed under the [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).