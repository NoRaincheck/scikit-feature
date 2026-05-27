# Utilities Overview

This page provides an organized reference of all utility functions in scikit-feature.

| Module | File | Description |
|--------|------|-------------|
| Construct W | [construct_w](utility/construct_w.md) | Construct weight matrix for similarity-based methods |
| Data Discretization | [data_discretization](utility/data_discretization.md) | Discretize continuous features into categorical bins |
| Entropy Estimators | [entropy_estimators](utility/entropy_estimators.md) | Estimate entropy and mutual information from data |
| Mutual Information | [mutual_information](utility/mutual_information.md) | Compute mutual information between variables |
| Sparse Learning Utils | [sparse_learning](utility/sparse_learning.md) | Utilities for sparse learning algorithms |
| Unsupervised Evaluation | [unsupervised_evaluation](utility/unsupervised_evaluation.md) | Evaluation metrics for unsupervised feature selection |
| Util | [util](utility/util.md) | General utility functions |

## Common Patterns

Many utilities are shared across algorithm categories:

- **Entropy estimators** and **mutual information** computations are used by all information-theoretic methods
- **Weight matrix construction** is essential for similarity-based algorithms (LapScore, SPEC, etc.)
- **Sparse learning utils** support the L21-norm based algorithms
