from pygame import sprite, image, mask
from pygame.rect import Rect

from model.DiningRoom.DiningTable import DiningTable


class DiningRoom(sprite.Sprite):
    def __init__(self, y, room_board):
        sprite.Sprite.__init__(self)
        self.neighbour_rooms = room_board[y]
        self.action_objects = []
        self.init_sprite(y)
        self.init_tables()

    def init_sprite(self, y):
        self.image = image.load("../resources/rooms/dining_room.png")
        self.mask = mask.from_surface(self.image)
        x = 0
        for room in self.neighbour_rooms.values():
            x += room.image.get_width()
        self.rect = Rect(x, 230 - y * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_tables(self):
        self.action_objects = [
            DiningTable(self.rect.x + 35, self.rect.y + 300),
            DiningTable(self.rect.x + 120, self.rect.y + 300),
            DiningTable(self.rect.x + 140, self.rect.y + 300),
            DiningTable(self.rect.x + 227, self.rect.y + 300),
            DiningTable(self.rect.x + 250, self.rect.y + 300),
            DiningTable(self.rect.x + 340, self.rect.y + 300),
            DiningTable(self.rect.x + 365, self.rect.y + 300),
            DiningTable(self.rect.x + 454, self.rect.y + 300),
        ]
