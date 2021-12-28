from model.DiningRoom.DiningRoom import DiningRoom
from model.OfficeRoom.OfficeRoom import OfficeRoom


class RoomSingleton:
    def __init__(self):
        self.room_board = {0: {}}

    def build_office(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception("board_pos[1] exceeded the actual number of floors", len(self.room_board))
        else:
            office = OfficeRoom(board_pos[0], board_pos[1], self.room_board)
            self.room_board[board_pos[1]][id(office)] = office

    def build_dining_room(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception("board_pos[1] exceeded the actual number of floors", len(self.room_board),
                            self.room_board)
        else:
            dining = DiningRoom(board_pos[0], board_pos[1], self.room_board)
            self.room_board[board_pos[1]][id(dining)] = dining
