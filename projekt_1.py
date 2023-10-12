"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: Lenka Pazourová
email: lenka.pazourova@seznam.cz
discord: LenkaP
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
registered_users = ['bob', 'ann', 'mike', 'liz']
users_passwords = {
                    'bob': '123', 
                    'ann': 'pass123', 
                    'mike': 'password123', 
                    'liz': 'pass123'
                    }
separator = '-' * 40

user = input("Username: ")
if user not in registered_users:
    print("Unregistered user. Terminating program..")

else:
    password = input("Password: ")
    if users_passwords.get(user) == password:
        print(separator)
        print(f"Welcome to the app, {user}\nWe have {len(TEXTS)} texts to be analyzed.")
        print(separator)
        text_choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
        if text_choice in range(1, (len(TEXTS)) + 1):
            text_list = TEXTS[text_choice - 1].split()
            titlecase = 0
            uppercase = 0
            lowercase = 0
            numeric = 0
            numeric_list = []
            for character in text_list:
                if character.istitle():
                    titlecase += 1
                elif character.isupper():
                    uppercase += 1
                elif character.islower():
                    lowercase += 1
                elif character.isnumeric(): 
                    numeric += 1
                    numeric_list.append(int(character))
            print(separator)
            print(f"There are {len(text_list)} words in the selected text.")
            print(f"There are {titlecase} titlecase words.")
            print(f"There are {uppercase} uppercase words.")
            print(f"There are {lowercase} lowercase words.")
            print(f"There are {numeric} numeric strings.")
            print(f"The sum of all the numbers {sum(numeric_list)}.")
            print(separator)
            print(("LEN| OCCURANCES\t|NR.").expandtabs(22))
            print(separator)
            
            len_words = []
            for words in text_list:
                len_words.append(len(words))
            
            for index in range(min(len_words), max(len_words) + 1):
                occurance = len_words.count(index)
                print((f"{str(index).ljust(2)} | {occurance * '*'}\t|{occurance}").expandtabs(22))
        else:
            print(separator)
            print("The number is out of range, terminating program..")
            print(separator)
    
    else: 
        print(separator)
        print("Wrong password, try again.")