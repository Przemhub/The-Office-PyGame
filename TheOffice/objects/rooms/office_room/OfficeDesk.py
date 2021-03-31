from data.rooms.office_room.OfficeDesk import OfficeDeskData
from pygame import Rect

class OfficeDesk:
    def __init__(self,x,y):
        self._data = OfficeDeskData()
        self.rect = Rect(x,y,40,37)