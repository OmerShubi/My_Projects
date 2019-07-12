# Original code was provided by:
# Original author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>

# Import datasets, classifiers and performance metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.preprocessing import StandardScaler

from Lab6.analysis_functions import *


def label_with_max_error(test_images, test_labels, predicted, show_images=False):
    errors = []
    for true_val in range(10):
        counter = 0
        for predicted_val in range(10):
            counter += show_pairs(
                true_val,
                predicted_val,
                test_images,
                test_labels,
                predicted,
                show_images,
            )

        errors.append(counter)
    print("label with most errors:", max(range(len(errors)), key=lambda i: errors[i]))


def test_run(classifier, scale=False, show_results=False):
    train_features, train_target, test_features, test_labels = preprocess_data(scale)

    predicted = classifier_test(
        classifier,
        train_features,
        train_target,
        test_features,
        test_labels,
        show_results,
    )

    label_with_max_error(test_features, test_labels, predicted)

    show_metrics(test_labels, predicted)


def preprocess_data(scale=False):
    # The digits dataset
    digits = datasets.load_digits()

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data into a (samples, feature) matrix:
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    if scale:
        scaler = StandardScaler()
        data = scaler.fit_transform(data)

    # plot_random_samples(digits.images, digits.target)

    # Learn the digits on the first half of the data
    train_features, train_target = (
        data[0 : n_samples // 2],
        digits.target[0 : n_samples // 2],
    )

    # Now predict the value of the digit on the second half:
    test_features, test_labels = data[n_samples // 2 :], digits.target[n_samples // 2 :]

    return train_features, train_target, test_features, test_labels


def show_metrics(expected, predicted):
    print("Accuracy: " + str(metrics.accuracy_score(expected, predicted)))
    print(
        "Avg Precision: "
        + str(metrics.precision_score(expected, predicted, average="macro"))
    )
    print(
        "Avg Recall: " + str(metrics.recall_score(expected, predicted, average="macro"))
    )
    print(
        "Avg F1 Score: " + str(metrics.f1_score(expected, predicted, average="macro"))
    )


def main():

    # Create classifiers
    classifier_knn = KNeighborsClassifier()
    classifier_r = NearestCentroid()

    print("KNN, unscaled:")
    test_run(classifier_knn, scale=False)
    print("KNN, scaled:")
    test_run(classifier_knn, scale=True)
    print("Rocchio, unscaled:")
    test_run(classifier_r, scale=False)
    print("Rocchio, scaled:")
    test_run(classifier_r, scale=True)


if __name__ == "__main__":
    main()
