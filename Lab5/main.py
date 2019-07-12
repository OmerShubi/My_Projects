from Lab5 import file_reader, rocchio_classifier
import math
import sys


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


def test_run(data_type, lower_and_remove_punctuation, remove_stop_words, distance_method):
    """
    Performs a test run, according to the given parameters
    :param data_type: Defines how to store the sentences, expects: 'boolean' / 'tf' / 'tfidf'
    :param lower_and_remove_punctuation: bool, if true turns all words to lower case and removes punctuation
    :param remove_stop_words: bool, if true removes all stop words
    :param distance_method: defines how to calculate distance, expects: 'euclidean' / 'cosine'
    :return: accuracy, the accuracy of the test run
    """
    file_name = "./dataset/amazon_cells_labelled_full.txt"
    train_file_name = "./dataset/amazon_cells_labelled_train.txt"
    test_file_name = "./dataset/amazon_cells_labelled_test.txt"

    data = file_reader.FileReader(file_name, lower_and_remove_punctuation, remove_stop_words)
    train_set, _ = data.build_set(data_type, train_file_name)
    test_set, _ = data.build_set(data_type, test_file_name)
    classifier = rocchio_classifier.RocchioClassifier(train_set)
    accuracy = calc_accuracy(test_set, classifier, distance_method)
    return accuracy


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


def retrieve(K, query, tfidf_docs, text_docs):
    distances = {}
    for doc in tfidf_docs:
        distances[doc] = cosine_similarity(query, tfidf_docs[doc])
    for k in range(K):
        key = max(distances, key=distances.get)
        print(str((k+1)) + ". " + key + " - " + text_docs[key] + "Score: " + str(distances[key]))
        distances.pop(key)


def lab5():
    print("Accuracy Results:")

    # boolean
    base_accuracy = test_run('boolean', False, False, 'euclidean')
    print("Bool:", base_accuracy)

    # tf
    tf_accuracy = test_run('tf', False, False, 'euclidean')
    print("tf:", tf_accuracy)

    # tfidf
    tfidf_accuracy = test_run('tfidf', False, False, 'euclidean')
    print("tfidf:", tfidf_accuracy)

    # tfidf with lower case and punctuation removal
    tfidf_lower_no_punctuation_accuracy = test_run('tfidf', True, False, 'euclidean')
    print("tfidf with lower case and punctuation removal:", tfidf_lower_no_punctuation_accuracy)

    # tfidf with lower case, punctuation removal and stopwords removal
    tfidf_cleaned_words_accuracy = test_run('tfidf', True, True, 'euclidean')
    print("tfidf with lower case, punctuation removal and stopwords removal:", tfidf_cleaned_words_accuracy)

    # tfidf with cosine similarity, lower case, punctuation removal and stopwords removal:
    tfidf_cleaned_words_cosine_accuracy = test_run('tfidf', True, True, 'cosine')
    print("tfidf with cosine similarity, lower case, punctuation removal and stopwords removal:",
          tfidf_cleaned_words_cosine_accuracy)

    debug = False
    if debug:
        print("\n DEBUG Full Accuracy Results:")

        # boolean
        print("Bool: ", base_accuracy)
        print("Diff to base: 0")
        print("Improvement from previous: -")

        # tf
        print("tf: ", tf_accuracy)
        print("Diff to base: ", tf_accuracy - base_accuracy)
        print("Improvement from previous: ", tf_accuracy - base_accuracy)

        # tfidf
        print("tfidf: ", tfidf_accuracy)
        print("Diff to base: ", tfidf_accuracy - base_accuracy)
        print("Improvement from previous: ", tfidf_accuracy - tf_accuracy)

        # tfidf with lower case and punctuation removal
        print("tfidf with lower case and punctuation removal: ", tfidf_lower_no_punctuation_accuracy)
        print("Diff to base: ", tfidf_lower_no_punctuation_accuracy - base_accuracy)
        print("Improvement from previous: ", tfidf_lower_no_punctuation_accuracy - tfidf_accuracy)

        # tfidf with lower case, punctuation removal and stopwords removal
        print("tfidf with lower case, punctuation removal and stopwords removal: ", tfidf_cleaned_words_accuracy)
        print("Diff to base: ", tfidf_cleaned_words_accuracy - base_accuracy)
        print("Improvement from previous: ", tfidf_cleaned_words_accuracy - tfidf_lower_no_punctuation_accuracy)

        # tfidf with cosine similarity, lower case, punctuation removal and stopwords removal:
        print("tfidf with cosine similarity, lower case, punctuation removal and stopwords removal: ",
              tfidf_cleaned_words_cosine_accuracy)
        print("Diff to base: ", tfidf_cleaned_words_cosine_accuracy - base_accuracy)
        print("Improvement from previous: ", tfidf_cleaned_words_cosine_accuracy - tfidf_cleaned_words_accuracy)


def lab6(K, query):
    file_name = "./dataset/amazon_cells_labelled_full.txt"
    data = file_reader.FileReader(file_name, True, True)
    tfidf_set, text_set = data.build_set('tfidf', file_name)
    parsed_query = data.parse_query(query)
    retrieve(K, parsed_query, tfidf_set, text_set)


if __name__ == '__main__':
    # uncomment to run lab 5
    # lab5()

    lab6(int(sys.argv[1]), sys.argv[2:][0])
