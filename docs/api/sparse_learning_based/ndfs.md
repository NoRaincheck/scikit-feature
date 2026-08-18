# NDFS

`skfeature.function.sparse_learning_based.NDFS`

## Description

**NDFS** (Nonnegative Discriminative Feature Selection) is an unsupervised method that performs spectral clustering and feature selection jointly under a nonnegative constraint on the cluster indicator matrix.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.sparse_learning_based import NDFS

X, y = load_iris(return_X_y=True)

# rank features via SelectKBest-compatible scoring
selector = SelectKBest(score_func=NDFS.ndfs, k=5)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array` or `None` — optional labels (unsupervised)
- `**kwargs`: optional `W` affinity matrix and `gamma`
- `mode`: `{"rank", "index"}`, default `"rank"`

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Li, Zechao et al. "Unsupervised feature selection via nonnegative spectral analysis and redundancy control." IEEE TIP 2015.
