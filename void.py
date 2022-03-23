import random
from grab_pay import *

def randomize(arr):
    random.shuffle(arr)
    return arr

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()

    pp.pprint(randomize(getPay()))
