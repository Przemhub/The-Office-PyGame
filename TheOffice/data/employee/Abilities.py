import random


class Abilities:
    def __init__(self):
        self.stomach = random.randrange(5, 15)
        self.boredom = random.randrange(5, 10)
        self.anxiety = random.randrange(4, 20)
        # self.inteligence = random.randrange(5, 10)