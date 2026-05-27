# Getting Started

`scikit-feature` is an open-source feature selection repository in Python, originally developed by the Data Mining and Machine Learning (DMML) Lab at Arizona State University. This fork maintains and updates the library for compatibility with modern versions of `scikit-learn`.

## What is Feature Selection?

Feature selection is the process of selecting a subset of relevant features (variables, predictors) for use in model construction. It helps to:

- Reduce overfitting
- Improve accuracy
- Reduce training time
- Improve model interpretability

## Algorithm Categories

The library organizes feature selection algorithms into several categories:

| Category | Description |
|----------|-------------|
| **Information Theoretical** | Algorithms based on information theory (mutual information, entropy) |
| **Similarity Based** | Algorithms that use similarity measures between samples |
| **Sparse Learning Based** | Algorithms using sparse representation and L21 norm regularization |
| **Statistical Based** | Statistical methods for evaluating feature relevance |
| **Structure Based** | Algorithms leveraging data structure (graphs, groups, trees) |
| **Wrapper Based** | Algorithm selection using a predetermined classifier |
| **Streaming** | Online/streaming feature selection algorithms |

## Project Structure

```
skfeature/
├── function/
│   ├── information_theoretical_based/  # Information-theoretic methods
│   ├── similarity_based/               # Similarity-based methods
│   ├── sparse_learning_based/          # Sparse learning methods
│   ├── statistical_based/              # Statistical methods
│   ├── structure/                      # Structure-based methods
│   ├── wrapper/                        # Wrapper methods
│   └── streaming/                      # Streaming methods
└── utility/                            # Utility functions
```

## License

This project is licensed under the [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
