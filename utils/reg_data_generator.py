import random
import string


def generate_email():
    numbers = random.choices(string.digits, k=8)
    suffix = "".join(numbers)
    email = f"test_{suffix}@test.com"
    return email

def generate_password():
    letters_lower = random.choices(string.ascii_lowercase, k=4)
    letters_upper = random.choices(string.ascii_uppercase, k=2)
    symbols = random.choices('!@#$%^&*', k=2)
    numbers = random.choices(string.digits, k=4)
    password = letters_lower + letters_upper + symbols + numbers
    random.shuffle(password)
    return "".join(password)

def generate_first_name():
    first_names = ["John", "Emma", "Olivia", "Liam", "Noah", "Ava"]
    return random.choice(first_names)

def generate_last_name():
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson"]
    return random.choice(last_names)
