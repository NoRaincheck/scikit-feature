# CFS

`skfeature.function.statistical_based.CFS`

## Description

**CFS** (Correlation-based Feature Selection) evaluates feature subsets by a merit function that rewards features highly correlated with the class labels but uncorrelated with each other, using symmetrical uncertainty as the correlation measure.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.statistical_based import CFS

X, y = load_iris(return_X_y=True)

# rank features and select the top k
selector = SelectKBest(score_func=CFS.cfs, k=2)
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

- Hall, Mark A. "Correlation-based feature selection for machine learning." PhD thesis 1999.
