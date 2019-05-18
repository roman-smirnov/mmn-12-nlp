class SubmissionSpec12:
    ''' 
    A class spec to inherit for your submission for the programming questions of this Maman.
    The contrived example implementation (solution12.py) exemplifies inheriting this class. 
    '''
    
    def train(self, annotated_sentences):
        ''' 
        Your function training your model. The argument to this function is the training set your 
        class will get for training, you do not need to split this data, you need to train on ALL 
        OF IT and on nothing but it.
         
        Input Argument: 
        • a list of tuples of the shape (segment, segment_tag)
            
        Returns: 
        • the class instance itself (self), for caller convenience only
        '''
    
    def predict(self, annotated_sentence):
        ''' 
        Your inference function.
         
        Input Argument:
        • a single sentence to predict, shaped as a list of segments
            
        Returns: 
        • a list comprising the predicted tag sequence for the input sentence, where each element is the tag name
        '''
    
    def _estimate_emission_probabilites(self, annotated_sentences):
        ''' 
        an internal function for estimating (computing) the HMM emission probabilities.
        not part of the driver API but we would prefer to have this uniform naming 
        '''
    
    def _estimate_transition_probabilites(self, annotated_sentences):
        ''' 
        an internal function for estimating (computing) the HMM transition probabilities.
        not part of the driver API but we would prefer to have this uniform naming 
        '''