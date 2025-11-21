import random
import string
import datetime

def generate_index_number(full_name):
    """
    Generates an index number using:
    - First 3 letters of full_name in uppercase
    - 5 random digits
    - 2 digits of the current year
    Example: "Ama Serwaa" -> "AMA1234525"
    """
    prefix = full_name[:3].upper()
    digits = ''.join(random.choices(string.digits, k=5))
    x=datetime.datetime.now()
    year=x.strftime("%y")
    return f"{prefix}{digits}{year}"
