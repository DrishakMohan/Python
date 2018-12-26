"""
    Name:Drishak Mohan
	Date: December 1th, 2018
"""

def checker(x):
    """
    Checks wheather x is less than,greater than or equal to 10 and 20 or 10 or 20 
    """
    if x > 10:
        if x <=20:
            # do something
            return ("x is greater than 10")
        else:
            return("Error")
    elif x > 20:
        # do something else
        return ("x is greater than 20")
    else:
        # do my last thing
        return ("x is not greater than 10 or 20")

print(checker(21))

# Given a server's response time
# Return "server down" if the response_time takes longer than 5000ms
# Return "server okay" if it returns a fast response_time

def server_status(response_time:int) -> str:
    # Complete the docstring && the code for this function!
    if response_time > 5000:
        return("Server Down")
    #elif response_time < 5000:
    else:
        return("Server Okay")

print(server_status(3000))
print(server_status(7000))
print(server_status(4600))
print(server_status(5000))