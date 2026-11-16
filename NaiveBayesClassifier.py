"""
Author: Eda Memik
Starting Date: 3/3/26

An implementation of a Naive Bayes Classifier
"""

import math  # math.log()
import os
import pickle

import re

"""
The name of positive dictionary cache file
"""
POSITIVE_DATA = "pos.dat"

"""
The name of negative dictionary cache file
"""
NEGATIVE_DATA = "neg.dat"

"""
The file name prefix for negative reviews
"""
NEGATIVE_FILE_PREFIX = "movies-1"

"""
The file name prefix for positive reviews
"""
POSITIVE_FILE_PREFIX = "movies-5"


class BayesClassifier:
    """A simple BayesClassifier implementation"""

    """
    A dictionary of frequencies of positive words
    """
    pos_freqs: dict[str, int]

    """
    A dictionary of frequencies of negative words
    """
    neg_freqs: dict[str, int]

    def __init__(self):
        """Constructor for the Naive Bayes Sentiment Classifier"""
        self.pos_freqs = {}
        self.neg_freqs = {}

    def setup(self, training_data: str):
        """
        If a cache of a trained classifier is stored in the current folder,
          it is loaded from that file;
        otherwise the system will proceed through training.

        Once setup, the classifier is ready to classify input text.

        Arguments:
            training_data: the local folder name with files to train on
        """
        if os.path.isfile(POSITIVE_DATA) and os.path.isfile(NEGATIVE_DATA):
            print("Data files found - loading to use cached values...")
            self.pos_freqs = self.load_dict(POSITIVE_DATA)
            self.neg_freqs = self.load_dict(NEGATIVE_DATA)
        else:
            print("Data files not found - running training...")
            self.train(training_data)
            self.save_dict(self.pos_freqs, POSITIVE_DATA)
            self.save_dict(self.neg_freqs, NEGATIVE_DATA)

    def save_dict(self, d: dict[str, int], filepath: str):
        """Pickle a given dictionary to a file with the given name.

        Args:
            d: A dictionary to pickle.
            filepath: The relative path to file to save.
        """
        print(f"Dictionary saved to file: {filepath}")
        with open(filepath, "wb") as f:
            pickle.Pickler(f).dump(d)

    def load_dict(self, filepath: str) -> dict[str, int]:
        """Load a pickled dictionary stored in given file.

        Args:
            filepath: The relative path to file to load.

        Returns:
            A dictionary stored in given file.
        """
        print(f"Loading dictionary from file: {filepath}")
        with open(filepath, "rb") as f:
            return pickle.Unpickler(f).load()  # type: ignore

    def load_file(self, filepath: str) -> str:
        """Load text of given file.

        Args:
            filepath: The relative path to file to load.

        Returns:
            The text of the given file.
        """
        with open(filepath, "r", encoding="utf8") as f:
            return f.read()




    def update_dict(self, words: list[str], freqs: dict[str, int]):
        """Update a given (word -> frequency) dictionary with given words list

        That is, increment the count of each word in words in the dictionary
        If any word in words is not currently in the dictionary,
          it is added with an initial count of 1

        Args:
            words: The list of tokens to update frequencies of
            freqs: A dictionary of frequencies to update
        """
        #Implement me!

        for word in words:
            if word in freqs:
                freqs[word] = freqs.get(word, 0) + 1
            else:
                freqs[word] = 1

        # Hint: don't overthink this function

        return






    def tokenize(self, text: str) -> list[str]:
        """Split the given text into a list of the individual tokens in order

        Specifically, tokens consist of lowercase letters, digits, and the symbols ', -, and _
          such that each word in the text is a distinct string in the output list

        Words are considered to be separated by _any_ non-tokenized characters

        For example,
        tokenize('Hello World 1234-5678') -> ['hello', 'world', '1234-5678']

        Args:
            text: The text to tokenize

        Returns:
            The tokens of given text in order
        """

        # TODO: Implement me!



        '''new_text1 = text.lower()
        new_text2 = new_text1.replace(".", "  ")
        new_text3 = new_text2.replace("?", "  ")
        new_text4 = new_text3.replace("!", "  ")
        new_text5 = new_text4.replace("&", "  ")
        new_text6 = new_text5.replace('"', "  ")
        new_text7 = new_text6.replace('@', "  ")
        new_text8 = new_text7.replace('^', "  ")
        new_text9 = new_text8.replace('$', "  ")
        new_text10 = new_text8.replace('(', "  ")'''

        #regular expresson

        new_text1 = text.lower()

        lst = []
        str = ""

        for letter in new_text1:
            match = re.match(r"[a-z0-9]", letter)

            if match != None or letter in ["'", "_", "-"]:
                str = str + letter

            if (match == None) and (str != "") and (letter not in ["'", "_", "-"]):
                lst.append(str)
                str = ""

        if str != "":
            lst.append(str)




        #new_text = new_text4.split()
        '''new_text = re.split(r'\s+', new_text6)
        while "" in new_text:
            new_text.remove("")'''




        '''new_text1 = text.lower()



        if '"' in new_text4:
            new_text = re.split(r'[", \n]', new_text4)
        else:
            new_text = new_text4.split()'''

        return lst





    def train(self, training_data: str):
        """Train the Naive Bayes Sentiment Classifier

        Specifically, generate the `pos_freq/neg_freq` dictionaries
          with frequencies of words in corresponding positive/negative reviews

        Arguments:
            training_data: the local folder name with files to train on
        """
        # get the list of file names from the training data directory
        # os.walk returns a generator, of which we only need the first value
        _, _, files = next(os.walk(training_data), (None, None, []))
        if not files:
            raise RuntimeError(f"Couldn't find path {training_data}")

        # TODO: Finish implementing me!
