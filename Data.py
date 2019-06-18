from sklearn import preprocessing
import numpy as np

# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        self.file = file_name

    def preprocess(self):
        doc_set = {}
        index = 0
        with open(self.file, 'r') as reader:
            for line in reader:
                vec = 26*[0,]
                for word in line.split("\t")[0].split():
                    word = self.pre_process_word(word)
                    if word == '':
                        continue
                    vec[self.words[word]] = 1
                doc_class = line.split("\t")[1].rstrip()
                vec.append(doc_class)
                doc_set['doc'+str(index)] = vec
                index += 1
        return doc_set
        pass
        # TODO with file...
        # TODO Preprocess function member - save all Attributes excluding content_Rating, movie_imdb_link, plot_keywords
        # TODO discard entries with any NaN value
        # TODO Handle duplicate movie_tile values
        # TODO handle Categorical Attributes - turn to dummy variables sklearn.preprocessing.OneHotEncoder
        # TODO Normalize - (x-mean)/SD - all variables except Categorical Attributes (dummy variables) sklearn.preprocessing.StandardScaler

    def splitToFiveFolds(self):
        pass
        # TODO split to 5-folds using sklearn
        #sklearn.model_selection.KFold(n_splits=5, shuffle=False, random_state=1)
