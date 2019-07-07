import random
import matplotlib.pyplot as plt
from sklearn import metrics


def plot_random_samples(images, labels):
    """
    plot 6 random items from the dataset,
    presented in a grid of 2(rows)*3(columns)
    images’ matrices are also printed
    :param images:
    :param labels:
    :return:
    """
    n_samples = len(images)
    all_indexes = list(range(n_samples))
    selected_indexes = random.sample(all_indexes, k=6)
    k = 1
    for index in selected_indexes:
        plt.subplot(2, 4, k)
        k += 1
        plt.axis("off")
        plt.imshow(images[index], cmap="binary")
        plt.title("Random: %i" % labels[index])
        print("this is how it would look like in a matrix: " + str(labels[index]))
        print(images[index])
    plt.show()
    plt.close()


def classifier_test(classifier, train, train_labels, test, test_labels):
    # Learn the digits on the first half of the data
    classifier.fit(train, train_labels)
    # Now predict the value of the digit on the second half:
    expected = test_labels
    predicted = classifier.predict(test)

    print(
        "Classification report for classifier %s:\n%s\n"
        % (classifier, metrics.classification_report(expected, predicted))
    )
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
    print("Accuracy: " + str(metrics.accuracy_score(expected, predicted)))

    return predicted
