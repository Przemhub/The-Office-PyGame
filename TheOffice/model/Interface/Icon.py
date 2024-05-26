from pygame import Rect


class Icon:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = Rect(x, y, image.get_width(), image.get_height())
