import sys

from file_reader import FileReader
from rocchio_classifier import RocchioClassifier
from utils import cosine_similarity, calc_accuracy


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

    data = FileReader(file_name, lower_and_remove_punctuation, remove_stop_words)
    train_set, _ = data.build_set(data_type, train_file_name)
    test_set, _ = data.build_set(data_type, test_file_name)
    classifier = RocchioClassifier(train_set)
    accuracy = calc_accuracy(test_set, classifier, distance_method)
    return accuracy


def retrieve(K, query, tfidf_docs, text_docs):
    distances = {}
    for doc in tfidf_docs:
        distances[doc] = cosine_similarity(query, tfidf_docs[doc])
    for k in range(K):
        key = max(distances, key=distances.get)
        print(str((k+1)) + ". " + key + " - " + text_docs[key] + " Score: " + str(distances[key]))
        distances.pop(key)


def Rocchio_in_action_multiple_configurations(full_results=False):
    """
    Checks accuracy of the Rocchio Classifier, with different configuration options
    :param full_results: displays more in-depth results
    :return:
    """
    print("Accuracy Results:")

    # boolean
    base_accuracy = test_run(data_type='boolean', lower_and_remove_punctuation=False,
                             remove_stop_words=False, distance_method='euclidean')
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

    if full_results:
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


def retrieve_best_k_related_reviews(K, query):
    """
    Utilizing the Rocchio Classifier,
    finds and displays the k most relevant reviews to a given query, and their score.
    :param K: int, number of related documents desired
    :param query: string, the query to check the reviews against.
    :return:
    """
    file_name = "./dataset/amazon_cells_labelled_full.txt"
    data = FileReader(file_name, True, True)
    tfidf_set, text_set = data.build_set('tfidf', file_name)
    parsed_query = data.parse_query(query)
    retrieve(K, parsed_query, tfidf_set, text_set)


if __name__ == '__main__':
    # Run with 'python -m main 5 "camera"' if run into issues with imports

    Rocchio_in_action_multiple_configurations(full_results=True)

    retrieve_best_k_related_reviews(5, "samsung phone")  # Hardcoded version

    # retrieve_best_k_related_reviews(int(sys.argv[1]), sys.argv[2:][0])  # Command line version
