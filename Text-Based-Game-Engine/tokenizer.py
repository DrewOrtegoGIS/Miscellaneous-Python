''' tokenizer.py

    Used to process in/valid commands. The basic elements of this game are 
    powered by the tokenizer. A token is a word-type and its associated word, 
    such as a "noun" called "chair". The game will always look for a valid 
    pattern of tokens when deciding whether a user's input is valid or not.
'''

import commands as c

valid_patterns = ( # Globally accessible to pattern_match and process_tokens
    ['verb'],
    ['direction'],
    ['noun'],
    ['adjective', 'noun'],
    ['interface'],
    ['verb', 'noun'],
    ['verb', 'adjective', 'noun'],
    ['noun', 'verb'],
    ['verb', 'direction'],
    ['verb', 'preposition', 'noun'],
    ['verb', 'preposition', 'adjective', 'noun'],
    ['verb', 'preposition', 'preposition', 'noun'],
    ['verb', 'noun', 'combine', 'noun'],
    ['verb', 'preposition', 'noun', 'combine', 'noun'],
    ['verb', 'noun', 'combine', 'preposition', 'noun'],
    ['verb', 'preposition', 'noun', 'combine', 'preposition', 'noun']
)

def get_token(user_input):
    ''' Tokenizes the given input and returns a list element. Skips over the
        "ignore" commands and doesn't include them in the returned list.
        Any unrecognized words will be returned as an error.'''
    tokenized_words = []
    for word in user_input:
        if   word in c.verbs: tokenized_words.append({'verb':word})
        elif word in c.nouns: tokenized_words.append({'noun':word})
        elif word in c.directions: tokenized_words.append({'direction':word})
        elif word in c.combine: tokenized_words.append({'combine':word})
        elif word in c.interface: tokenized_words.append({'interface':word})
        elif word in c.preposition: tokenized_words.append({'preposition':word})
        elif word in c.adjectives: tokenized_words.append({'adjective':word})
        else: return [{'error':word}]
    return tokenized_words


def pattern_match(tokenized_input):
    ''' Compares the word-type pattern of the user's input to the list of all 
        valid patterns. Returns True if the pattern of the input is matched to 
        a listed pattern.'''
    global valid_patterns
    user_pattern = [list(token_key.keys())[0] for token_key in tokenized_input]
    if user_pattern in valid_patterns:
        return user_pattern
    else:
        return False
