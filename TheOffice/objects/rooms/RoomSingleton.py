from objects.rooms.dining_room.DiningRoom import DiningRoom
from objects.rooms.office_room.OfficeRoom import OfficeRoom


class RoomSingleton:
    def __init__(self):
        self.room_board = [[]]

    def build_office(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            if board_pos[1] > len(self.room_board) + 1:
                raise Exception("board_pos[1] exceeded the actual number of floors", len(self.room_board))
            else:
                self.room_board.append([OfficeRoom(board_pos[0], board_pos[1], len(self.room_board))])
        else:
            self.room_board[board_pos[1]].append(OfficeRoom(board_pos[0], board_pos[1], len(self.room_board)))

    def build_dining_room(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            if board_pos[1] > len(self.room_board) + 1:
                raise Exception("board_pos[1] exceeded the actual number of floors", len(self.room_board),
                                self.room_board)
            else:
                self.room_board.append([DiningRoom(board_pos[0], board_pos[1],
                                                   len(self.room_board[len(self.room_board) - 1]), self.room_board)])
        else:
            self.room_board[board_pos[1]].append(
                DiningRoom(board_pos[0], board_pos[1], len(self.room_board[len(self.room_board) - 1]), self.room_board))
