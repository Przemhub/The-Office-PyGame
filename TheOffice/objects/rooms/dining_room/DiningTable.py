from pygame import Rect

from data.rooms.dining_room.DiningTable import DiningTableData


class DiningTable:
    def __init__(self, x, y):
        self._data = DiningTableData()
        self.rect = Rect(x, y, 40, 37)
