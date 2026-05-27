# Quick Start

## Basic Usage

Here's a minimal example of using scikit-feature for feature selection:

```python
from skfeature.function.statistical_based import t_score
import numpy as np
from sklearn.datasets import load_iris

# Load sample data
X, y = load_iris(return_X_y=True)

# Select top 2 features using t-score
selected_features = t_score.select_feature(X, y, k=2)
print(f"Selected feature indices: {selected_features}")
```

## Example with Information Theoretical Methods

```python
from skfeature.function.information_theoretical_based import MRMR
import numpy as np
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

# Select top 10 features using MRMR (Minimum Redundancy Maximum Relevance)
selected_features = MRMR.select_feature(X, y, k=10)
print(f"Selected feature indices: {selected_features}")
```

## Example with Wrapper Methods

```python
from skfeature.function.wrapper import svm_forward
import numpy as np
from sklearn.datasets import load_wine

X, y = load_wine(return_X_y=True)

# Select top 5 features using SVM-based forward selection
selected_features = svm_forward.select_feature(X, y, k=5)
print(f"Selected feature indices: {selected_features}")
```

## Choosing the Right Algorithm

| Use Case | Recommended Method |
|----------|-------------------|
| General purpose, fast | `t_score`, `f_score` (Statistical) |
| Capturing feature interactions | `MIM`, `MRMR`, `JMI` (Information Theoretical) |
| High-dimensional data | `RFS`, `MCFS` (Sparse Learning) |
| Small sample size | `ReliefF`, `LapScore` (Similarity Based) |
| Domain-specific groups | `Group FS` (Structure Based) |
| Streaming/online scenarios | `Alpha Investing` (Streaming) |

## Getting Feature Scores

Most algorithms also provide score access:

```python
from skfeature.function.similarity_based import fisher_score

X, y = load_iris(return_X_y=True)

# Get Fisher scores for all features
scores = fisher_score.fisher_score(X, y)
print(f"Fisher scores: {scores}")
