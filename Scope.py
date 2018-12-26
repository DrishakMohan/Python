# Scope Example

## Attempt 1
def my_function():
    print(x)

x = 5
my_function()   # What is the output? Why did it happen?


## Attempt 2
# def my_function():
#     print(x)
#     x = 1

# x = 5
# my_function()   # What is the output? Why did it happen?


# Note: You must uncomment the blocks to test the code and result

# Example 1


x = 5
def my_function(y):
    return (y + x)

print(my_function(6))

# Example 2

y = 5
def my_function(y):
    return (y)

print(my_function(6))


#  Example 3

y = 5
def my_function(y):
    x = y
    return (x + 2*y)

print(my_function(6))



"""
For Example:
    If given: x = 1, y = 2, z = 3
        adult(1) + child(2) + university_student(3)
        3 + 4 + 15 = 22
    Should return: "22 cookies"
"""

def cookie_monster(adult:int, child:int, university_student: int) -> str:
    # Each adult (x) --> eats 3 cookies
    # Each child (y) --> eats 2 cookies
    # Each university_student (z) --> eats 5 cookies
    # return the required number of cookies
    result = ((adult*3) + (child*2) + (university_student*5))
    return (str(result) + " cookies")

print(cookie_monster(1,2,3))