#C:\Users\MadeA\Desktop\CS150\Archive-1\train_test1\movies-1-1.txt

        num_files_looked = 0
        dict1 = {}
        dict5 = {}

        #dir_full = os.path.dirname(os.path.abspath(__file__))
        #filepath = os.path.join(dir_full, training_data, filename)
        #filepath = os.path.join('Users', 'MadeA', 'Desktop','CS150', 'Archive-1', 'train_test1', filename)
        for filename in files:
            filepath = os.path.join(training_data, filename)
            current_file = self.load_file(filepath)
            tokens = self.tokenize(current_file)

            num_files_looked += 1
            if (num_files_looked % 500) == 0:
                print(f"{num_files_looked} files looked at")

            if NEGATIVE_FILE_PREFIX in filename:
                self.update_dict(tokens, dict1)
            elif POSITIVE_FILE_PREFIX in filename:
                self.update_dict(tokens, dict5)

        self.pos_freqs = dict5
        self.neg_freqs = dict1
        print(f"{num_files_looked} files looked at")


#{'one': 1, 'two': 2, 'three': 1, "'''comment": 1, "test'''": 1, 'lines': 1}
#{'one': 1, 'two': 1, 'three': 1, "'''comment": 1, "test'''\ntwo lines": 1}

        #self.save_dict(dict1, os.path.dirname(os.path.abspath(__file__)))


        return

    def classify(self, text: str) -> str:
        """Classify the given text as negative or positive

        This is done by calculating the most likely document class
          as described in the lab writeup
          and using the pos_freqs and neg_freqs dictionaries associated with this classifier

        If either dictionary is empty (i.e., this classifier is untrained)
          then the behavior of this function is unspecified (anything can happen)

        Args:
            text: The text to classify

        Returns:
            The classification string, either 'positive' or 'negative'
        """

        len_pos = len(self.pos_freqs)
        len_neg = len(self.neg_freqs)
        prob_pos_in = 0
        prob_neg_in = 0

        lst_total_words_pos = list(self.pos_freqs.values())
        num_words_pos = sum(lst_total_words_pos)

        lst_total_words_neg = list(self.neg_freqs.values())
        num_words_neg = sum(lst_total_words_neg)



        txt_tokens = self.tokenize(text)

        for word in txt_tokens:
            #prob_pos_in = sum(math.log((self.pos_freqs.get(word, 0) + 1)/num_words_pos))
            prob_pos_in = math.log((self.pos_freqs.get(word, 0) + 1) / num_words_pos) + prob_pos_in
            prob_neg_in = math.log((self.neg_freqs.get(word, 0) + 1)/num_words_neg) + prob_neg_in

        #    prob_neg_in = sum(math.log((self.neg_freqs.get(word, 0) + 1)/num_words_neg))


        if prob_pos_in < prob_neg_in:
            return 'negative'
        elif prob_pos_in > prob_neg_in:
            return 'positive'
        else:
            return 'Wether or not the statement is positive or negative, cannot be ascertained'
#sum(log ((positive_count_of_word + 1)/total_positive_word_count))



        return ''
