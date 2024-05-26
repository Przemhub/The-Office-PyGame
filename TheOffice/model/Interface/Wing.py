from pygame import Rect


class Wing:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.gadget = None  # this could be calendar, employee hiring window, buying room window
        # It's set in the mousecontroller during mouse press event on icon

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
