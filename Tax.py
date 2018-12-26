
"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: This function calculates the tax.
"""
"""
Example:
    Person A has an income of $100,000
    Person A's tax rate is 25%
    What is Person A's tax? 
"""
some_income = 100000 # this is an example input
some_tax_rate = 0.25 # this is another example input

"""
    How much $$$ will Person A pay in taxes?
"""
def calc_tax(income, tax_rate):
    return(income*tax_rate)

print(calc_tax(some_income, some_tax_rate)) # an example call of your function

"""
    What is Person A's net income? How much $$$ is left after tax 
"""
def after_tax_income(income, tax_rate):
    return(income-calc_tax(income,tax_rate))

print(after_tax_income(some_income, some_tax_rate)) 

"""
    What is person A's gross income? How much $$$ before tax? 
"""

def gross_income(after_tax_income, tax_rate):
    return(after_tax_income/(1-tax_rate))

# Note how the functions are 'nested' (i.e. within one another)
print(gross_income(after_tax_income(some_income, some_tax_rate), some_tax_rate))