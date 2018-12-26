"""
	Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Adults order 2 slices --> x
	Students order 3 slices --> y
	Children order 1 slice --> z

	Each pizza has exactly 8 slices.
	You can't order individual slices, only whole pizzas. 

	Write a function, which takes 3 parameters (x,y,z), representing
	the number of pizzas required to feed these hungry people.

	HINT: Math's ceiling function! Integer division after adding 7! 

"""
import math

def how_many_pizzas(adult:int, child:int, university_student:int) -> int:
    slices = (adult*2)+(university_student*3)+(child*1)
    return(math.ceil(slices/8))
    # alternate answer: return ((slices + 7) // 8)

print(how_many_pizzas(5,5,5))
