import random
from api import *

def randomize(arr):
    random.shuffle(arr)
    return arr

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()

    pp.pprint(randomize(getPay()))
