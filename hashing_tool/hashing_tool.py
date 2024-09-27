import os
import hashlib

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_input():
    while True:
        clear_terminal()
        print("-" * 5, "Hashing Tool", "-" * 5)
        print("1. MD5 Hash")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. Exit")
        try:
            choice = int(input("Enter your Choice: "))
            if choice == 4:
                print("Exiting the program.")
                exit()
            elif choice < 1 or choice > 4:
                print("Choose the right number!")
                input("Enter to continue...")
            else:
                return choice
        except ValueError:
            print("Enter the right value")
            input("Enter to continue... ")

def hashing(phrase, choice):
    try:
        if choice == 1:
            hashed = hashlib.md5(phrase.encode('utf-8')).hexdigest()
            print("The MD5 hash is:\n")
            print(hashed)
        elif choice == 2:
            hashed = hashlib.sha1(phrase.encode('utf-8')).hexdigest()
            print("The SHA-1 hash is:\n")
            print(hashed)
        elif choice == 3:
            hashed = hashlib.sha256(phrase.encode('utf-8')).hexdigest()
            print("The SHA-256 hash is:\n")
            print(hashed)
    except Exception as e:
        print(f"Error: {e}")

while True:
    choice = ask_input()
    Ph_hash = input("Enter the phrase to hash: ")
    hashing(Ph_hash, choice)
    input("Press Enter to continue...")
