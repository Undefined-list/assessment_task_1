alphabet = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#an alphabet for indexing individual letters
def decrypt():
    cypher = input("What is the cypher? ")
    message= input("what is the encrypted word? ")
    #user input of the cypher and encrypted word
    i=0
    #while loop
    decrypted= ""
    #to hold the message
    while i < len(message):
        #while loop using the counter as an index for message
        toomuch = 0
        for x in cypher:
            x = x.lower()
            lower_letter = message[i].lower()
            #Making the letters both lower, to be able to index them in alphabet
            special_character = True
            #to check for special characters
            while special_character ==True:
                lower_letter = message[i].lower()
                #making the lower_letter variable a new letter, if it goes through loop more than once
                if lower_letter not in alphabet:
                    decrypted += lower_letter
                    #to add the special character into the outputted text
                    i+=1
                    #changing the letter that is in the lower_letter variable
                    if i >= len(message):
                        #if i equals the length it must break out of the loop, incase the end has more than one special character
                        break
                else:
                    special_character = False
                    #ends loop
            if x not in alphabet:
                #will skip any special characters in the cypher
                toomuch +=1
                if toomuch >= len(cypher):
                    return "Please enter an actual cypher."
                continue
          
            letter= alphabet.index(lower_letter)-alphabet.index(x)
            #the index of the letter in the message minus the one in the cypher will give you the index in the alphabet, negatives are okay, the negative index works out
            Is_upper = message[i]
            Is_upper = Is_upper.isupper()
            #outputs a bool if a letter is upper or isnt
            if Is_upper == True:
                #checks if the letter is upper, and makes it upper case in the output
                decrypted += alphabet[letter].upper()
            else:
                #doesnt make it upper
                decrypted += alphabet[letter]
            
            i+=1
            #makes the letter from the message change
            if i >= len(message):
                #if i is greater or equal to message the message indexing will break leading to an error
                break
    return decrypted
    #returns decrypted word
def encrypt():
    cypher = input("what cypher do you want to use? ")
    to_encrypt = input("what do you want to encrypt? ")
    #input
    encrypted = ""
    i=0
    while i < len(to_encrypt):
        toomuch = 0 
        for x in cypher:
            x = x.lower()
            special_character =True
            while special_character == True:
                lower_letter = to_encrypt[i].lower()
                if lower_letter not in alphabet:
                    encrypted += lower_letter
                    i+=1
                    if i >= len(to_encrypt):
                        break
                else:
                    special_character =False
                #legit all the same as in the last function
                    
            if x not in alphabet:
                toomuch += 1
                if toomuch >= len(cypher):
                    return "Please enter an actual cypher."
                continue
            
            lower_letter = to_encrypt[i].lower()
            letter = alphabet.index(x) + alphabet.index(lower_letter)
            #adds them together, to get the index of the letter on the table for the cypher
            if letter > 25:
                letter -= 26 
                #if its greater than 25, subtracts 26 to reset it to the begining of alphabet
            Is_upper = to_encrypt[i]
            Is_upper = Is_upper.isupper()
            if Is_upper == True:
                encrypted += alphabet[letter].upper()
            else:
                encrypted += alphabet[letter]
            i+=1
            if i >= len(to_encrypt):
                break
    return encrypted
which = input("Do you want to encrypt or decrypt? ")
#input whether or not you want to encrypt or decrypt with the cypher
which = which.lower()
if which == "encrypt":
    print(encrypt())
    #calls functions to encrypt as well as printing returned value
elif which == "decrypt":
    print(decrypt())
    #calls functions to decrypt as well as printing returned value
else: 
    print("Please enter the words: 'encrypt', 'decrypt' only")