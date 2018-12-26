"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Encrypting a letter,sentence and then decrypting it back .
    key is a parameter which states the postion of a letter to be shifted right by k units or letters
"""



def encrypt_letter(letter: str) -> str:
    """ Encrypt letter by shifting three places to the right. """
    base = ord('a')
    offset = ord(letter) - base + 3
    if offset > 26:
        offset = offset - 26
    return chr(base + offset)

def encrypt_letter_with_key(letter: str, key: int) -> str:
    """ Encrypt letter by shifting three places to the right. """
    base = ord('a')
    offset = ord(letter) - base + key
    if offset > 26:
        offset -= 26
    return chr(base + offset)

def encrypt_sentence(sentence:str, key:int) -> str:
    """ Return a sentence that is caesar encrypted by some offset 'key' """
    answer = ""
    for x in sentence:
        answer += encrypt_letter_with_key(x,key)
    return answer

print(encrypt_sentence("this is my secret message", 5))
print(encrypt_sentence("my name is john", 5))
print(encrypt_sentence("abcdefghijklmnopqrstuvwxyz", 5))

# take home problem!
# try it with punctuation too! :)
# encrypt_sentence("Hi there! My name is mike, what is yours??", 4)

def decrypt_letter_with_key(letter: str, key: int) -> str:
    """ Encrypt letter by shifting three places to the right. """
    base = ord('a')
    offset = ord(letter) - base - key
    if offset < 0:
        offset += 26
    return chr(base + offset)

def decrypt_sentence(sentence:str, key:int) -> str:
    """ Return a sentence that is caesar encrypted by some offset 'key' """
    answer = ""
    for x in sentence:
        answer += decrypt_letter_with_key(x,key)
    return answer

print(decrypt_sentence("ymnx%nx%rd%xjhwjy%rjxxflj", 5))
print(decrypt_sentence("rd%sfrj%nx%otms", 5))
print(decrypt_sentence("fghijklmnopqrstuvwxyz{bcde", 5))