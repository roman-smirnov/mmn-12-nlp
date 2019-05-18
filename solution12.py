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
        self.labels = {}
        self.words = {}
        self.transitions = {tag: {t: 0 for t in self.tag_set} for tag in self.tag_set}
        self.labels_counter = {}
        self.words_counter = {}
        self.total_words = 0

    def _estimate_emission_probabilites(self, annotated_sentences):
        for word in self.emission:
            for type in self.emission[word]:
                self.emission[word][type] = self.emission[word][type] / self.labels_counter[type]

        f = open('probability.txt', 'w')
        f.write(json.dumps(self.emission))
        f.close()

    def _counters(self, annotated_sentences):
        for sentence in annotated_sentences:
            for couple in sentence:
                word = couple[0]
                type = couple[1]
                self.total_words += 1

                if type not in self.labels_counter:
                    self.labels_counter[type] = 0
                self.labels_counter[type] += 1

                if word not in self.words_counter:
                    self.words_counter[word] = 0
                self.words_counter[word] += 1

                if word not in self.emission:
                    self.emission[word] = {}

                if type not in self.emission[word]:
                    self.emission[word][type] = 0
                self.emission[word][type] += 1
        # f = open('counts.txt', 'w')
        # f.write(json.dumps(self.emission))
        # f.close()
        #
        #
        # f = open('words.txt', 'w')
        # f.write(json.dumps(self.words_counter))
        # f.close()

    def _find_max_conditional_probabilty(self, word):
        if word not in self.emission:
            random.choice(self.tag_set)

        max_probabilty = 0
        curr_label = random.choice(self.tag_set)
        for label in self.emission[word]:
            probabilty = self.emission[word][label] * self.labels[label] / self.words[word]
            if probabilty > max_probabilty:
                max_probabilty = probabilty
                curr_label = label

        return curr_label


    def _probabilty_label(self):
        for label in self.labels_counter:
            self.labels[label] = self.labels_counter[label] / self.total_words

    def _probabilty_word(self):
        for word in self.words_counter:
            self.words[word] = self.words_counter[word] / self.total_words

    def _estimate_transition_probabilites(self, annotated_sentences):
        successors = {tag: {t: 0 for t in self.tag_set} for tag in self.tag_set}
        for s in annotated_sentences:
            for u, v in list(zip(s[:-1], s[1:])):
                successors[u[1]][v[1]] += 1

        for t in self.tag_set:
            suc_sum = sum(successors[t].values())
            for ts in self.tag_set:
                self.transitions[t][ts] = successors[t][ts]/suc_sum

        pprint(self.transitions)

    def train(self, annotated_sentences):
        """ trains the HMM model (computes the probability distributions) """
        print('training function received {} annotated sentences as training data'.format(len(annotated_sentences)))
        self._counters(annotated_sentences)
        self._estimate_emission_probabilites(annotated_sentences)
        self._estimate_transition_probabilites(annotated_sentences)
        self._probabilty_label()
        self._probabilty_word()
        return self

    def predict(self, sentence):
        prediction = [self._find_max_conditional_probabilty(segment) for segment in sentence]
        assert (len(prediction) == len(sentence))
        return prediction
