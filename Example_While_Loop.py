"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: returns every third character starting from position n
"""





def every_third (s:str,n:int) -> str :
    # returns every third character starting from position n
    # on string s. USE A WHILE LOOP.
    ans = ""
    while ((n+2) < len(s)):
        ans += s[n+2]
        n = n+3  	# equivalent to n+=3
    return(ans)
print(every_third("abcdefg",0))
print(every_third("hello there",0))
print(every_third("hello there",2))

"""
every_third("abcdefg",0) --> "cf"
every_third("hello there",0) --> "l e"
every_third("hello there",2) --> "ohe"
"""
def every_third_ui (n:int) -> str :
    # returns every third character starting from position n
    # on string prompted by user.
    
"""
every_third_ui(0)
>> What is your word? "It's me! Who are you?"
>> 'm ory?    
"""


def index_of(s: str, ch: str, n: int) -> int: # CHALLENGE QUESTION
'''Return the index of the nth instance of character ch in the string s or
-1 if there is no nth instance of ch in s.
>>> index_of('abcaca', 'a', 1)           --> 0
>>> index_of('abcaca', 'a', 2)           --> 3
>>> index_of('abcaca', 'a', 4)           --> -1
'''
