"""
	Name:Drishak Mohan
	Date: December 1th, 2018
	Description: This is the area of a triangle written in the form of a 
	function. It is then called by the main body of the program and printed 
	to the screen.
"""

##########
# DEFINED 1ST FUNCTION
##########
def triangle_area(): # area of a triangle function
    height = 10
    base = 6
    Area = (height*base)/2
    return(Area)	# note that we are returning NOT printing
########

#Main Body of program 
print(triangle_area())	# this will use the hard-coded numbers in the 
						# function above (i.e. height of 10, base of 6)

##########
# DEFINED 2ND FUNCTION
##########
def triangle_area(height, base): # area of a triangle function
    Area = (height*base)/2
    return(Area)	# note that we are returning NOT printing
########

#Main Body of program 
print(triangle_area(20,5))
