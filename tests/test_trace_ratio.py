from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

from skfeature.function.similarity_based import trace_ratio


def test_trace_ratio():
    X, y = make_classification(n_samples=200, n_features=20, n_informative=5, n_redundant=5, n_classes=2)
    X = X.astype(float)

    num_fea = 5
    kfold = KFold(n_splits=2, shuffle=True)

    # build pipeline
    pipeline = Pipeline(
        [("select top k", SelectKBest(score_func=trace_ratio.trace_ratio, k=num_fea)), ("linear svm", svm.LinearSVC())]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.5