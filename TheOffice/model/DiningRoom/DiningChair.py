from pygame import Rect

from model.ActionObject import ActionObject


class DiningChair(ActionObject):
    def __init__(self, x, y, room):
        ActionObject.__init__(self)
        self.taken = False
        self.rect = Rect(x, y, 20, 37)
        self.room = room
