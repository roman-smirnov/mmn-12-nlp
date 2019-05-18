import subprocess
import pyconll
import itertools 
import os.path
from .util import get_single_file
from pathlib import Path


def _conllu_transformer_POS_tagging(source):
    '''
    transforms a conllu entry into an entry for our task
    
    filters away all fused entries that conllu files tend to 
    include for every decomposed word form, as that would be 
    just wierd duplication counterproductive for our tasks
    '''
    
    sentences = []
    
    for entry in itertools.chain(source): 
        
        valid_sentence = True # https://github.com/pyconll/pyconll/issues/37
        
        sentence = []
        for idx, token in enumerate(entry):
            
            if '-' in token.id: continue # skip fused tokens
            
            sentence.append((token.form, token.upos))
            
            if not token.form: valid_sentence = False
                    
        if valid_sentence:
            sentences.append(sentence)    
    
    return sentences    


def build_POS_tagging_data(source_treebank_name = "UD_Hebrew-HTB", git_hash = "82591c955e86222e32531336ff23e36c220b5846"):
    if not os.path.isdir(source_treebank_name) :
        print("fetching the data source from github...")
        subprocess.run(["git", "clone", "https://github.com/UniversalDependencies/" + source_treebank_name])
        subprocess.run(["git", "checkout", git_hash], cwd=source_treebank_name)    

    print("transforming the data source...")
    
    conllu1 = pyconll.load_from_file(Path.cwd().joinpath(source_treebank_name, get_single_file(source_treebank_name, 'train')))
    conllu2 = pyconll.load_from_file(Path.cwd().joinpath(source_treebank_name, get_single_file(source_treebank_name, 'dev')))

    return _conllu_transformer_POS_tagging(conllu1) + _conllu_transformer_POS_tagging(conllu2)