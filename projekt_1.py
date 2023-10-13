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

users_passwords = {
                    'bob': '123', 
                    'ann': 'pass123', 
                    'mike': 'password123', 
                    'liz': 'pass123'
                    }
separator = '-' * 40

user = input("Username: ")
if user not in users_passwords.keys():
    print(separator)
    print("Unregistered user. Terminating program..")
    print(separator)

else:
    password = input("Password: ")
    if users_passwords.get(user) == password:
        print(separator)
        print(f"Welcome to the app, {user}\nWe have {len(TEXTS)} texts to be analyzed.")
        print(separator)
        text_choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
        
        # analyze user chooice text
        if int(text_choice) in range(1, (len(TEXTS)) + 1):
            text_list = TEXTS[(int(text_choice)) - 1].split()
            titlecase = 0
            uppercase = 0
            lowercase = 0
            numeric = 0
            numeric_sum = 0
            for character in text_list:
                if character.istitle():
                    titlecase += 1
                elif character.isupper():
                    uppercase += 1
                elif character.islower():
                    lowercase += 1
                elif character.isnumeric(): 
                    numeric += 1
                    numeric_sum += int(character)
            print(separator)
            print(f"There are {len(text_list)} words in the selected text.")
            print(f"There are {titlecase} titlecase words.")
            print(f"There are {uppercase} uppercase words.")
            print(f"There are {lowercase} lowercase words.")
            print(f"There are {numeric} numeric strings.")
            print(f"The sum of all the numbers {numeric_sum}.")
            print(separator)
            print(("LEN| OCCURANCES\t|NR.").expandtabs(23))
            print(separator)
            
            # len words chart
            clear_text = []
            len_occurance = {}
            for one_word in text_list:
                clear_text.append(len(one_word.strip(',.')))
            
            for number in clear_text:
                if number not in len_occurance:
                    len_occurance[number] = 1
                else:
                    len_occurance[number] = len_occurance[number] + 1
            
            for key, value in sorted(len_occurance.items()):
                print((f"{str(key).ljust(2)} | {value * '*'}\t|{value}").expandtabs(23))

        elif int(text_choice) > len(TEXTS):
            print(separator)
            print("The number is out of range, terminating program..")
            print(separator)
        
        elif int(text_choice) < 1:
            print(separator)
            print("The number is out of range, terminating program..")
            print(separator)
        
    else: 
        print(separator)
        print("Wrong password, try again.")