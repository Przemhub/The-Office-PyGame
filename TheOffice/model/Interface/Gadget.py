class Gadget:
    def __init__(self, rect, image):
        self.rect = rect
        self.image = image

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
