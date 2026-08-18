# Sparse Learning Utils

`skfeature.utility.sparse_learning`

## Description

**Sparse Learning Utils** contains shared helpers for the sparse-learning feature selection algorithms, including feature ranking from weight matrices, label matrix construction, l2,1-norm computation, and proximal operators.

## Usage

```python
import numpy as np

from skfeature.utility import sparse_learning

W = np.random.rand(10, 3)
ranking = sparse_learning.feature_ranking(W)
```

## Functions

- `feature_ranking(W)`: rank features according to the l2-norms of the rows of the weight matrix `W`
- `generate_diagonal_matrix(U)`: build a diagonal matrix from the row l2-norms of `U`
- `calculate_l21_norm(X)`: compute the l2,1 norm of a matrix
- `construct_label_matrix(label)`: build a one-hot label matrix
- `construct_label_matrix_pan(label)`: build a binarized label matrix
- `euclidean_projection(V, n_features, n_classes, z, gamma)`: euclidean projection step used by l2,1 solvers
- `tree_lasso_projection(v, n_features, idx, n_nodes)`: projection for tree-structured lasso
- `tree_norm(w, n_features, idx, n_nodes)`: tree-structured group norm
