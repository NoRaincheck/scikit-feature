# Algorithms Overview

This page provides an organized reference of all feature selection algorithms in scikit-feature.

## Information Theoretical Based

| Algorithm | File | Description |
|-----------|------|-------------|
| MIM | [mim](information_theoretical_based/mim.md) | Mutual Information Maximization |
| MIFS | [mifs](information_theoretical_based/mifs.md) | Mutual Information Feature Selection |
| JMI | [jmi](information_theoretical_based/jmi.md) | Joint Mutual Information |
| CMIM | [cmim](information_theoretical_based/cmim.md) | Conditional Maximal Importance |
| CIFE | [cife](information_theoretical_based/cife.md) | Conditional Information Feature Extraction |
| MRMR | [mrmr](information_theoretical_based/mrmr.md) | Minimum Redundancy Maximum Relevance |
| FCBF | [fcbf](information_theoretical_based/fcbf.md) | Fast Correlation Filter Bank |
| DISR | [disr](information_theoretical_based/disr.md) | Discriminative Information Selection for Regression |
| ICAP | [icap](information_theoretical_based/icap.md) | Interaction Capping |
| LCSI | [lcsi](information_theoretical_based/lcsi.md) | Local Conditional Score Improvement |

## Similarity Based

| Algorithm | File | Description |
|-----------|------|-------------|
| Fisher Score | [fisher_score](similarity_based/fisher_score.md) | Fisher Score for feature ranking |
| LapScore | [lap_score](similarity_based/lap_score.md) | Laplacian Score |
| ReliefF | [relieff](similarity_based/relieff.md) | Relief-F algorithm |
| SPEC | [spec](similarity_based/spec.md) | Spectral Feature Selection |
| Trace Ratio | [trace_ratio](similarity_based/trace_ratio.md) | Trace Ratio Criterion |

## Sparse Learning Based

| Algorithm | File | Description |
|-----------|------|-------------|
| RFS | [rfs](sparse_learning_based/rfs.md) | Robust Feature Selection |
| MCFS | [mcfs](sparse_learning_based/mcfs.md) | Multivariate Cluster Feature Selection |
| NDFS | [ndfs](sparse_learning_based/ndfs.md) | Non-negative Dual View Clustering |
| UDFS | [udfs](sparse_learning_based/udfs.md) | Unsupervised Discriminative Feature Selection |
| Ll_l21 | [ll_l21](sparse_learning_based/ll_l21.md) | L1,2 Norm Regularization |
| Ls_l21 | [ls_l21](sparse_learning_based/ls_l21.md) | Least Squares with L21 Norm |

## Statistical Based

| Algorithm | File | Description |
|-----------|------|-------------|
| t-Score | [t_score](statistical_based/t_score.md) | Student's t-test Score |
| F-Score | [f_score](statistical_based/f_score.md) | ANOVA F-test Score |
| Chi-Square | [chi_square](statistical_based/chi_square.md) | Chi-Square Test |
| Gini Index | [gini_index](statistical_based/gini_index.md) | Gini Index |
| Low Variance | [low_variance](statistical_based/low_variance.md) | Low Variance Threshold |
| CFS | [cfs](statistical_based/cfs.md) | Correlation-based Feature Selection |

## Structure Based

| Algorithm | File | Description |
|-----------|------|-------------|
| Graph FS | [graph_fs](structure/graph_fs.md) | Graph-based Feature Selection |
| Group FS | [group_fs](structure/group_fs.md) | Group-based Feature Selection |
| Tree FS | [tree_fs](structure/tree_fs.md) | Tree-based Feature Selection |

## Wrapper Based

| Algorithm | File | Description |
|-----------|------|-------------|
| SVM Forward | [svm_forward](wrapper/svm_forward.md) | SVM-based Forward Selection |
| SVM Backward | [svm_backward](wrapper/svm_backward.md) | SVM-based Backward Elimination |
| Decision Tree Forward | [decision_tree_forward](wrapper/decision_tree_forward.md) | DT-based Forward Selection |
| Decision Tree Backward | [decision_tree_backward](wrapper/decision_tree_backward.md) | DT-based Backward Elimination |

## Streaming Based

| Algorithm | File | Description |
|-----------|------|-------------|
| Alpha Investing | [alpha_investing](streaming/alpha_investing.md) | Alpha Investing Rule for Online Feature Selection |
