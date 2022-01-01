from pygame import sprite, image, mask
from pygame.rect import Rect

from model.OfficeRoom.OfficeDesk import OfficeDesk


class OfficeRoom(sprite.Sprite):
    def __init__(self, x, y, room_board):
        self.neighbour_rooms = room_board[y]
        sprite.Sprite.__init__(self)
        self.action_objects = []
        self.init_sprite(y)
        self.init_desks()

    def init_sprite(self, y):
        self.image = image.load("../resources/rooms/office.png")
        self.mask = mask.from_surface(self.image)
        x = 0
        for room in self.neighbour_rooms.values():
            x += room.image.get_width()
        self.rect = Rect(x, 230 - y * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())


    def init_desks(self):
        self.action_objects = [
            OfficeDesk(self.rect.x + 35, self.rect.y + 300),
            OfficeDesk(self.rect.x + 120, self.rect.y + 300),
            OfficeDesk(self.rect.x + 200, self.rect.y + 300),
            OfficeDesk(self.rect.x + 275, self.rect.y + 300)
        ]
