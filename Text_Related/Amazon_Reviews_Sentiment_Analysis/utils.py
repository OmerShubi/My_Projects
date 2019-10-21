import math

def calc_accuracy(test_set, classifier, distance_method):
    """
    Calculates a given classifier's accuracy on a test set, using the chosen distance method (euclidean / cosine)
    :param test_set: the test set, dictionary
    :param classifier: the trained rocchio classifier
    :param distance_method:
    :return:
    """
    correct = 0.0
    total = len(test_set.keys())
    for key in test_set:
        real = test_set[key][-1]
        predicted = classifier.predict(test_set[key][0:-1], distance_method)
        if real == predicted:
            correct += 1.0
    return correct/total


def cosine_similarity(list1, list2):
    """
    Calculates cosine similarity between two lists of doubles

    Assumes lists are of same length
    :param list1: list of doubles
    :param list2: list of doubles
    :return: cosine similarity, double
    """
    list1_norm = 0
    list2_norm = 0
    result = 0

    for i in range(len(list1)):
        list1_norm += list1[i]**2
        list2_norm += list2[i]**2
        result += list1[i]*list2[i]

    list1_norm = math.sqrt(list1_norm)
    list2_norm = math.sqrt(list2_norm)

    return result/(list1_norm*list2_norm)