from pygame import image, Rect


class Toolbar:
    def __init__(self):
        self.image = image.load("../resources/interface/top.png")
        self.rect = Rect(20, 0, 1, 1)
