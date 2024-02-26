from pygame import Rect, image

from model.Room import Room


class Corridor(Room):
    def __init__(self, board_pos, room_board):
        super().__init__(board_pos, room_board)
        self.init_sprite()

    def init_sprite(self):
        self.image = image.load("../resources/rooms/corridor.png")
        (x, y) = self.get_base_coordinates()
        self.rect = Rect(x, y, self.image.get_width(),
                         self.image.get_height())