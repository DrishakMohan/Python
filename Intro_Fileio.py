"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Introduction to FileI/O .
"""



# with open ("hello.txt") as file: 
# 	read_data = file.read()

# print(read_data)


file = open("hello.txt", 'r')
#a = file.readline()
b = file.readlines()
#c = file.read(8)

#print(a)
print(b)
#print(c)

file.close()

file = open("output.txt", 'w')
file.write("This is a test!\nThis is pretty neat!!")
#file.write("What will happen now?")
file.close()

file = open("output.txt", 'w')
file.write("What will happen now?")
file.close()

print("This is the start!")
try:
    f = open("file.txt", 'r')
    print(f.readlines())
    f.close()
except:
    print("The Error was caught!! Aha!")

print("This is the end")


try:
    f = open("data.txt", 'r')
    data = f.readlines()
    age = []
    name = []
    print(data)
    for i in data:
        a = i[:len(i)-1]
        temp = a.split(",")
        name.append(temp[0])
        age.append(temp[1])
    print(name[1:])
    print(age[1:])
    f.close()
except:
    print("There was an Error with the data.txt file!")



from typing import TextIO, List

def get_bandnames(band_file: TextIO) -> List[str]:
    '''Return a list of all of the bandnames in a band file.
    Assumption: Header lines have been removed
    '''
    bands = []
    for line in band_file:
        fields = line.strip().split(",")
        #fields = line.split(",")
        bands.append(fields[0])
    return bands

bands_file = open("bands.txt", 'r')
print(get_bandnames(bands_file))


