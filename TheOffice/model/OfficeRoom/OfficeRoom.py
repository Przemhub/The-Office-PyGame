from pygame import image, mask
from pygame.rect import Rect

from model.OfficeRoom.OfficeDesk import OfficeDesk
from model.Room import Room


class OfficeRoom(Room):
    def __init__(self, board_pos, room_board):
        Room.__init__(self, board_pos, room_board)
        self.init_sprite()
        self.init_desks()

    def init_sprite(self):
        self.image = image.load("../resources/rooms/office.png")
        self.mask = mask.from_surface(self.image)
        (x, y) = self.get_base_coordinates()
        self.rect = Rect(x, y - self.floor * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_desks(self):
        self.action_objects = [
            OfficeDesk(self.rect.x + 35, self.rect.y + 300, self),
            OfficeDesk(self.rect.x + 120, self.rect.y + 300, self),
            OfficeDesk(self.rect.x + 200, self.rect.y + 300, self),
            OfficeDesk(self.rect.x + 275, self.rect.y + 300, self)
        ]
