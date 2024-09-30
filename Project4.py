import random
import string
import pyperclip  

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    print(random.choice(characters) for i in range(length))
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Welcome to my Random Password Generator!")
length = int(input("Enter desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
password = generate_password(length, use_uppercase, use_numbers, use_symbols)
print(f"Generated Password: {password}")
copy = input("Copy password to clipboard? (y/n): ").lower()
if copy == 'y':
    pyperclip.copy(password)
    print("Password copied to clipboard!")


