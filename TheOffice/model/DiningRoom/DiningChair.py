from pygame import Rect

from model.Furniture import Furniture


class DiningChair(Furniture):
    def __init__(self, x, y, room):
        Furniture.__init__(self)
        self.rect = Rect(x, y, 20, 37)
        self.room = room
