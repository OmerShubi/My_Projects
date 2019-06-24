from Data import Data
from sklearn import metrics
from AlgorithmRunner import AlgorithmRunner


if __name__ == '__main__':
    file_name = './movie_metadata.csv'

    data = Data(file_name)
    data.preprocess()
    kf = data.splitToFiveFolds()
    classifierKNN = AlgorithmRunner('KNN')
    classifierRocchio = AlgorithmRunner('Rocchio')

    fold = 0
    KNN_precision = 0
    KNN_recall = 0
    KNN_accuracy = 0
    Rocchio_precision = 0
    Rocchio_recall = 0
    Rocchio_accuracy = 0
    for train_index, test_index in kf.split(data.X):
        fold = fold + 1
        X_train, X_test = data.X[train_index], data.X[test_index]
        y_train, y_test = data.y[train_index], data.y[test_index]
        classifierKNN.fit(X_train, y_train)
        predictedKNN = classifierKNN.predict(X_test)

        classifierRocchio.fit(X_train, y_train)
        predictedRocchio = classifierRocchio.predict(X_test)
        expected = y_test
        # print("-------------   Fold", fold, "  --------------------")
        # print("Classification report for KNN classifier \n%s\n"
        #       % (metrics.classification_report(expected, predictedKNN)))
        #
        # print("Classification report for Rocchio classifier \n%s\n"
        #       % (metrics.classification_report(expected, predictedRocchio)))

        KNN_accuracy += metrics.accuracy_score(expected, predictedKNN)
        Rocchio_accuracy += metrics.accuracy_score(expected, predictedRocchio)

        KNN_precision += metrics.precision_score(expected, predictedKNN, average='binary')
        Rocchio_precision += metrics.precision_score(expected, predictedRocchio, average='binary')

        KNN_recall += metrics.recall_score(expected, predictedKNN, average='binary')
        Rocchio_recall += metrics.recall_score(expected, predictedRocchio, average='binary')

    print("Question 1:")
    print("KNN classifier {:.2f}, {:.2f}, {:.2f}".format(KNN_precision/5, KNN_recall/5, KNN_accuracy/5))
    print("Rocchio classifier: {:.2f}, {:.2f}, {:.2f}".format(Rocchio_precision/5, Rocchio_recall/5, Rocchio_accuracy/5))

    # print("Question 2:")
    # print("KNN classifier", KNN_improved_accuracy)
    # print("Rocchio classifier:", Rocchio_improved_accuracy)


