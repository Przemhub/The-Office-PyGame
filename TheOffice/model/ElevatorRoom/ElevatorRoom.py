from pygame import image, Rect

from model.ElevatorRoom.Elevator import Elevator
from model.Room import Room


class ElevatorRoom(Room):
    def __init__(self, board_pos, room_board):
        super().__init__(board_pos, room_board)
        self.init_sprite()
        self.init_tables()

    def init_sprite(self):
        self.image = image.load("../resources/rooms/elevator_room.png")
        (x, y) = self.get_base_coordinates()
        self.rect = Rect(x, y, self.image.get_width(),
                         self.image.get_height())

    def init_tables(self):
        self.action_objects = [
            Elevator(self.rect.x + 130, self.rect.y + 250, self)
        ]