"""
    Name:Drishak Mohan
	Date: December 1th, 2018
"""


# compute the summation of the integer string

x = "1234567890876543456789765432345678"
# what is the total of x?

# Words of wisdom: do not name your function anything more than 20 characters
def summation_of_all_the_numbers_inside_a_string(input_string:str) -> int:
    # Code me!
    answer = 0
    for i in input_string:
        answer = answer + int(i)
    return answer

number_string_one = "1234567890876543456789765432345678"
print(summation_of_all_the_numbers_inside_a_string(number_string_one))

number_string_two = "2468"
print(summation_of_all_the_numbers_inside_a_string(number_string_two))

number_string_three = "35810"
print(summation_of_all_the_numbers_inside_a_string(number_string_three))

number_string_four = "5467384756789257902847873627869"
print(summation_of_all_the_numbers_inside_a_string(number_string_four))

# Write a function that splits every other character into its own string.
# For example: "Hello There!" would be turned into two strings:
#               string_one: "HloTee"
#               string_two: "el hr!"
def word_splitter (in_str:str) -> (str,str):
    """ Pre-condition: you can assume that len(in_str) >=2
        Return two separate strings in the form of a 'tuple'
             i.e. (string_one, string_two)
    """
    string_one = ""
    string_two = ""
    
    for i in range(0,len(in_str)): 
        if ((i % 2) == 0):
            string_one += in_str[i]
        else:
            string_two += in_str[i]
    return (string_one,string_two)

s = "Hello There!"
print(word_splitter(s))

s1 = "This is me!"
print(word_splitter(s1))

s2 = "Where are we?"
print(word_splitter(s2))

# Write a function that counts all the white spaces in a sentence.
# Return the number of whitespaces
def whitespace_counter (in_str:str) -> int:
    space = 0

    for i in in_str:
        if i == " ":
            space += 1

    return space
    
    """
    for i in (in_str.split(" ")):
        space += 1

    return (space-1)
    """

print(whitespace_counter("This is CSC 108! Welcome Everyone!"))
# >>> 5
some_sentence = "Today is Tuesday October 2nd, 2018. We had a 6pm - 9pm lecture."
print(whitespace_counter(some_sentence))
# >>> 12