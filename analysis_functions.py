import random
import matplotlib.pyplot as plt


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
