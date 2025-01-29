import string
import random


def generate_password(length: int, include_special: bool, include_numbers: bool) -> str:
    """
    Generate a secure password with customizable options.
    """
    if not (12 <= length <= 128):
        raise ValueError(
            "Password length must be between 12 and 128 characters.")

    if not (include_special or include_numbers):
        raise ValueError(
            "At least one character type must be selected.")
    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_special:
        chars += string.punctuation

    # if length < 12 or length > 128:
     #   raise ValueError(
      #      "Password length must be between 12 and 128 characters.")
    print(''.join(random.choices(chars, k=length)))

    return ''.join(random.choices(chars, k=length))


def check_password_strength(password: str) -> str:
    """
     Check the strength of a given password and return its rating.
    - Weak: Length < 12 or lacks variety (only letters, no numbers/special characters).
    - Moderate: Length >= 12, includes 2 of 3 character types (letters, numbers, special chars).
    - Strong: Length >= 12 and includes all 3 character types.
    """
    if len(password) < 12:
        return "Weak"

    strength = 0
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 4:
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    else:
        return "Weak"
