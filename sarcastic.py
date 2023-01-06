import random

def exclamation_convert(single_letter: str):
    what_is = random.randint(1, 2)
    if what_is == 1:
        return "1"
    return "!"

def sArCaStIc(normal_case: str):
    index = 0
    sarcastic = ""
    for letter in normal_case:
        if letter == "!":
            letter = exclamation_convert(letter)
        if index % 2 == 0:
            sarcastic += letter.lower()
            index += 1
        elif index % 2 != 0:
            sarcastic += letter.upper()
            index += 1
 
    print(sarcastic)

what_to_say = input("Type something: ")
print()
sArCaStIc(what_to_say)


# Completely random rather than alternating lower/upper
# Comment this out, create new file for psychotic.py

"""
import random

def sArCaStIc(normal_case: str):
    sarcastic = ""

    for char in normal_case:
        rando_char = random.randint(1, 2)
        if char == "!":
            if rando_char == 1:
                sarcastic += "1"
            if rando_char == 2:
                sarcastic += "!"
        elif rando_char == 1:
            sarcastic += char.upper()
        else:
            sarcastic += char.lower()
    
    return sarcastic

what_to_say = input("Type something: ")
print()
print(sArCaStIc(what_to_say))
"""

