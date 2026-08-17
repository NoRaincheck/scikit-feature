from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import KBinsDiscretizer

from skfeature.function.information_theoretical_based import MIFS


def test_mifs():
    X, y = make_classification(n_samples=400, n_features=30, n_informative=8, n_redundant=8, flip_y=0.02, n_classes=2)
    X = X.astype(float)

    # the mutual information based scores require discrete features
    X = KBinsDiscretizer(n_bins=5, encode="ordinal").fit_transform(X)
    X = X.astype(float)

    num_fea = 10
    kfold = KFold(n_splits=2, shuffle=True)

    # build pipeline
    pipeline = Pipeline(
        [("select top k", SelectKBest(score_func=MIFS.mifs, k=num_fea)), ("linear svm", svm.LinearSVC())]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.6
