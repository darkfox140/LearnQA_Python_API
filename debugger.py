import random
import string


def random_string(length):
    symbols = string.ascii_lowercase
    return "".join([random.choice(symbols) for e in range(length)])


print(random_string(1))