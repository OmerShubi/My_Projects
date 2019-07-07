# Original code was provided by:
# Original author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>

import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid


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
    images_and_labels = list(zip(digits.images, digits.target))
    for index, (image, label) in enumerate(images_and_labels[:8]):
        plt.subplot(2, 4, index + 1)
        plt.axis("off")
        plt.imshow(image, cmap="binary")
        plt.title("Training: %i" % label)
        print("this is how it would look like in a matrix: " + str(label))
        print(digits.images[index])
    plt.show()
    plt.close()

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data into a (samples, feature) matrix:
    print(digits.images.shape)

    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    # Create a classifier
    classifier = KNeighborsClassifier()
    # Learn the digits on the first half of the data
    classifier.fit(data[0 : n_samples // 2], digits.target[0 : n_samples // 2])
    # Now predict the value of the digit on the second half:
    expected = digits.target[n_samples // 2 :]
    predicted = classifier.predict(data[n_samples // 2 :])

    print(
        "Classification report for classifier %s:\n%s\n"
        % (classifier, metrics.classification_report(expected, predicted))
    )
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
    print("Accuracy: " + str(metrics.accuracy_score(expected, predicted)))

    # plotting the errors of the model
    images_and_predictions = list(zip(digits.images[n_samples // 2 :], predicted))
    for index, (image, prediction) in enumerate(images_and_predictions[:]):
        if expected[index] == predicted[index]:
            continue
        plt.imshow(image, cmap="binary")
        plt.title("Prediction: %i" % prediction + " True Label: %i" % expected[index])
        plt.show()


if __name__ == "__main__":
    main()
