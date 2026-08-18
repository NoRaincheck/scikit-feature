# Utilities Overview

This page provides an organized reference of all utility modules in `scikit-feature`.

| Module | File | Description |
|--------|------|-------------|
| [Construct W](utility/construct_w.md) | `construct_W` | Construct weight matrix for similarity-based methods |
| [Data Discretization](utility/data_discretization.md) | `data_discretization` | Discretize continuous features into categorical bins |
| [Entropy Estimators](utility/entropy_estimators.md) | `entropy_estimators` | Estimate entropy and mutual information from data |
| [Mutual Information](utility/mutual_information.md) | `mutual_information` | Compute mutual information between variables |
| [Sparse Learning Utils](utility/sparse_learning.md) | `sparse_learning` | Utilities for sparse learning algorithms |
| [Unsupervised Evaluation](utility/unsupervised_evaluation.md) | `unsupervised_evaluation` | Evaluation metrics for unsupervised feature selection |
| [Util](utility/util.md) | `util` | General utility functions |

## Common patterns

Many utilities are shared across algorithm categories:

-   **Entropy estimators** and **mutual information** computations are used by all
    information-theoretic methods
-   **Weight matrix construction** is essential for similarity-based algorithms
    (LapScore, SPEC, etc.)
-   **Sparse learning utils** support the l2,1-norm based algorithms
-   **Data discretization** prepares continuous data for the information-theoretic methods

## See also

-   [Algorithms overview](../api/algorithms-overview.md) — every algorithm that relies on
    these utilities