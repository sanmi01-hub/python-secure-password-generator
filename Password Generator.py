import secrets
import string
import random

def generate_password():
    print("=== Secure password generator ===")

    #Get password length
    while True:
        try:
            length = int(input("Enter your preferred password length (min 8 and max 30): "))
            if length < 8 or (length > 30):
                print("Password must be between 8-30 characters.\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number.\n")
    #User choices

    uppercase = input("Include uppercase letters? (y/n): ").lower()
    lowercase = input("Include lowercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    symbols = input("Include symbols? (y/n): ").lower()

    alphabet = ""
    required = []

    if uppercase == "y":
        alphabet += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if lowercase == "y":
        alphabet += string.ascii_lowercase
        required.append(secrets.choice(string.ascii_lowercase))
    if numbers == "y":
        alphabet += string.digits
        required.append(secrets.choice(string.digits))
    if symbols == "y":
        alphabet += string.punctuation
        required.append(secrets.choice(string.punctuation))

    #Check if user selected anything
    if alphabet == "":
        print("You must choose at least one character type.")
        return

    #Ensure password length is enough
    if length < len(required):
        print("\nPassword length is too short for the selected option.")
        return

    #Generate remaining characters
    remaining = length - len(required)
    password = required.copy()

    for _ in range(remaining):
        password.append(secrets.choice(alphabet))

    #Shuffle password so required characters aren't always first
    random.shuffle(password)

    #convert list to string
    final_password = "".join(password)
    return final_password

password = generate_password()

if password:
    print("\nGenerated password:")
    print(password)
    print('Password generated successfully.')
