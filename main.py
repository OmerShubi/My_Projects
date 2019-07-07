# Original code was provided by:
# Original author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>

import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from analysis_functions import *


def main():

    # The digits dataset
    digits = datasets.load_digits()

    print(digits.data.shape)
    # The data that we are interested in is made of 8x8 images of digits, let's
    # have a look at the first 8 images, stored in the `images` attribute of the
    # dataset.  If we were working from image files, we could load them using
    # matplotlib.pyplot.imread.  Note that each image must have the same size. For these
    # images, we know which digit they represent: it is given in the 'target' of
    # the dataset.
    plot_random_samples(digits.images, digits.target)

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data into a (samples, feature) matrix:
    print(digits.images.shape)

    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    # Create a KNN classifier
    classifierKNN = KNeighborsClassifier()
    classifierRocchio = NearestCentroid()

    # Learn the digits on the first half of the data
    train_features, train_target = (
        data[0 : n_samples // 2],
        digits.target[0 : n_samples // 2],
    )

    # Now predict the value of the digit on the second half:
    test_features, test_labels = data[n_samples // 2 :], digits.target[n_samples // 2 :]

    predicted_KNN = classifier_test(
        classifierKNN, train_features, train_target, test_features, test_labels
    )

    predicted_Rocchio = classifier_test(
        classifierRocchio, train_features, train_target, test_features, test_labels
    )

    # plotting the errors of the model
    images_and_predictions = list(zip(digits.images[n_samples // 2 :], predicted_KNN))
    for index, (image, prediction) in enumerate(images_and_predictions[:]):
        if test_labels[index] == predicted_KNN[index]:
            continue
        plt.imshow(image, cmap="binary")
        plt.title(
            "KNN Prediction: %i" % prediction + " True Label: %i" % test_labels[index]
        )
        plt.show()

    images_and_predictions = list(
        zip(digits.images[n_samples // 2 :], predicted_Rocchio)
    )
    for index, (image, prediction) in enumerate(images_and_predictions[:]):
        if test_labels[index] == predicted_Rocchio[index]:
            continue
        plt.imshow(image, cmap="binary")
        plt.title(
            "Rocchio Prediction: %i" % prediction
            + " True Label: %i" % test_labels[index]
        )
        plt.show()


if __name__ == "__main__":
    main()
