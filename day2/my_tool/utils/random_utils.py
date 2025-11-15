import random 
import string

def random_id(length=8):
    """
    Generates a random alphanumeric ID

    """
    chars=string.ascii_letters+string.digits
    return "".join(random.choices(chars,k=length))

def random_user():
    """
    Generates a random user profile 
    """
    names=["Alice","Bob","Charlie","Diana","Eve","Frank"]
    return{
        "id":random_id(10),
        "name":random.choice(names),
        "age": random.randint(18,60)
    }
