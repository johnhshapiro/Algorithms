import time
import math

class RandGen():
    """Class that generates a sequence of 'random' numbers
    """
    def __init__(self):
        self.seed = int(str(time.time())[-3:].replace('.',''))

    def generate_random(self):
        self.seed = 7 * self.seed % 101
        return (self.seed -1) % 10 + 1

if __name__ == '__main__':
    random = RandGen()
    for i in range(100):
        print(random.generate_random())