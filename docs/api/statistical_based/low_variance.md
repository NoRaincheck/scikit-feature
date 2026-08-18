# Low Variance

`skfeature.function.statistical_based.low_variance`

## Description

**Low Variance** removes features whose variance falls below a threshold. It is a simple unsupervised filter useful for dropping constant or near-constant features before applying other methods.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.statistical_based import low_variance

X, y = load_iris(return_X_y=True)

# drop features with variance below the threshold
X_selected = low_variance.low_variance_feature_selection(X, threshold=0.5)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `threshold`: `float`, default `0.0` — minimum variance a feature must have to be kept
- `mode`: `{"rank", "index"}`, default `"rank"`

## Returns

- `X_selected`: transformed data with low-variance features removed

## References

- Based on `sklearn.feature_selection.VarianceThreshold`.
