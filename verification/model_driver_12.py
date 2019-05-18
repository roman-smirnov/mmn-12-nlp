import random
import itertools 
from pprint import pprint  
import numpy as np
import pandas as pd  
from sklearn.utils import shuffle
import sklearn.metrics 
import traceback
import sys
from tqdm import tqdm


def _safe_predict(tagger, sentence):
    try:
        return tagger.predict(sentence)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print('tagger crashed over the following input sentence with the following exception:\n{}\n{} {}'.format(sentence, exc_type, exc_value))
        #print(traceback.format_exc())
        return None

def _safe_bulk_predict(tagger, sentences):
    failed_predictions = 0
    predictions = []
    
    for sentence in tqdm(sentences):  
        prediction = _safe_predict(tagger, sentence)
        predictions.append(prediction)
        if prediction is None: 
            failed_predictions += 1
            
    return (predictions, failed_predictions)
    
    
def _evaluate(tagger, test_set):
    ''' evaluates a given trained tagger, through a given test set '''
    
    print('predicting with the tagger ...')
    
    test_set_input = list(map(lambda sentence: list(map(lambda entry: entry[0], sentence)), test_set))
    predictions, failed = _safe_bulk_predict(tagger, test_set_input)
    
    # evaluation
    
    print('computing the evaluation ...')
    
    segments = 0
    correct = 0
    failed_sentences = 0
    
    for sentence_idx in range(len(test_set)):
        sentence   = test_set_input[sentence_idx]
        prediction = predictions[sentence_idx]
        gold       = list(map(lambda entry: entry[1], test_set[sentence_idx]))
        
        segments += len(sentence)
                    
        if prediction is None:
            failed_sentences += 1
        else:
            for idx in range(len(sentence)):
                segment = sentence[idx]
                segment_prediction = prediction[idx]
                segment_gold       = gold[idx]
                
                if segment_prediction == segment_gold:
                    correct += 1
    
    token_accuracy = correct / segments
    print(f'sentences:        {len(test_set)}')
    print(f'failed sentences: {failed_sentences}')
    print(f'token accuracy:   {token_accuracy:.4f}')   
    
    return token_accuracy   
    

def model_driver_12(tagger_class_under_test, annotated_sentences, passes=3, split=0.1):

    ''' drives a given tagger implementation through training and evaluation '''

    assert 0 < split < 0.3, "the split argument value should be a proportion for the test set"

    token_accuracies = []
    
    for cross_validation_pass in range(passes):
        
        print()
        print(f'starting cross-validation pass {cross_validation_pass}')
        print('rebuilding the tagger under test')

        tagger_under_test = tagger_class_under_test()

        # get a train-test split
        shuffled = annotated_sentences
        for _ in range(10):
            shuffled = shuffle(shuffled)
        
        dataset_size = len(annotated_sentences)
        split_index  = int(dataset_size*split)
        test_set     = shuffled[:split_index]
        
        train_set    = shuffled[split_index:]

        print(f'train set size: {len(train_set)} sentences')
        print(f'test set size:  {len(test_set)} sentences')

        tagger = tagger_under_test.train(train_set)

        token_accuracies.append(_evaluate(tagger, test_set))

    
    ## final statistics across the cross validation passes

    final_token_accuracy = np.average(token_accuracies)
    std                  = np.std(token_accuracies)

    print()
    print('======================================')
    print('Final Cross-Validation Token Accuracy:')
    print(f'{final_token_accuracy:.3f} (std: {std:.5f})')
