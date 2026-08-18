# Chi-Square

`skfeature.function.statistical_based.chi_square`

## Description

**Chi-Square** measures the dependence between each feature and the class labels using the chi-square statistic. It is a standard filter for classification and is well suited to count-based or non-negative features.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.statistical_based import chi_square

X, y = load_iris(return_X_y=True)

# rank features and select the top k
selector = SelectKBest(score_func=chi_square.chi_square, k=2)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data, must be non-negative
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Based on `sklearn.feature_selection.chi2`.
