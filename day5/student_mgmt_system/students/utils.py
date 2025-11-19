import random
import string

def generate_index_number(full_name):
    """
    Generates an index number using:
    - First 3 letters of full_name in uppercase
    - 7 random digits
    Example: "Ama Serwaa" -> "AMA1234567"
    """
    prefix = full_name[:3].upper()
    digits = ''.join(random.choices(string.digits, k=7))
    return f"{prefix}{digits}"
