from pygame import Rect

from model.Furniture import Furniture


class Elevator(Furniture):
    def __init__(self, x, y, room):
        Furniture.__init__(self)
        self.rect = Rect(x, y, 40, 100)
        self.room = room
