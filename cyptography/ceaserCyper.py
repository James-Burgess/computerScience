#!/usr/bin/python3 
import sys

def text_to_number(input_Array):
    #letter to ordinate
    mylist = []
    for letters in input_Array:        
        mylist.append(ord(letters))
    return mylist

def shift_cypher(input_Array,key):
    #ordinate to encrypted
    mylist = []
    for number in input_Array:     
        mylist.append(number + key)
    return mylist


def num_to_string(inputList):
    mylist = []
    for numbers in inputList: #encryptedOrdinate to Letters
        mylist.append(chr(numbers))
    return mylist

def decrypt():
	userInput = str(input("plz enter text"))
	key = int(input("Please enter the key: \n"))
	crypt(userInput, -key)

def encrypt():
	userInput = str(input("plz enter text"))
	key = int(input("Please enter the key: \n"))
	crypt(userInput, key)

def crypt(userInput, key):

	unicoded = text_to_number(list(userInput))
	encryptedUnicode = shift_cypher(unicoded, key)

	encryptedOrdinate = num_to_string(encryptedUnicode)
	encryptedString = ''.join(encryptedOrdinate)

	print(encryptedString)


def main(name, user_input):
	if user_input == 'decrypt':
		decrypt()
	elif user_input == 'encrypt':
		encrypt()
	else:
		print("useage is ./ceaserCyper.py encrypt/decrypt")

if __name__ == '__main__':
	main(*sys.argv)
