from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
from sklearn.preprocessing import KBinsDiscretizer

from skfeature.function.wrapper import svm_backward, svm_forward


def _discrete_classification_data():
    X, y = make_classification(n_samples=400, n_features=30, n_informative=8, n_redundant=8, flip_y=0.02, n_classes=2)
    X = X.astype(float)
    X = KBinsDiscretizer(n_bins=5, encode="ordinal").fit_transform(X)
    return X.astype(float), y


def test_svm_backward():
    X, y = _discrete_classification_data()
    kfold = KFold(n_splits=2, shuffle=True)

    # svm_backward needs the number of features to keep, so it cannot be wired
    # through SelectKBest; call it directly and refit on the selected subset
    accuracies = []
    for train_index, test_index in kfold.split(X):
        F = svm_backward.svm_backward(X[train_index], y[train_index], n_selected_features=10, mode="index")
        clf = svm.LinearSVC()
        clf.fit(X[train_index][:, F], y[train_index])
        accuracies.append(clf.score(X[test_index][:, F], y[test_index]))

    results = accuracies
    print(f"Accuracy: {sum(results) / len(results)}")
    assert sum(results) / len(results) > 0.6


def test_svm_forward():
    X, y = _discrete_classification_data()
    kfold = KFold(n_splits=2, shuffle=True)

    # svm_forward needs the number of features to keep, so call it directly
    accuracies = []
    for train_index, test_index in kfold.split(X):
        F = svm_forward.svm_forward(X[train_index], y[train_index], n_selected_features=10, mode="index")
        clf = svm.LinearSVC()
        clf.fit(X[train_index][:, F], y[train_index])
        accuracies.append(clf.score(X[test_index][:, F], y[test_index]))

    results = accuracies
    print(f"Accuracy: {sum(results) / len(results)}")
    assert sum(results) / len(results) > 0.6
