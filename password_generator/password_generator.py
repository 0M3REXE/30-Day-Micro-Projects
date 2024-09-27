import os
import string
import random
import pyperclip

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    banner = r"""
 ____    ____   _____ _____ __    __   ___   ____   ___         ____    ___  ____  
|    \  /    | / ___// ___/|  |__|  | /   \ |    \ |   \       /    |  /  _]|    \ 
|  o  )|  o  |(   \_(   \_ |  |  |  ||     ||  D  )|    \     |   __| /  [_ |  _  |
|   _/ |     | \__  |\__  ||  |  |  ||  O  ||    / |  D  |    |  |  ||    _]|  |  |
|  |   |  _  | /  \ |/  \ ||  `  '  ||     ||    \ |     |    |  |_ ||   [_ |  |  |
|  |   |  |  | \    |\    | \      / |     ||  .  \|     |    |     ||     ||  |  |
|__|   |__|__|  \___| \___|  \_/\_/   \___/ |__|\_||_____|    |___,_||_____||__|__|                                                                             
    """
    print(banner)

def ask_input():
    while True:
        clear_terminal()
        print("-" * 5, "Password Generator", "-" * 5)
        print("1. Characters, numbers, and special characters")
        print("2. Only characters, capital and small")
        print("3. Characters and numbers, without special characters")
        print("4. Exit")
        try:
            choice = int(input("Enter the number of your choice (1-4): "))
            if choice == 4:
                print("Exiting the program.")
                exit()
            elif choice < 1 or choice > 4:
                print("Choose the right number !!")
            else:
                return choice
        except ValueError:
            print("Please enter a valid integer.")
            input("Press Enter to continue...")

def password_generate(length, choice):
    try:
        if choice == 1:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(characters, k=length))
        elif choice == 2:
            characters = string.ascii_letters
            password = ''.join(random.choices(characters, k=length))
        elif choice == 3:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(f"Generated {len_pass} length password:", password)
        pyperclip.copy(password)  # Copy password to clipboard
        print("Password copied to clipboard!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

display_banner()
input("Press Enter to continue...")

choice = ask_input()

while True:
    len_pass = input("Enter the length of password (8 is default): ")
    if len_pass == '':
        len_pass = 8
    else:
        try:
            len_pass = int(len_pass)
        except ValueError:
            print("Please enter a valid integer.")
            continue
    if len_pass < 8 or len_pass > 16:
        print("The valid range is 8-16.")
    else:
        break

password_generate(len_pass, choice)
