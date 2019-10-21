import math


class RocchioClassifier:
    def __init__(self, train_set):
        self.training_set = train_set
        self.class_centroids = {}
        self.training()

    def training(self):
        """
        Trains the Rocchio classifier (creates the centroids)
        :return: Nothing
        """
        class_size = {}
        for doc in self.training_set:
            doc_class = self.training_set[doc][-1]
            if doc_class not in self.class_centroids.keys():
                self.class_centroids[doc_class] = self.training_set[doc][0:-1]
                class_size[doc_class] = 1
            else:
                self.class_centroids[doc_class] = [self.class_centroids[doc_class][i] + self.training_set[doc][0:-1][i]
                                                   for i in range(len(self.training_set[doc]) - 1)]
                class_size[doc_class] += 1
        for c in self.class_centroids.keys():
            for i in range(len(self.class_centroids[c])):
                self.class_centroids[c][i] /= float(class_size[c])

    def predict(self, document, distance_method):
        """
        Predicts class of document
        Computes distance of doc from each centroid and returns the argmin
        :return:
        :param document: list of binary values
        :param distance_method: select whether to use euclidean or cosine distances
        :return: predicted class
        """
        distances = {}
        for centroid in self.class_centroids:
            if distance_method == 'euclidean':
                distances[centroid] = (self.eucildean_dist(self.class_centroids.get(centroid), document))
            elif distance_method == 'cosine':
                distances[centroid] = (self.cosine_similarity(self.class_centroids.get(centroid), document))
            else:
                print("wrong value. should be 'euclidean' or 'cosine'")

        if distance_method == 'euclidean':
            return min(distances, key=distances.get)  # Lower euclidean distance = more similar
        elif distance_method == 'cosine':
            return max(distances, key=distances.get)  # Higher cosine similarity = more similar
        else:
            return -1

    @staticmethod
    def eucildean_dist(list1, list2):
        """
        Calculates euclidean distance between two lists of doubles

        Assumes lists are of same length
        :param list1: list of doubles
        :param list2: list of doubles
        :return: euclidean distance, double
        """
        result = 0
        for i in range(len(list1)):
            result += (list1[i] - list2[i])**2
        return math.sqrt(result)

    @staticmethod
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
