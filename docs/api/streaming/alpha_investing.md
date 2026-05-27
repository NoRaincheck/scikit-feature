# Alpha Investing

**Module:** `skfeature.function.streaming.alpha_investing`

## Description

Alpha Investing. This algorithm performs online/sequential feature selection using the alpha investing rule, allowing features to be selected or rejected as data arrives in a streaming fashion.

## Usage

```python
from skfeature.function.streaming import alpha_investing
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = alpha_investing.select_feature(X, y, k=5)
print(f"Selected feature indices: {selected_features}")
```

## Parameters

- `X`: Feature matrix of shape (n_samples, n_features)
- `y`: Class labels of shape (n_samples,) or (n_samples, 1)
- `k`: Number of features to select

## Returns

- `selected_features`: Array of selected feature indices

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
