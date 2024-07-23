import random
import string

def generate_password(length):
    # Define all possible characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Get desired password length from user
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Length must be greater than zero. Please enter again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Generate and print the password
password = generate_password(length)
print("Generated password:", password)
