#! python3
import re

password = input("Please input the password to check if it is strong:\n")

strong = True
if len(password) < 8:
    strong = False
    
if not re.search(r'\d', password): # if not any(char.isdigit() for char in password): # these are same
    strong = False
if not re.search(r'[a-z]', password): # if not any(char.islower() for char in password): # these are same
    strong = False
if not re.search(r'[A-Z]', password): # if not any(char.isupper() for char in password): # these are same
    strong = False

if strong:
    print('Your password is strong since it is at least 8 characters long and has at least one digit, a lowercase letter, and a capital letter.')    
else:
    print('Your password is NOT strong since it is NOT at least 8 characters long or has at least one digit, a lowercase letter, or a capital letter.')    
