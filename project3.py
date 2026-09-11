import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length
    all_chars = lower + upper + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the password so it's random
    random.shuffle(password)

    return "".join(password)

# Take input from user
length = int(input("Enter password length: "))

# Generate and print password
print("Generated Password:", generate_password(length))
