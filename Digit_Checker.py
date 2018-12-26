"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: 
    Write a function is_digit that has a single string argument x and returns
    True or False. Include its docstring

    First you check to see if x is a string, then you check to see if it is of
    length 1. If it is not, the function returns False and terminates.

    If x is of length 1, it is checked if it is a digit, using the built-in
    function ord(). If it is, True is returned. Otherwise, False is returned.

    For example:
        is_digit("23") is False
        is_digit("3") is True
        is_digit("9") is True
        is_digit("hello") is False
        is_digit("3.05") is False
        is_digit("") is False
        is_digit(2) is False
        is_digit(3.05) is False
"""

def is_digit(x:str) -> bool:
    # Your code goes here
    return ((type(x) == str) and (len(x) == 1) and (ord('0') <= ord(x) <= ord('9')))
        
"""
        if (ord('0') <= ord(x) <= ord('9')):
            return(True)
    else:
        return(False)
"""
print(is_digit("23") == False)
print(is_digit("3") == True)
print(is_digit("9") == True)
print(is_digit("hello") == False)
print(is_digit("3.05") == False)
print(is_digit("") == False)
print(is_digit(2) == False)
print(is_digit(3.05) == False)