from pygame import Rect

from model.Furniture import Furniture


class ConferenceChair(Furniture):
    def __init__(self, x, y, room):
        Furniture.__init__(self)
        self.rect = Rect(x, y, 25, 42)
        self.room = room
