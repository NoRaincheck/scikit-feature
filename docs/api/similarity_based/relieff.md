# ReliefF

`skfeature.function.similarity_based.reliefF`

## Description

**ReliefF** is a supervised instance-based method. It estimates feature quality by repeatedly sampling an instance and updating feature weights based on its nearest neighbors from the same and different classes.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.similarity_based import reliefF

X, y = load_iris(return_X_y=True)

# get a score for every feature (aligned with SelectKBest)
score = reliefF.reliefF(X, y)

# or get the indices of the selected features
selected = reliefF.reliefF(X, y, mode="index")
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `**kwargs`: optional `k` number of neighbors (default `5`)
- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
