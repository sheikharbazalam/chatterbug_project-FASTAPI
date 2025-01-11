import string
import random


def generate_password(length: int, include_special: bool = False, include_numbers: bool = True) -> str:
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    # Define the character set
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits if include_numbers else ""
    special_chars = string.punctuation if include_special else ""

    all_chars = lower_case + upper_case + numbers + special_chars

    if not all_chars:
        raise ValueError(
            "Password should include at least one type of character (letters, numbers, or special characters).")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password
