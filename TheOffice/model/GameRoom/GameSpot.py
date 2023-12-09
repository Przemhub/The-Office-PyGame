from pygame import Rect

from model.Furniture import Furniture


class GameSpot(Furniture):
    def __init__(self,x,y, room):
        Furniture.__init__(self)
        self.taken = False
        self.rect = Rect(x,y,40,37)
        self.room = room