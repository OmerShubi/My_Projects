import file_reader
import rocchio_classifier
import math

def calc_accuracy(test_set, classifier, predict_method):
    correct = 0.0
    total = len(test_set.keys())
    for key in test_set:
        real = test_set[key][-1]
        predicted = classifier.predict(test_set[key][0:-1], predict_method)
        if real == predicted:
            correct += 1.0
    return correct/total


if __name__ == '__main__':

    file_name = "./dataset/amazon_cells_labelled_full.txt"
    train_file_name = "./dataset/amazon_cells_labelled_train.txt"
    test_file_name = "./dataset/amazon_cells_labelled_test.txt"

    print("Accuracy Results:\n")

    data_0_1_2 = file_reader.FileReader(file_name, lower_and_remove_punctuation=False, remove_stop_words=False)

    # boolean
    train_set_bool, _ = data_0_1_2.build_set("boolean", train_file_name)
    test_set_bool, _ = data_0_1_2.build_set("boolean", test_file_name)
    classifier_bool = rocchio_classifier.RocchioClassifier(train_set_bool)
    print("Bool: ", calc_accuracy(test_set_bool, classifier_bool, 'euclidean distance'))

    # tf
    train_set_tf, _ = data_0_1_2.build_set("tf", train_file_name)
    test_set_tf, _ = data_0_1_2.build_set("tf", test_file_name)
    classifier_tf = rocchio_classifier.RocchioClassifier(train_set_tf)
    print("tf: ", calc_accuracy(test_set_tf, classifier_tf, 'euclidean distance'))

    # tfidf
    train_set_tfidf, _ = data_0_1_2.build_set("tfidf", train_file_name)
    test_set_tfidf, _ = data_0_1_2.build_set("tfidf", test_file_name)
    classifier_tfidf = rocchio_classifier.RocchioClassifier(train_set_tfidf)
    print("tfidf: ", calc_accuracy(test_set_tfidf, classifier_tfidf, 'euclidean distance'))

    # tfidf with lower case and punctuation removal
    data_3 = file_reader.FileReader(file_name, lower_and_remove_punctuation=True, remove_stop_words=False)
    train_set_tfidf, _ = data_3.build_set("tfidf", train_file_name)
    test_set_tfidf, _ = data_3.build_set("tfidf", test_file_name)
    classifier_tfidf = rocchio_classifier.RocchioClassifier(train_set_tfidf)
    print("tfidf with lower case and punctuation removal: ",
          calc_accuracy(test_set_tfidf, classifier_tfidf, 'euclidean distance'))

    data_4_5 = file_reader.FileReader(file_name, lower_and_remove_punctuation=True, remove_stop_words=True)

    # tfidf with lower case, punctuation removal and stopwords removal
    train_set_tfidf, _ = data_4_5.build_set("tfidf", train_file_name)
    test_set_tfidf, _ = data_4_5.build_set("tfidf", test_file_name)
    classifier_tfidf = rocchio_classifier.RocchioClassifier(train_set_tfidf)

    print("tfidf with lower case, punctuation removal and stopwords removal: ",
          calc_accuracy(test_set_tfidf, classifier_tfidf, 'euclidean distance'))

    # tfidf with cosine similarity, lower case, punctuation removal and stopwords removal:
    print("tfidf with cosine similarity, lower case, punctuation removal and stopwords removal: ",
          calc_accuracy(test_set_tfidf, classifier_tfidf, 'cosine similarity'))

