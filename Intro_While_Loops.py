"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to while loops .
"""



"""
for i in range (start, stop, step):
    # do something

a = "abcdefghijklmnop"
for i in a:
    # do something
"""
correct_input = "Winnie" 
while True:
    temp_input = input("Enter your name: ")
    if (temp_input == correct_input):
        print("Well done! Hello Winnie! :)")
        break
    else:
        print("You are not authorized! >.<")

## Write a function that generates a random integer (1 - 10)
## and prompts the user (i.e. input) to find the correct random number.
## Once the user guesses correctly, return "You're Right!"

def find_me () -> str:
    import random
    random_number = random.randint(1,10)

    while True:
        guess = int(input("Enter random number: "))
        if (guess == random_number):
            return("You're Right!")
        else:
            print("Incorrect Guess!")
        
print(find_me())