import random

def generate_key():
    result = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return result