"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: This is just an example of how reducing a function increase the efficiency of the function.
"""

def my_test_function(x,y):
    if x > 100 and y > 0:
        if y > 100 and x > 0:
            return "A"
        elif y > 100 or x > 0:
            return "A"
        else:
            return "B"
    elif y <= 0 or x <= 0:
        if x == y:
            return "A"
        if x <= y and x >= y:
            return "B"
        if y < x and x < y:
            return "C"
        else:
            return "A"
    else:
        if x > 100 or y <= 0:
            return "A"
        if x <= 100 and y > 0:
            return "B"
        else:
            return "D"

print(my_test_function(50,50))
print(my_test_function(100,50))
print(my_test_function(200,50))
print(my_test_function(1,1))
print(my_test_function(500,500))
print(my_test_function(500,1500))
print(my_test_function(-1,-1))
print(my_test_function(-10,-5))
print(my_test_function(-5,-10))

def my_test_function_reduced(x,y):
    if x > 100 and y > 0:
        return "A"
    elif y <= 0 or x <= 0:
        return "A"
    else:                               # invoked if 0 < x <= 100
        if x <= 100:
            return "B"

print("\n~~~BREAK~~~\n")
print(my_test_function_reduced(50,50))
print(my_test_function_reduced(100,50))
print(my_test_function_reduced(200,50))
print(my_test_function_reduced(1,1))
print(my_test_function_reduced(500,500))
print(my_test_function_reduced(500,1500))
print(my_test_function_reduced(-1,-1))
print(my_test_function_reduced(-10,-5))
print(my_test_function_reduced(-5,-10))