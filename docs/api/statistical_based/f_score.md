# F-Score

`skfeature.function.statistical_based.f_score`

## Description

**F-Score** ranks features using the ANOVA F-value between each feature and the class labels, which measures how much of the feature variance is explained by class differences.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.statistical_based import f_score

X, y = load_iris(return_X_y=True)

# rank features and select the top k
selector = SelectKBest(score_func=f_score.f_score, k=2)
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

- Based on `sklearn.feature_selection.f_classif`.
