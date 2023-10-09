"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: Lenka Pazourová
email: lenka.pazourova@seznam.cz
discord: LenkaP
"""

import task_template
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
        print(f"Welcome to the app, {user}\nWe have 3 texts to be analyzed.")
        print(separator)
    
    else: 
        print("Wrong password, try again.")