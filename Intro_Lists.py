"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to lists .
"""




"""
a = "This is a sentence"
l = []
for i in range(len(a)):
    l.append(a[i])
print(l)
"""

from typing import List
def get_even(L: List[int]) -> List[int]:
    '''Return a list containing the even elements of L.'''
    temp_list = []
    for x in L:
        if x%2==0:
            temp_list.append(x)
    return temp_list
    
print(get_even([]) == [])
print(get_even([1, 3]) == [])
print(get_even([2, 1, 2]) == [2, 2])

def all_titlecase(L: List[str]) -> bool:
    '''Return True iff all of the strings in L are titlecased.
       Unless it starts the title: and, or, the, of --> all lowercase
    '''
    temp = []
    check = ["and", "or", "the", "of"]
    flag = False

    if L == []:
        flag = True
        return flag

    for i in L:
        temp = i.split(" ")
        for j in temp:
            if not j in check:
                if (j[0].isupper() and j[1:].islower()):
                    flag = True
                else:
                    flag = False
                    return flag
            elif ((j in check) and (j == temp[0])):
                flag = False
                return flag
    return flag
                    

print(all_titlecase([])) # True
print(all_titlecase(['The Book of Three','The Name of the Wind','Snow Crash'])) # True
print(all_titlecase(['The Book of Three','The Name of the Wind','SNow Crash'])) # False
print(all_titlecase(['the Book of Three','The Name of the Wind','Snow Crash'])) # False
print(all_titlecase(['The JuNGLE Book','The Bible','Earth Meets Air'])) # False 
print(all_titlecase(['The Jungle Book','the Bible','Earth Meets Air'])) # False
print(all_titlecase(['The Jungle Book','The bible','Earth Meets Air'])) # False
print(all_titlecase(['The Jungle Book','The Bible','Earth Meets aIr'])) # False
print(all_titlecase(['The Jungle Book','The Bible','Earth Meets Air'])) # True

    