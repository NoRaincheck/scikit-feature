# t-Score

`skfeature.function.statistical_based.t_score`

## Description

**t-Score** ranks features using a two-sample t-test style statistic for each feature across the class labels, favoring features whose class means are well separated relative to the within-class spread.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.statistical_based import t_score

X, y = load_iris(return_X_y=True)

# rank features and select the top k
selector = SelectKBest(score_func=t_score.t_score, k=2)
X_selected = selector.fit_transform(X, y)
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
