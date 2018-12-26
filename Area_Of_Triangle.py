"""
    Name: Drishak Mohan
	Date: December 19th, 2018
	Description: This is the area of a triangle written in the form of a 
	function. It is then called by the main body of the program and printed 
	to the screen.
"""

def triangle_area() -> str:
    """
    This function takes in two Float or int parameters from user, Base and Height, of type float to calculate Area of a triangle in float.
    """
    print(" Enter Value Of Base : ")
    Base = float(input())
    # input function returns string value. 
    
    print(" Enter Value Of Height : ")
    Height = float(input())

    print(" Enter unit: ")
    unit = input()

    while Base <= 0.0 or Height <= 0.0 or unit.isalpha() == False:
        
        if Base <= 0.0 and Height <= 0.0 and unit.isalpha() == False:
            
            print("Enter valid float value of Base  : ")
            Base = float(input())
            
            print("Enter valid float value of Height : ")
            Height = float(input()) 

            print("Enter valid correct unit : ")
            unit = input()
        
        elif Base <= 0 and unit.isalpha() == False:
            print("Enter valid value for Base :")
            Base = float(input())

            print("Enter valid correct unit : ")
            unit = input()
        
        elif Height <= 0.0 and unit.isalpha() == False:
            print("Enter valid float value of Height : ")
            Height = float(input()) 
            
            print("Enter valid correct unit : ")
            unit = input()

        elif Base <= 0.0 and Height <= 0.0:
            print("Enter valid float value of Base  : ")
            Base = float(input())
            
            print("Enter valid Height : ")
            Height = float(input()) 

        elif Base <= 0:
            print("Enter valid value for Base :")
            Base = float(input())
       
        elif Height <= 0.0:
            print("Enter valid value for Height :")
            Height = float(input())
        
        elif unit.isalpha() == False:
            print("Enter valid correct unit : ")
            unit = input()
    return "{0} square {1}".format(0.5*Height*Base,unit)
a=triangle_area()
print(a)



    
        
