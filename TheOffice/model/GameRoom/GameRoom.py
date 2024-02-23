from pygame import image, Rect, mask

from model.GameRoom.GameSpot import GameSpot
from model.Room import Room


class GameRoom(Room):
    def __init__(self, y, room_board):
        Room.__init__(self, room_board[y])
        self.init_sprite(y)
        self.init_spots()

    def init_sprite(self, floor):
        self.image = image.load("../resources/rooms/game_room.png")
        self.mask = mask.from_surface(self.image)
        (x, y) = self.get_base_coordinates()
        self.rect = Rect(x, y - floor * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_spots(self):
        self.action_objects = [
            GameSpot(self.rect.x + 52, self.rect.y + 300, self),
            GameSpot(self.rect.x + 90, self.rect.y + 300, self),
            GameSpot(self.rect.x + 185, self.rect.y + 300, self),
            GameSpot(self.rect.x + 300, self.rect.y + 300, self),
        ]
