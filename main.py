from Data import Data
from AlgorithmRunner import AlgorithmRunner


if __name__ == '__main__':

    file_name = './movie_metadata.csv'

    data = Data(file_name)
    data.preprocess()

    classifierKNN = AlgorithmRunner('KNN')
    classifierRocchio = AlgorithmRunner('Rocchio')

    classifierRocchio.cross_val_score(data)
    classifierKNN.cross_val_score(data)

    print("Question 1:")
    print("KNN classifier {:.2f}, {:.2f}, {:.2f}".format(classifierKNN.precision,
                                                         classifierKNN.recall, classifierKNN.accuracy))
    print("Rocchio classifier: {:.2f}, {:.2f}, {:.2f}".format(classifierRocchio.precision, classifierRocchio.recall,
                                                              classifierRocchio.accuracy))

    # print("Question 2:")
    # print("KNN classifier", KNN_improved_accuracy)
    # print("Rocchio classifier:", Rocchio_improved_accuracy)
