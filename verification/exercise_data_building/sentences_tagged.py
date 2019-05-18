import subprocess
import pyconll
import itertools 
import os.path
from .util import get_single_file
from pathlib import Path

def _conllu_transformer(source):
    ''' 
    transforms a conllu sentence into a list of segment entries capturing per segment:
      • its form
      • weather a verb/non-verb
      
    filters away all fused entries that conllu files tend to 
    include for every decomposed word form, as that would be 
    just wierd duplication counterproductive for our tasks
    '''
    
    sentences = []
    
    for entry in itertools.chain(source): 
        
        valid_sentence = True # https://github.com/pyconll/pyconll/issues/37
                
        sentence = []
        for idx, token in enumerate(entry):
            
            if '-' in token.id: continue # skips fused segments
                         
            if token.upos == 'VERB':
                sentence.append(dict(token=token.form, label=1))
            else:
                sentence.append(dict(token=token.form, label=0))
                
            if not token.form: valid_sentence = False
        
        if valid_sentence:
            sentences.append(sentence)    
    
    return sentences    


def build_verb_in_context_data(source_treebank_name = "UD_Hebrew-HTB", git_hash = "82591c955e86222e32531336ff23e36c220b5846"):
    ''' transforms conllu files to a lists where each entry is a segment with verb/non-verb indciation '''
        
    if not os.path.isdir(source_treebank_name) :
        print("fetching the data source from github...")
        subprocess.run(["git", "clone", "https://github.com/UniversalDependencies/" + source_treebank_name])
        subprocess.run(["git", "checkout", git_hash], cwd=source_treebank_name)    

    print("transforming the data source...")
    
    conllu1 = pyconll.load_from_file(Path.cwd().joinpath(source_treebank_name, get_single_file(source_treebank_name, 'train')))
    conllu2 = pyconll.load_from_file(Path.cwd().joinpath(source_treebank_name, get_single_file(source_treebank_name, 'dev')))

    return _conllu_transformer(conllu1) + _conllu_transformer(conllu2)
            
