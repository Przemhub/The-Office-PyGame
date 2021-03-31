from pygame import sprite, image, mask
from pygame.rect import Rect

from data.rooms.dining_room.DiningRoom import DiningRoomData
from objects.rooms.Room import Room
from objects.rooms.dining_room.DiningTable import DiningTable


class DiningRoom(Room):
    def __init__(self, x, y,id, room_array):
        self.room_array = room_array
        self.id = id
        self.init_sprite(x,y)
        self.init_tables()
        self._data = DiningRoomData(list(map(lambda table:table._data,self.tables)))

    def init_sprite(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("resources/rooms/dining_room.png")
        self.mask = mask.from_surface(self.image)
        x = 0
        y = 0
        for room in self.room_array:
            x
        self.rect = Rect(x * self.image.get_width(), 230 - y * self.image.get_height(), self.image.get_width(), self.image.get_height())


    def init_tables(self):
        self.tables = [
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 35, self.rect.y + 300),
        ]