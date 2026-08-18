# MIFS

`skfeature.function.information_theoretical_based.mifs`

## Description

**MIFS** (Mutual Information Feature Selection) extends MIM by penalizing redundancy between the candidate feature and the already selected ones, i.e. `J(f) = I(f; y) - beta * sum_j I(fj; f)`, with `beta = 0.5` by default.

!!! note
    This information-theoretic method requires **discrete** input features. Discretize continuous data first, for example with `sklearn.preprocessing.KBinsDiscretizer`.


## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import KBinsDiscretizer

from skfeature.function.information_theoretical_based import mifs

X, y = load_iris(return_X_y=True)

# information-theoretic scores require discrete features
X = KBinsDiscretizer(n_bins=5, encode="ordinal").fit_transform(X).astype(float)

# integrate with scikit-learn pipelines via SelectKBest
selector = SelectKBest(score_func=mifs.mifs, k=5)
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

- Battiti, Roberto. "Using mutual information for selecting features in supervised neural net learning." IEEE TNN 1994.
