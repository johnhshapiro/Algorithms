import time
import math

class RandGen():

    def __init__(self):
        self.seed = time.time()

    def generate_random(self):
        digit = int(str(seed)[-1])
        print(digit)
        number = int(str(int(str(seed)[-1])/math.e)[1])
        return number