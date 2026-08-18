# Algorithms Overview

This page provides an organized reference of all feature selection algorithms in
`scikit-feature`.

## Information Theoretical Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [MIM](information_theoretical_based/mim.md) | `mim` | Mutual Information Maximization |
| [MIFS](information_theoretical_based/mifs.md) | `mifs` | Mutual Information Feature Selection |
| [JMI](information_theoretical_based/jmi.md) | `jmi` | Joint Mutual Information |
| [CMIM](information_theoretical_based/cmim.md) | `cmim` | Conditional Mutual Information Maximization |
| [CIFE](information_theoretical_based/cife.md) | `cife` | Conditional Infomax Feature Extraction |
| [MRMR](information_theoretical_based/mrmr.md) | `mrmr` | Minimum Redundancy Maximum Relevance |
| [FCBF](information_theoretical_based/fcbf.md) | `fcbf` | Fast Correlation-Based Filter |
| [DISR](information_theoretical_based/disr.md) | `disr` | Double Input Symmetrical Relevance |
| [ICAP](information_theoretical_based/icap.md) | `icap` | Interaction Capping |
| [LCSI](information_theoretical_based/lcsi.md) | `lcsi` | Local Conditional Score Improvement |

## Similarity Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [Fisher Score](similarity_based/fisher_score.md) | `fisher_score` | Fisher score for feature ranking |
| [LapScore](similarity_based/lap_score.md) | `lap_score` | Laplacian score |
| [ReliefF](similarity_based/relieff.md) | `reliefF` | Relief-F algorithm |
| [SPEC](similarity_based/spec.md) | `SPEC` | Spectral feature selection |
| [Trace Ratio](similarity_based/trace_ratio.md) | `trace_ratio` | Trace ratio criterion |

## Sparse Learning Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [RFS](sparse_learning_based/rfs.md) | `RFS` | Robust feature selection via joint l2,1-norms |
| [MCFS](sparse_learning_based/mcfs.md) | `MCFS` | Multi-cluster feature selection |
| [NDFS](sparse_learning_based/ndfs.md) | `NDFS` | Nonnegative spectral feature selection |
| [UDFS](sparse_learning_based/udfs.md) | `UDFS` | l2,1-norm regularized unsupervised feature selection |
| [ll_l21](sparse_learning_based/ll_l21.md) | `ll_l21` | Logistic loss with l2,1-norm regularization |
| [ls_l21](sparse_learning_based/ls_l21.md) | `ls_l21` | Least squares with l2,1-norm regularization |

## Statistical Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [t-Score](statistical_based/t_score.md) | `t_score` | Student's t-test score |
| [F-Score](statistical_based/f_score.md) | `f_score` | ANOVA F-test score |
| [Chi-Square](statistical_based/chi_square.md) | `chi_square` | Chi-square test |
| [Gini Index](statistical_based/gini_index.md) | `gini_index` | Gini index |
| [Low Variance](statistical_based/low_variance.md) | `low_variance` | Low variance threshold |
| [CFS](statistical_based/cfs.md) | `CFS` | Correlation-based feature selection |

## Structure Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [Graph FS](structure/graph_fs.md) | `graph_fs` | Graph-based feature selection |
| [Group FS](structure/group_fs.md) | `group_fs` | Group-based feature selection |
| [Tree FS](structure/tree_fs.md) | `tree_fs` | Tree-structured feature selection |

## Wrapper Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [SVM Forward](wrapper/svm_forward.md) | `svm_forward` | SVM-based forward selection |
| [SVM Backward](wrapper/svm_backward.md) | `svm_backward` | SVM-based backward elimination |
| [Decision Tree Forward](wrapper/decision_tree_forward.md) | `decision_tree_forward` | Decision-tree-based forward selection |
| [Decision Tree Backward](wrapper/decision_tree_backward.md) | `decision_tree_backward` | Decision-tree-based backward elimination |

## Streaming Based

| Algorithm | Module | Description |
|-----------|--------|-------------|
| [Alpha Investing](streaming/alpha_investing.md) | `alpha_investing` | Streamwise (online) feature selection |

## See also

-   [Utilities overview](../api/utilities-overview.md) — shared helpers used by the algorithms above