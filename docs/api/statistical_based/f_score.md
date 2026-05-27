# F-Score

**Module:** `skfeature.function.statistical_based.f_score`

## Description

F-Score (ANOVA F-test Score for feature ranking). Statistical methods evaluate the relationship between each feature and the target variable using statistical tests or measures.

## Usage

```python
from skfeature.function.statistical_based import f_score
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = f_score.select_feature(X, y, k=5)
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
