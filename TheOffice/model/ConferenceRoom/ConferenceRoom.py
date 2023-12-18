from pygame import Rect, mask, image

from model.ConferenceRoom.ConferenceChair import ConferenceChair
from model.Room import Room


class ConferenceRoom(Room):
    def __init__(self, y, room_board):
        Room.__init__(self)
        self.neighbour_rooms = room_board[y]
        self.init_sprite(y)
        self.init_tables()

    def init_sprite(self, y):
        self.image = image.load("../resources/rooms/conference_room.png")
        self.mask = mask.from_surface(self.image)
        x = 0
        for room in self.neighbour_rooms.values():
            x += room.image.get_width()
        self.rect = Rect(x, 230 - y * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_tables(self):
        self.action_objects = [
            ConferenceChair(self.rect.x + 75,self.rect.y + 290,self),
            ConferenceChair(self.rect.x + 235, self.rect.y + 290,self)
        ]
