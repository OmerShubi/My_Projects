# Reads the csv file and save data to memory

class Data:
    def preprocess(self):
        pass
        # TODO with file...
        # TODO Preprocess function member - save all Attributes excluding content_Rating, movie_imdb_link, plot_keywords
        # TODO discard entries with any NaN value
        # TODO Handle duplicate movie_tile values
        # TODO handle Categorical Attributes - turn to dummy variables
        # TODO Normalize - (x-mean)/SD - all variables except Categorical Attributes (dummy variables)


    def splitToFiveFolds(self):
        pass
        # TODO split to 5-folds using sklearn
        #sklearn.model_selection.KFold(n_splits=5, shuffle=False, random_state=1)
