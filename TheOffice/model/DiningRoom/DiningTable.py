from pygame import Rect


class DiningTable:
    def __init__(self, x, y):
        self.taken = [False, False]
        self.rect = Rect(x, y, 20, 37)
