from pygame import Rect, image

from model.ConferenceRoom.ConferenceChair import ConferenceChair
from model.Room import Room


class ConferenceRoom(Room):
    def __init__(self, board_pos, room_board):
        super().__init__(board_pos, room_board)
        self.init_sprite()
        self.init_tables()

    def init_sprite(self):
        self.image = image.load("../resources/rooms/conference_room.png")
        (x, y) = self.get_base_coordinates()
        self.rect = Rect(x, y - self.floor * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_tables(self):
        self.action_objects = [
            ConferenceChair(self.rect.x + 75,self.rect.y + 290,self),
            ConferenceChair(self.rect.x + 235, self.rect.y + 290,self)
        ]
