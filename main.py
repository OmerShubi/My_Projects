import file_reader
import rocchio_classifier


def calc_accuracy(test_set, classifier, predict_method):
    correct = 0.0
    total = len(test_set.keys())
    for key in test_set:
        real = test_set[key][-1]
        predicted = classifier.predict(test_set[key][0:-1], predict_method)
        if real == predicted:
            correct += 1.0
    return correct/total


def test_run(data_type, lower_and_remove_punctuation, remove_stop_words,
             distance_method):
    file_name = "./dataset/amazon_cells_labelled_full.txt"  # TODO change to command line?
    train_file_name = "./dataset/amazon_cells_labelled_train.txt"
    test_file_name = "./dataset/amazon_cells_labelled_test.txt"

    data = file_reader.FileReader(file_name, lower_and_remove_punctuation, remove_stop_words)
    train_set, _ = data.build_set(data_type, train_file_name)
    test_set, _ = data.build_set(data_type, test_file_name)
    classifier = rocchio_classifier.RocchioClassifier(train_set)
    accuracy = calc_accuracy(test_set, classifier, distance_method)
    return accuracy


if __name__ == '__main__':

    print("Accuracy Results:\n")

    # boolean
    base_accuracy = test_run('boolean', False, False, 'euclidean')
    print("Bool: ", base_accuracy)
    print("Diff to base: 0")
    print("Improvement from previous: -")

    # tf
    tf_accuracy = test_run('tf', False, False, 'euclidean')

    print("tf: ", tf_accuracy)
    print("Diff to base: ", tf_accuracy-base_accuracy)
    print("Improvement from previous: ", tf_accuracy-base_accuracy)

    # tfidf
    tfidf_accuracy = test_run('tfidf', False, False, 'euclidean')

    print("tfidf: ", tfidf_accuracy)
    print("Diff to base: ", tfidf_accuracy-base_accuracy)
    print("Improvement from previous: ", tfidf_accuracy-tf_accuracy)

    # tfidf with lower case and punctuation removal
    tfidf_lower_no_punctuation_accuracy = test_run('tfidf', True, False, 'euclidean')

    print("tfidf with lower case and punctuation removal: ", tfidf_lower_no_punctuation_accuracy)
    print("Diff to base: ", tfidf_lower_no_punctuation_accuracy-base_accuracy)
    print("Improvement from previous: ", tfidf_lower_no_punctuation_accuracy-tfidf_accuracy)

    # tfidf with lower case, punctuation removal and stopwords removal
    tfidf_cleaned_words_accuracy = test_run('tfidf', True, True, 'euclidean')

    print("tfidf with lower case, punctuation removal and stopwords removal: ", tfidf_cleaned_words_accuracy)
    print("Diff to base: ", tfidf_cleaned_words_accuracy-base_accuracy)
    print("Improvement from previous: ", tfidf_cleaned_words_accuracy-tfidf_lower_no_punctuation_accuracy)

    # tfidf with cosine similarity, lower case, punctuation removal and stopwords removal:
    tfidf_cleaned_words_cosine_accuracy = test_run('tfidf', True, True, 'cosine')

    print("tfidf with cosine similarity, lower case, punctuation removal and stopwords removal: ",
          tfidf_cleaned_words_cosine_accuracy)
    print("Diff to base: ", tfidf_cleaned_words_cosine_accuracy-base_accuracy)
    print("Improvement from previous: ", tfidf_cleaned_words_cosine_accuracy-tfidf_cleaned_words_accuracy)

