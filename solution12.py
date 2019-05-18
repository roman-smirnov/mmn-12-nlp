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
import json


class Submission(SubmissionSpec12):
    """ a contrived poorely performing solution for question one of this Maman """

    def __init__(self) -> None:
        super().__init__()
        self.tag_set = 'ADJ ADP PUNCT ADV AUX SYM INTJ CCONJ X NOUN DET PROPN NUM VERB PART PRON SCONJ'.split()
        self.emission = {}
        self.transitions = {}

    def _estimate_emission_probabilites(self, annotated_sentences):
        types_count = {}
        for sentence in annotated_sentences:
            for couple in sentence:
                word = couple[0]
                type = couple[1]

                if type not in self.emission:
                    self.emission[type] = {}
                    types_count[type] = 0
                types_count[type] += 1

                if word in self.emission[type]:
                    self.emission[type][word] += 1
                else:
                    self.emission[type][word] = 1

        for type2 in self.emission:
            for word2 in self.emission[type2]:
                self.emission[type2][word2] = self.emission[type2][word2] / types_count[type2]

        # f = open('probability.txt', 'w')
        # f.write(json.dumps(self.emission))
        # f.close()

    def _estimate_transition_probabilites(self, annotated_sentences):
        # words = [p[0] for s in annotated_sentences for p in s]
        successors = {tag: {t: 0 for t in self.tag_set} for tag in self.tag_set}
        for s in annotated_sentences:
            for u, v in list(zip(s[:-1], s[1:])):
                successors[u[1]][v[1]] += 1
        pprint(successors)

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
