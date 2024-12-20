import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password must be at least 6 characters.")
    chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
    ] + random.choices(chars, k=length - 2)
    random.shuffle(password)
    return ''.join(password)

# Example usage
length = int(input("Enter password length: "))
print("Generated password:", generate_password(length))