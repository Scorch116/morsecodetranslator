"""
Ed McGrath - Morse code translator
"""
"""
NEED TO UNDERSTAND .... VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
"""

#Morse code dictionary from a morse code chart
codeDict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


#setting a function to decrypt an input - morse to english!
def decryption(input):
    input += ' '
    deci = '' #decipher
    cit = '' # citext

    for character in input:
        if character != ' ':  # checking for spaces
            i = 0             #couter for keeping count of the spaces
            cit += character  #store input into character
        else:  #in case of space
            i += 1  # this indicates new character

            if i == 2: # will indicate start of new word
                deci += ' '   # add space to make sure words are separated

            else:

                deci += list(codeDict.keys())[list(codeDict.values()).index(cit)]
                cit = ''

    return deci

input = ".... . .-.. .-.. --- -....- .-- --- .-. .-.. -.." # Hard code cause I cannot seem to get it to work with input will have to further investigate
morse = input

print(decryption(morse))



def encryption(input):
    cit = ''
    for character in input:                                   #ADDS MORSE CODE WITH SPACE TO SERARATE MORE CODE FOR THE DIFFERENT CHARACTERS
        if character != ' ':
            cit += codeDict[character] + ' '                  
        else:               #1 SPACE INDICATES THAT THERE IS DIFFERENT CHARACRTERS
            cit += ' '      # 2 INDICATES DIFFERENT WORDS
    return cit

encryptInput = "HELLO-WORLD"
print(encryption(encryptInput))
