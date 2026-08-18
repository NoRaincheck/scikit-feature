# LapScore

`skfeature.function.similarity_based.lap_score`

## Description

**Laplacian Score** is an unsupervised method. It builds an affinity graph over the samples and scores each feature by how well it preserves the local manifold structure of the data; lower scores indicate better features.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.similarity_based import lap_score

X, y = load_iris(return_X_y=True)  # labels are optional for this unsupervised method

# get a score for every feature (aligned with SelectKBest)
score = lap_score.lap_score(X, y)

# or get the indices of the selected features
selected = lap_score.lap_score(X, y, mode="index")
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` or `None` — optional class labels (unsupervised)
- `**kwargs`: optional `W` sparse affinity matrix, shape `(n_samples, n_samples)`
- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
