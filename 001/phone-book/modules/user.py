SUGGEST_INPUT = [
    "What is your duty?", 
    "How it's goin'?",
    "Cheers!🥂",
    "Oh.. Let's go!",
    "I'm waitin' for",
    ]


import random
import re

def get_action_number():
    flag =  True
    pattern = "^[0-8]$"
    while flag:
        # Range 0, 1, 2, 3, 4
        random_suggest = random.randrange(0, len(SUGGEST_INPUT))
        action = input(f"{SUGGEST_INPUT[random_suggest]} > ")
        if bool(re.search(pattern, action)):
            flag = False     
        else:
            print("You need to type a number 1-8 or 0 to exit")
    return int(action)
 
def get_answer_to(message):
    print()
    print(message)
    print("Type «Y» to say «YES» or smth. else to «NO»")
    answer = input("Answer > ").lower()
    if answer == 'y':
        return True
    return False

def get_phone_number(message):
    flag =  True
    pattern = "^[0-9]+$"
    while flag:
        phone_number = input(f"{message} > ")
        if bool(re.search(pattern, phone_number)):
            flag = False     
        else:
            print("You need to type only numbers like 0-9")
    return phone_number