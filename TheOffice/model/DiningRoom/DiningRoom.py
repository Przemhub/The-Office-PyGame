from pygame import sprite, image, mask
from pygame.rect import Rect

from model.DiningRoom.DiningChair import DiningChair
from model.Room import Room


class DiningRoom(Room):
    def __init__(self, board_pos, room_board):
        Room.__init__(self, board_pos, room_board)
        self.init_sprite()
        self.init_tables()

    def init_sprite(self):
        self.image = image.load("../resources/rooms/dining_room.png")
        self.mask = mask.from_surface(self.image)
        (x, y) = self.get_base_coordinates()
        self.rect = Rect(x, y - self.floor * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_tables(self):
        self.action_objects = [
            DiningChair(self.rect.x + 35, self.rect.y + 300, self),
            DiningChair(self.rect.x + 120, self.rect.y + 300, self),
            DiningChair(self.rect.x + 220, self.rect.y + 300, self),
            DiningChair(self.rect.x + 315, self.rect.y + 300, self)
        ]
