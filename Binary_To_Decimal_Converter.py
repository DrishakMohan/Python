"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: convertion of binary to decimals .
"""



"""
for i in x:
    # method one

for i in range(start, stop, step):
    # method two

start = 0
stop = 1000
step = 10
for i in range (start, stop, step):
    print(i)
"""

name = "Michael"

start = 0
stop = len(name)
step = 1 #default value

for i in range (start,stop):
    print(name[i])

def decimal(binary_str: str) -> int:
    rev_str = binary_str[::-1]
    answer = 0
    
    for i in range (0, len(rev_str)):
        if (int(rev_str[i]) == 1):
            answer += (2 ** i)

    return answer

print(decimal("1000"))
print(decimal("0111001")) # 2^0 + 2^3 + 2^4 + 2^5 == 57


## Homework
# Hint: This function is easiest if an "index" is kept. You can do so with
# the range function, if you'd like.
# Hint 2: You may want to go through the string backwards.

def binary(decimal_str: str) -> int:
    '''Return the decimal value of the binary number represented by the str
    binary_str.

    binary(8)
    >>> 1000
    binary(57)
    >>> 0111001
    
    '''