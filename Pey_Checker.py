"""
	Name:Drishak Mohan
	Date: December 1th, 2018
	Description: A student is eligible for PEY if their CGPA is AT LEAST 2.0,
	they are also in year 2 or year 3, and they are in the CS program.

	You are tasked to write a function, given a student's CGPA, year, and program; determine whether they are eligible for PEY.
	You will return a Boolean value
"""
# a better name: check_PEY_eligibility(...)
def PEY_eligible(CGPA: float, year: int, program: str) -> bool:
    # This is some fantastic comment describing your code :)
    return((CGPA >= 2.0) and ((year == 2) or (year == 3)) and (program == "CS"))

# These are some test cases
## Test Case 1
### TRUE
print(PEY_eligible(3.6,3,"CS"))

## Test Case 2
### TRUE
print(PEY_eligible(2.1,2,"CS"))

## Test Case 3
### FALSE --> CGPA
print(PEY_eligible(1.3,3,"CS"))

## Test Case 4
### FALSE --> year
print(PEY_eligible(3.2,4,"CS"))

## Test Case 5
### FALSE --> program
print(PEY_eligible(3.2,2,"ART"))

## Test Case 6
### FALSE --> lowercase
print(PEY_eligible(3.2,2,"cs"))