import sklearn
import pandas as pd
import numpy as np

# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        self.file = file_name # path to file
        self.data = pd.array

    def preprocess(self):
        # import csv
        scaler = sklearn.preprocessing.StandardScaler()

        self.data = pd.read_csv(self.file, delimiter=',')

        # save all Attributes excluding content_Rating, movie_imdb_link, plot_keywords
        self.data.drop(columns=['content_rating', 'movie_imdb_link', 'plot_keywords'], inplace=True)

        # discard entries with any NaN value
        self.data.dropna(inplace=True)

        #  Handle duplicate movie_tile values
        self.data.drop_duplicates(subset='movie_title', inplace=True)

        #  handle Categorical Attributes - turn to dummy variables
        self.data = pd.get_dummies(self.data)


        # self.X_train, self.X_test, self.y_train, self.y_test = \
        # train_test_split_split(X, y, random_state=0)
        # TODO Normalize - (x-mean)/SD - all variables except Categorical Attributes (dummy variables) sklearn.preprocessing.StandardScaler

    def splitToFiveFolds(self):
        pass
        # TODO split to 5-folds using sklearn
        #sklearn.model_selection.KFold(n_splits=5, shuffle=False, random_state=1)
