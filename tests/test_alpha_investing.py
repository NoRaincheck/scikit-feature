from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

from skfeature.function.streaming import alpha_investing


def test_alphainvesting():
    X, y = make_classification(n_samples=200, n_features=20, n_informative=5, n_redundant=5, n_classes=2)
    X = X.astype(float)
    y = y.astype(float)

    kfold = KFold(n_splits=2, shuffle=True)

    # build pipeline
    pipeline = Pipeline(
        [
            ("alphainvesting", alpha_investing.AlphaInvesting(w0=0.05, dw=0.05)),
            ("linear svm", svm.LinearSVC()),
        ]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.6
