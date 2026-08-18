# Quick Start

This page walks you through the basic usage of `scikit-feature`. All scoring functions
integrate with scikit-learn through `SelectKBest`, so you can plug them into any existing
`Pipeline`.

## Basic usage

Here is a minimal example using the t-score filter:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.statistical_based import t_score

X, y = load_iris(return_X_y=True)

# Select the top 2 features
selector = SelectKBest(score_func=t_score.t_score, k=2)
X_selected = selector.fit_transform(X, y)
print(f"Selected feature indices: {selector.get_support(indices=True)}")
```

## Information-theoretic methods

Information-theoretic algorithms (MRMR, JMI, MIM, ...) require **discrete** features.
Discretize continuous data first with `KBinsDiscretizer`:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import KBinsDiscretizer

from skfeature.function.information_theoretical_based import MRMR

X, y = load_breast_cancer(return_X_y=True)
X = KBinsDiscretizer(n_bins=5, encode="ordinal").fit_transform(X).astype(float)

# Select the top 10 features using MRMR
selector = SelectKBest(score_func=MRMR.mrmr, k=10)
X_selected = selector.fit_transform(X, y)
print(f"Selected feature indices: {selector.get_support(indices=True)}")
```

## Wrapper methods

Wrapper methods evaluate subsets using a classifier and can be called directly. They need
the number of features to keep, so they are not wired through `SelectKBest`:

```python
from sklearn.datasets import load_wine
from sklearn.svm import LinearSVC

from skfeature.function.wrapper import svm_forward

X, y = load_wine(return_X_y=True)

# Select the top 5 features using SVM-based forward selection
selected = svm_forward.svm_forward(X, y, n_selected_features=5, mode="index")
print(f"Selected feature indices: {selected}")
```

## Choosing the right algorithm

| Use case | Recommended method |
|----------|-------------------|
| General purpose, fast | `t_score`, `f_score` (Statistical) |
| Capturing feature interactions | `MIM`, `MRMR`, `JMI` (Information Theoretical) |
| High-dimensional data | `RFS`, `MCFS` (Sparse Learning) |
| Small sample size | `ReliefF`, `LapScore` (Similarity Based) |
| Domain-specific groups | `Group FS` (Structure Based) |
| Streaming/online scenarios | `Alpha Investing` (Streaming) |

## Getting feature scores

Most filters also expose the raw scores directly. The returned array is aligned with
`SelectKBest`, i.e. entry `i` holds the score of feature `i`:

```python
from sklearn.datasets import load_iris

from skfeature.function.similarity_based import fisher_score

X, y = load_iris(return_X_y=True)

scores = fisher_score.fisher_score(X, y)
print(f"Fisher scores: {scores}")
```

## Using a pipeline

Because every scoring function is `SelectKBest`-compatible, you can compose a full
classification pipeline in a single step:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.svm import LinearSVC

from skfeature.function.information_theoretical_based import JMI

X, y = load_breast_cancer(return_X_y=True)
X = KBinsDiscretizer(n_bins=5, encode="ordinal").fit_transform(X).astype(float)

pipeline = Pipeline(
    [
        ("select", SelectKBest(score_func=JMI.jmi, k=10)),
        ("svm", LinearSVC()),
    ]
)

print(cross_val_score(pipeline, X, y, cv=3).mean())
```