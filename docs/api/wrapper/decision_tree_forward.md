# Decision Tree Forward

**Module:** `skfeature.function.wrapper.decision_tree_forward`

## Description

Decision Tree Forward (DT-based Forward Selection). Wrapper methods use a predetermined classifier to evaluate subsets of features. They generally provide better performance than filter methods but at higher computational cost.

## Usage

```python
from skfeature.function.wrapper import decision_tree_forward
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = decision_tree_forward.select_feature(X, y, k=5)
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
