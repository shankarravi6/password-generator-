import random

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the length of the password is at least 8 characters
    length = max(length, 8)

    # Generate a random password using the selected character sets
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Prompt the user for the desired password length
    password_length = int(input("Enter the desired password length: "))

    # Generate and print the password
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
