from pygame import Rect, image


class Corridor:
    def __init__(self, floor):
        self.image = image.load("../resources/rooms/corridor.png")
        self.rect = Rect(0, 230 - floor * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())