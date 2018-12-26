"""
    Name:Drishak Mohan
	Date: December 1th, 2018
"""


from typing import List, Dict
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()