"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Examples to Lists .
"""


def remove_x(xs:list, x:int) -> list:
    """ Removes all instances of x from the list xs."""
    for i in xs:
        if x == i:
            xs.remove(i)

    return xs

"""
while x in xs:
    xs.remove(x)
return xs
"""
from typing import List
def disassemble(cs:str) -> List[str]:
    """Returns a list of characters comprising cs,
    maintaining order."""
    # return list(cs)
    d_list=[]
    for x in cs:
        d_list.append(x)
    return d_list

from typing import List
def list_addition(A:List[int], B:List[int]) -> List[int]:
    """Given two lists of equivalent size, return the sum of those values."""
    z = []
    if len(A) == len(B):
        for i in range(len(A)):
            z.append(sum((A[i],B[i])))
    else:
        z = "Error! You must input lists of the same size!"
    return z
"""
>>> list_addition([1, 2], [3, 4])
    [4, 6]
>>> list_addition([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
>>> list_addition([1, 2], [3, 4, 5])
    Error! You must input lists of the same size!
"""
print(list_addition([1, 2], [3, 4]))
print(list_addition([1, 2, 3], [4, 5, 6]))
print(list_addition([1, 2], [3, 4, 5]))

def list_addition2(A:List[int], B:List[int], C:List[int]) -> List[int]:
    """Given three lists of equivalent size, return the sum of those values."""
    z = []
    if len(A) == len(B) == len(C):
        for i in range(len(A)):
            z.append(sum((A[i],B[i],C[i])))
    else:
        z = "Error! You must input lists of the same size!"
    return z

"""    
>>> list_addition2([1, 2], [3, 4], [5, 6])
    [9, 12]
>>> list_addition2([1, 2, 3], [4, 5, 6], [7, 8, 9])
    [12, 15, 18]
>>> list_addition2([1, 2], [3, 4, 5], [6, 7])
    Error! You must input lists of the same size!
"""
print(list_addition2([1, 2], [3, 4], [5, 6]))
print(list_addition2([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(list_addition2([1, 2], [3, 4, 5], [6, 7]))


    

    