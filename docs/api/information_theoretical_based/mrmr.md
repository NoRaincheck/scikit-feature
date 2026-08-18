# MRMR

`skfeature.function.information_theoretical_based.mrmr`

## Description

**MRMR** (Minimum Redundancy Maximum Relevance) selects features that are highly relevant to the class labels while minimizing the average redundancy with the already selected features, i.e. `J(f) = I(f; y) - mean_j I(fj; f)`.

!!! note
    This information-theoretic method requires **discrete** input features. Discretize continuous data first, for example with `sklearn.preprocessing.KBinsDiscretizer`.


## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import KBinsDiscretizer

from skfeature.function.information_theoretical_based import mrmr

X, y = load_iris(return_X_y=True)

# information-theoretic scores require discrete features
X = KBinsDiscretizer(n_bins=5, encode="ordinal").fit_transform(X).astype(float)

# integrate with scikit-learn pipelines via SelectKBest
selector = SelectKBest(score_func=mrmr.mrmr, k=5)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first
- `X`: `numpy array`, shape `(n_samples, n_features)` — input data, must be discrete
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `**kwargs`: additional parameters (see `n_selected_features` below)

Optional keyword arguments:

- `n_selected_features`: `int` — number of features to select

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Peng, Hanchuan, Long, Fuhui, and Ding, Chris. "Feature selection based on mutual information criteria of max-dependency, max-relevance, and min-redundancy." IEEE TPAMI 2005.
