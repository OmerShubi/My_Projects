from sklearn import *
import pandas as pd
import sklearn_pandas

import numpy as np

# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        self.file = file_name # path to file
        self.data = pd.DataFrame

    def preprocess(self):
        # import csv

        self.data = pd.read_csv(self.file, delimiter=',')

        # save all Attributes excluding content_Rating, movie_imdb_link, plot_keywords
        self.data.drop(columns=['content_rating', 'movie_imdb_link', 'plot_keywords'], inplace=True)

        # discard entries with any NaN value
        self.data.dropna(inplace=True)

        #  Handle duplicate movie_tile values
        self.data.drop_duplicates(subset='movie_title', keep='first', inplace=True)

        numerical_columns = self.data.select_dtypes(include='number').columns
        categorical_columns = self.data.select_dtypes(exclude='number').columns

        preprocessor = compose.ColumnTransformer(transformers=[('num',preprocessing.StandardScaler(), numerical_columns),
                                                        ('cat', preprocessing.OneHotEncoder(), categorical_columns)])

        cleaned_data = preprocessor.fit_transform(self.data)
        print(type(cleaned_data))





        # self.X_train, self.X_test, self.y_train, self.y_test = \
        # train_test_split_split(X, y, random_state=0)

    def splitToFiveFolds(self):
                model_selection.KFold(n_splits=5, shuffle=False, random_state=1)
