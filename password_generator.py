import random

def generate_password(length=12):
    
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":

    password_length = int(input("Enter the desired password length: "))

    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
