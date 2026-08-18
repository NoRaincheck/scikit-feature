# Getting Started

`scikit-feature` is an open-source feature selection repository in Python, originally
developed by the Data Mining and Machine Learning (DMML) Lab at Arizona State University.
This fork maintains and updates the library for compatibility with modern versions of
`scikit-learn`.

## What is feature selection?

Feature selection is the process of selecting a subset of relevant features (variables,
predictors) for use in model construction. It helps to:

-   Reduce overfitting
-   Improve accuracy
-   Reduce training time
-   Improve model interpretability

## Algorithm categories

The library organizes feature selection algorithms into several categories:

| Category | Description |
|----------|-------------|
| **Information Theoretical** | Algorithms based on information theory (mutual information, entropy) |
| **Similarity Based** | Algorithms that use similarity measures between samples |
| **Sparse Learning Based** | Algorithms using sparse representation and l2,1-norm regularization |
| **Statistical Based** | Statistical methods for evaluating feature relevance |
| **Structure Based** | Algorithms leveraging data structure (graphs, groups, trees) |
| **Wrapper Based** | Algorithm selection using a predetermined classifier |
| **Streaming** | Online/streaming feature selection algorithms |

## Project structure

The single package lives in `skfeature/`, organized by algorithm family:

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

The [Algorithms overview](../api/algorithms-overview.md) page lists every algorithm with a
link to its reference documentation.

## Next steps

-   [Installation](installation.md) — install the package with pip or from source
-   [Quick Start](quick-start.md) — run your first feature selection in minutes
-   [Algorithms overview](../api/algorithms-overview.md) — browse all available methods
-   [Contributing](../contributing.md) — learn how to add new algorithms

## License

This project is licensed under the [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).