# Construct W

`skfeature.utility.construct_W`

## Description

**Construct W** builds the affinity (similarity) matrix used by similarity-based and spectral feature selection methods. It supports several graph construction strategies, including k-nearest-neighbor and heat-kernel weighting.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.utility import construct_W

X, y = load_iris(return_X_y=True)
W = construct_W.construct_W(X)
```

## Functions

- `construct_W(X, **kwargs)`: build the affinity matrix `W` of shape `(n_samples, n_samples)` from the input data. Supported strategies include `knn` (k-nearest-neighbor) and `heat` (heat kernel).
