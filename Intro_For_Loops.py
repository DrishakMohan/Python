"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to for loops .
"""



"""
## Loop Option 1
##### utilizing range
for i in range (0, 10, 2): # range from (START, STOP, STEP) 
    print(i)

b = "This is me!"

for i in range(0,len(b)):
    print(b[i])

a = "Hello World!"

## Loop Option 2
##### iterating through each instance of an object (a string in this case!)
for i in a:
    print(i)
"""

def is_digit(x:str) -> bool:
    return ((type(x) == str) and (len(x) == 1) and (ord('0') <= ord(x) <= ord('9')))

# Moving away from "static" thinking to more "dynamic" thinking 
def are_digits(x:str) -> bool:
    # Returns True iff all the characters in the string are numbers
    
    for i in x:        
        if is_digit(i) == True:
            answer = True
        else:
            answer = False
            #return answer
            break
    return answer
    
print(are_digits("12342112345"))
print(are_digits("12342a12345"))