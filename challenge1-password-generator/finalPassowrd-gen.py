# importing modules for generating random characters and working with strings.
import random
import string

def generate_password(length=8):
    # Converting character categories to lists
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    # Combining all character categories into a single list
    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    # print(type(all_characters))

    # Ensure minimum password length
    if length < 8:
        length = 8


    # Shuffle the password to ensure randomness
    random.shuffle(all_characters)


    # Convert the all_characters list to a string
    password = ''.join(random.choices(all_characters, k=length))


    # Validating the password if it has atleast 1 upper, 1 lower, 1 digit and 1 symbol characters
    if (any(char.isupper() for char in password) and 
    any(char.islower() for char in password) and 
    any(char.isdigit() for char in password) and 
    any(char in string.punctuation for char in password)):
        return password

    # Returns a text if validation fails
    return "Invalid password, validation fails. Rerun the program!"

# calling the generate_password function with the provided length, and the resulting password 
# is stored in the password variable.

length = int(input("Enter your desired password length: "))

password = generate_password(length)
print("Generated password:", password)