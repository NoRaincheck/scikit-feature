# Data Discretization

`skfeature.utility.data_discretization`

## Description

**Data Discretization** converts continuous features into discrete bins. This is required as a preprocessing step before running the information-theoretic feature selection algorithms, which expect discrete inputs.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.utility import data_discretization

X, y = load_iris(return_X_y=True)
X_discrete = data_discretization.data_discretization(X, n_bins=5)
```

## Functions

- `data_discretization(X, n_bins)`: discretize each feature into `n_bins` equal-width bins and return the discretized matrix.
