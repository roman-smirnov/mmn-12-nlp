# NOTES


- emission probabilities: given a tag, how likely is each word to be annotated by it. 
- transition probabilities: given a tag, the probability of each tag to be the next in the sequence.  

`annotated_sentences` is a list of lists of 2-tuples

```
`[('DATE', 'NOUN'), (':', 'PUNCT'), ('Tuesday', 'PROPN'), (',', 'PUNCT'), ('November', 'PROPN'), ('22', 'NUM'), (',', 'PUNCT'), ('2005', 'NUM')], [('remember', 'VERB'), ('to', 'PART'), ('bring', 'VERB'), ('cash', 'NOUN'), ('since', 'SCONJ'), ('they', 'PRON'), ('do', 'AUX'), ("n't", 'PART'), ('take', 'VERB'), ('debit', 'NOUN'), ('or', 'CCONJ'), ('credit', 'NOUN'), ('.', 'PUNCT')]
```

There are 17 tags
```
tag_set = 'ADJ ADP PUNCT ADV AUX SYM INTJ CCONJ X NOUN DET PROPN NUM VERB PART PRON SCONJ'.split()
```


```
SENTENCE:
 ['Actually', 'it', 'is', 'not', 'a', 'new', 'truck', '.']
PREDICTION:
 ['PART', 'PUNCT', 'INTJ', 'X', 'ADV', 'INTJ', 'CCONJ', 'NOUN']
SENTENCE:
 ['Thanks', '.']
PREDICTION:
 ['CCONJ', 'PART']
SENTENCE:
 ['Wayne']
PREDICTION:
 ['NUM']
SENTENCE:
 ['Thanks', ',']
PREDICTION:
 ['SYM', 'PRON']
SENTENCE:
 ['David']
PREDICTION:
 ['ADV']
SENTENCE:
 ['I', 'think', 'compared', 'to', 'my', 'house', ',', 'he', "'s", 'embarrased', 'about', 'his', 'apartment', '.']
PREDICTION:
 ['ADP', 'INTJ', 'PUNCT', 'SYM', 'PART', 'ADV', 'AUX', 'SYM', 'PUNCT', 'X', 'PUNCT', 'PART', 'NOUN', 'CCONJ']
SENTENCE:
 ['I', 'have', 'been', 'here', 'a', 'few', 'times', 'for', 'oil', 'changes', 'and', 'just', 'got', 'my', 'tires', ',', 'alignment', 'and', 'state', 'inspection', 'done', 'yesterday', '.']
PREDICTION:
 ['X', 'ADP', 'AUX', 'NUM', 'SCONJ', 'AUX', 'X', 'PUNCT', 'ADP', 'CCONJ', 'NOUN', 'ADV', 'X', 'PART', 'ADV', 'SCONJ', 'ADJ', 'PART', 'SCONJ', 'NUM', 'DET', 'PART', 'PRON']
```