import math


class FileReader:

    def __init__(self, input_file, lower_and_remove_punctuation, remove_stop_words):
        self.file = input_file
        self.words = {}
        self.df = {}
        self.stop_words = []
        self.number_of_docs = 0
        self.lower_and_remove_punctuation = lower_and_remove_punctuation
        self.remove_stop_words = remove_stop_words
        self.create_stop_words_list()
        self.create_words_bank()
        self.inv_words = {v: k for k, v in self.words.items()}

    def build_set(self, vector_type, file_to_vector):
        if vector_type == 'boolean':
            return self.build_set_boolean(file_to_vector)
        if vector_type == 'tf':
            return self.build_set_tf(file_to_vector)
        if vector_type == 'tfidf':
            return self.build_set_tfidf(file_to_vector)
        else:
            print("vector_type should be 'boolean' / 'tf' / 'tfidf'")

    def create_stop_words_list(self):
        with open('./stop_words.txt') as stop_words_file:
            for stop_word in stop_words_file:
                self.stop_words.append(stop_word.rstrip())

    def pre_process_word(self, word):
        """
        Preprocesses a word by turning it to lower case,
        removes some punctuation and returns the word or
        empty string if it is a stop word
        :param word: string
        :return: updated word - string
        """
        if self.lower_and_remove_punctuation:
            # Changes word to lower case
            word = word.lower()

            # Removes punctuations
            word = word.rstrip('.,?!:')

        if self.remove_stop_words:
            # returns empty string if word is a stop word
            if word in self.stop_words:
                return ''

        return word

    def create_words_bank(self):
        index = 0
        with open(self.file, 'r') as reader:  # open the file "file"
            for line in reader:  # for each line in file
                seen_in_this_line = []
                for word in line.split("\t")[0].split(): # for each word in the line
                    word = self.pre_process_word(word)
                    if word == '':
                        continue
                    if word not in self.df:
                        self.df[word] = 1  # document frequency
                        seen_in_this_line.append(word)
                    if word not in seen_in_this_line:
                        self.df[word] += 1
                        seen_in_this_line.append(word)
                    if word not in self.words.keys():  # if the word doesnt already exists in the words dictionary
                        self.words[word] = index  # add it
                        index += 1
                self.number_of_docs += 1

    def build_set_boolean(self, file_to_vector):
        """
        Builds the data vector using boolean format
        :param file_to_vector: the file to be processed
        :return: the file in vector form, using boolean format
        """
        doc_set = {}
        reg_representation = {}
        index = 0
        with open(file_to_vector, 'r') as reader:
            for line in reader:
                vec = len(self.words)*[0, ]
                for word in line.split("\t")[0].split():
                    word = self.pre_process_word(word)
                    if word == '':
                        continue
                    vec[self.words[word]] = 1
                doc_class = line.split("\t")[1].rstrip()
                vec.append(doc_class)
                doc_set['doc'+str(index)] = vec
                reg_representation['doc' + str(index)] = line.split("\t")[0]
                index += 1
        return doc_set, reg_representation

    def build_set_tf(self, file_to_vector):
        """
        Builds the data vector using tf format
        :param file_to_vector: the file to be processed
        :return: the file in vector form, using tf format
        """
        doc_set = {}
        reg_representation = {}
        index = 0
        with open(file_to_vector, 'r') as reader:
            for line in reader:
                vec = len(self.words)*[0,]
                for word in line.split("\t")[0].split():
                    word = self.pre_process_word(word)
                    if word == '':
                        continue
                    vec[self.words[word]] += 1
                # After iterating over all words we now have the tf and can store words in tf format
                for word in range(len(vec)):
                    if vec[word] == 0:
                        continue
                    else:
                        vec[word] = 1 + math.log(vec[word], 10)
                doc_class = line.split("\t")[1].rstrip()
                vec.append(doc_class)
                doc_set['doc'+str(index)] = vec
                reg_representation['doc' + str(index)] = line.split("\t")[0]
                index += 1
        return doc_set, reg_representation

    def build_set_tfidf(self, file_to_vector):
        """
        Builds the data vector using tfidf format
        :param file_to_vector: the file to be processed
        :return: the file in vector form, using tfidf format
        """
        doc_set = {}
        reg_representation = {}
        index = 0
        with open(file_to_vector, 'r') as reader:
            for line in reader:
                vec = len(self.words)*[0,]
                for word in line.split("\t")[0].split():
                    word = self.pre_process_word(word)
                    if word == '':
                        continue
                    vec[self.words[word]] += 1
                # After iterating over all words we now have the tf and can store words in tfidf format
                for word in self.words.keys():
                    if vec[self.words[word]] == 0:
                        continue
                    else:
                        vec[self.words[word]] = vec[self.words[word]]*math.log((self.number_of_docs/self.df[word]), 10)
                doc_class = line.split("\t")[1].rstrip()
                vec.append(doc_class)
                doc_set['doc'+str(index)] = vec
                reg_representation['doc' + str(index)] = line.split("\t")[0]
                index += 1
        return doc_set, reg_representation

    def parse_query(self, query):
        """
        Builds the data vector using tfidf format
        :param file_to_vector: the file to be processed
        :return: the file in vector form, using tfidf format
        """
        doc_set = {}
        reg_representation = {}
        index = 0
        vec = len(self.words) * [0, ]
        for word in query.split("\t")[0].split():
            word = self.pre_process_word(word)
            if word == '':
                continue
            if word in self.words:
                vec[self.words[word]] += 1
        # After iterating over all words we now have the tf and can store words in tfidf format
        for word in self.words.keys():
            if vec[self.words[word]] == 0:
                continue
            else:
                vec[self.words[word]] = vec[self.words[word]] * math.log((self.number_of_docs / self.df[word]), 10)
        doc_set['doc' + str(index)] = vec
        reg_representation['doc' + str(index)] = query.split("\t")[0]
        index += 1
        return vec
