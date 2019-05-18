# general imports
import random
import itertools
from pprint import pprint
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  # data splitter
from sklearn.linear_model import LogisticRegression
import re

# project supplied imports
from submission_specs.SubmissionSpec12 import SubmissionSpec12


class Submission(SubmissionSpec12):
    """ a contrived poorely performing solution for question one of this Maman """

    def __init__(self) -> None:
        super().__init__()
        self.tag_set = 'ADJ ADP PUNCT ADV AUX SYM INTJ CCONJ X NOUN DET PROPN NUM VERB PART PRON SCONJ'.split()
        self.emission = {}
        self.transitions = {}

    def _estimate_emission_probabilites(self, annotated_sentences):
        # print('ANNOTATED SENTENCES:\n', annotated_sentences)
        # print(type(annotated_sentences[5][0])) [ [ () ] ]
        pass

    def _estimate_transition_probabilites(self, annotated_sentences):
        words = [p[0] for s in annotated_sentences for p in s]
        # for s in annotated_sentences:
        # print(len(words.count()))

        pass

    def train(self, annotated_sentences):
        """ trains the HMM model (computes the probability distributions) """
        print('training function received {} annotated sentences as training data'.format(len(annotated_sentences)))
        self._estimate_emission_probabilites(annotated_sentences)
        self._estimate_transition_probabilites(annotated_sentences)
        return self

    def predict(self, sentence):
        prediction = [random.choice(self.tag_set) for segment in sentence]
        assert (len(prediction) == len(sentence))
        return prediction
