"""
    Name: Drishak Mohan
	Date: December 19th, 2018
"""



from typing import List, Dict, TextIO
from random import randint
def count_occurrences(L: List[str]) -> Dict[str, int]:
    '''Return a dictionary in which the keys are
    the items in L and their associated values
    are integers denoting the number of times the
    item is contained in L.

    >>> count_occurrences(['cat', 'dog', 'cat', 'cat', 'dog'])
    {'dog': 2, 'cat': 3}
    >>> count_occurrences(['me', 'you', 'you', 'me', 'you', 'you'])
    {'me': 2, 'you': 4}
    '''
    d = {}
    for element in L:
        d[element] = L.count(element)
    return d

def associate_pair(d: Dict[str, List[str]], key: str, value: str):
    '''Add the key-value pair to d. keys may need to be associated with
    multiple values, so values are placed in a list.
    Assumption: key is immutable
    '''
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

def make_dictionary(f: TextIO) -> Dict[str, List[str]]:
    '''Return a dictionary where the keys are words in f and the value
    for a key is the list of words that were found to follow the key in f.
    '''
    d = {}
    context = ''

    for line in f:
        word_list = line.split()

        for word in word_list:
            associate_pair(d, context, word)
            context = word
            
    return d

def mimic_text(word_dict: Dict[str, List[str]], num_words: int) -> str:
    '''Based on the word patterns in word_dict, return a string that mimics
    that text, and has num_words words.
    '''
    story = ''
    context = ''
    
    for i in range(num_words):
        # Choose the next word, based on the context
        follow_words = word_dict[context]
        word = follow_words[randint(0, len(follow_words) - 1)]

        # Add to our fictionally created story
        story += ' ' + word
        context = word

    return story
    
    
"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""
if __name__ == '__main__':
    # Read a text and remember the words and what comes after them in a dictionary
    f = open(input("Training text: "))
    d = make_dictionary(f)
    f.close()
    print(mimic_text(d, 100))