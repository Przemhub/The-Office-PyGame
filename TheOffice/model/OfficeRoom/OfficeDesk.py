from pygame import Rect

class OfficeDesk:
    def __init__(self,x,y):
        self.taken = False
        self.rect = Rect(x,y,40,37)

