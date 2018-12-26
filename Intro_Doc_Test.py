"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to Doc test and example.
"""




def abs(x):
    """
    >>> abs(0)
    0
    >>> abs(-2)
    2
    >>> abs(2)
    2
    >>> abs(89)
    89
    >>> abs(-1024)
    1024
    """
    if x < 0:
        return -x
    return x

def our_max(num1: int, num2: int) -> int:
    """returns the larger of num1 and num2
       if equal, pick one! :-)
       >>> our_max(14,222)
       222
       >>> our_max(-12,6)
       6
       >>> our_max(3,12)
       12
    """
    ## Your code goes here
    return num1*(num1 >= num2) + num2*(num2 > num1) 

from typing import List
def indices(s: str, substr: str) -> List[int]:
    '''Return the indices in s at which non-overlapping
    copies of substr start. substr is non-empty.
    Make sure you ignorecase!

    >>> indices('A Coool pool look', 'oo')
    [3, 9, 14]
    >>> indices('My name is Michael, it is me myself and I!', 'my')
    [0, 29]
    >>> indices('Jamal, I am here', 'am')
    [1, 9]
    '''
    count = []
    a = s.count(substr)

    for value in range(a):
        index = s.find(substr,count+len(value))
        count.append(index)

    return count
    
    
    
    """
    index = 0
    ans = []

    while index != -1:
        ans.append(s.find(substr, index))
        index = s.find(substr, index + len(substr))
    return ans
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()






    
