"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to Dictionaries .
"""


# NEXT: Dictionaries
## Creating a dictionary
#my_dict = {}

### Key:Value
my_dict = {1:'apple', 2:'pear', 3:'peach', 4:'coconuts'}
roman = {1:'I', 5:'V', 10:'X'}

## How to access elements
print(my_dict[1])
print(roman[10])

## Add/Change elements
roman[50] = 'L'

## Check element addition
print(roman)

## Delete elements
del roman[1]

## Check element deletion
print(roman)

## Dictionary Methods
#### clear() -- removes all items
#### copy() -- returns a shallow copy of the dictionary
#### update([other]) -- update value based on other (key,value)

# Practice Question
#Inventory: "pie":15, "pizza":3, "burger":45, "KD":55, "ramen":33
## Recall: key:value

def checker (word:str) -> int:
    """Create a function that checks how many items are in our food
       inventory system. They must match the words in our dictionary.
    """
    inv_dict={"pie":15, "pizza":3, "burger":45, "KD":55, "ramen":33}
    try:
        return(inv_dict[word])
    except:
        return("Not in inventory!")

print(checker("KD"))
print(checker("Hot Dog"))
print(checker("pie"))

def checker_pro(sentence:str) -> int:
    """Given the checker above, you are to create a function (checker_pro)
that takes in a sentence and outputs the sum of all of the items."""
    count = 0
    # sentence = sentence.split(" ")
    inv_dict={"pie":15, "pizza":3, "burger":45, "KD":55, "ramen":33}
    
    for i in sentence:      # Doesn't account for special characters
        try:
            count += inv_dict[i]
        except:
            count += 0
    """
    for i in inv_dict:      # Doesn't account for duplicate keys
        if i in sentence:   # can strip() and split() this
            count += inv_dict[i]
    """
    return count
    
print(checker_pro("How much pie is there left in the ramen kitchen?"))
print(checker_pro("I'll take a slice of pizza with my KD!"))
print(checker_pro("I'll take a slice of pizza with my pizza!"))
