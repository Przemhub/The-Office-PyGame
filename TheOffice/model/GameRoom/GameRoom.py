from pygame import image, Rect, mask

from model.GameRoom.GameSpot import GameSpot
from model.Room import Room


class GameRoom(Room):
    def __init__(self, y, room_board):
        Room.__init__(self)
        self.neighbour_rooms = room_board[y]
        self.init_sprite(y)
        self.init_spots()


    def init_sprite(self, y):
        self.image = image.load("../resources/rooms/game_room.png")
        self.mask = mask.from_surface(self.image)
        x = 0
        for room in self.neighbour_rooms.values():
            x += room.image.get_width()
        self.rect = Rect(x, 230 - y * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())


    def init_spots(self):
        self.action_objects = [
            GameSpot(self.rect.x + 35, self.rect.y + 300, self),
            GameSpot(self.rect.x + 120, self.rect.y + 300, self),
            GameSpot(self.rect.x + 140, self.rect.y + 300, self),
            GameSpot(self.rect.x + 227, self.rect.y + 300, self),
            GameSpot(self.rect.x + 250, self.rect.y + 300, self),
            GameSpot(self.rect.x + 340, self.rect.y + 300, self),
            GameSpot(self.rect.x + 365, self.rect.y + 300, self),
            GameSpot(self.rect.x + 454, self.rect.y + 300, self),
        ]