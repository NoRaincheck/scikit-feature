# SPEC

`skfeature.function.similarity_based.SPEC`

## Description

**SPEC** (Spectral Feature Selection) is a spectral method that can be used in both supervised and unsupervised settings. It scores features by their consistency with the eigenvectors of a similarity (affinity) matrix of the samples.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.similarity_based import SPEC

X, y = load_iris(return_X_y=True)

# get a score for every feature (aligned with SelectKBest)
score = SPEC.spec(X, y)

# or get the indices of the selected features
selected = SPEC.spec(X, y, mode="index")
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` or `None` — optional class labels
- `**kwargs`: additional parameters (e.g. `n_neighbors` for the similarity graph)
- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
