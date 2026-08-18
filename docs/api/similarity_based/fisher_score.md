# Fisher Score

`skfeature.function.similarity_based.fisher_score`

## Description

**Fisher Score** is a supervised ranking method. For each feature it measures the ratio of between-class variance to within-class variance; features with high scores are discriminative and are ranked first.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.similarity_based import fisher_score

X, y = load_iris(return_X_y=True)

# get a score for every feature (aligned with SelectKBest)
score = fisher_score.fisher_score(X, y)

# or get the indices of the selected features
selected = fisher_score.fisher_score(X, y, mode="index")
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
