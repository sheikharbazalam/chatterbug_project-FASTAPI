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
