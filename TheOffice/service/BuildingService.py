from model.ConferenceRoom.ConferenceRoom import ConferenceRoom
from model.Corridor.Corridor import Corridor
from model.DiningRoom.DiningRoom import DiningRoom
from model.GameRoom.GameRoom import GameRoom
from model.OfficeRoom.OfficeRoom import OfficeRoom


class BuildingService:
    def __init__(self):
        self.room_board = [[]]
        self.corridors = []

    def build_floor(self):
        self.room_board[len(self.room_board)] = []

    # board_pos(x,y)
    # board_pos[x] - order of the room in a row
    # board_pos[y] - floor
    def build_office(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception(board_pos[1], "exceeded the actual number of floors to build on:", len(self.room_board))
        else:
            office = OfficeRoom(board_pos[0], board_pos[1], self.room_board)
            self.room_board[board_pos[1]].insert(board_pos[0], office)

    def build_dining_room(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception(board_pos[1], "exceeded the actual number of floors to build on:", len(self.room_board),
                            self.room_board)
        else:
            dining = DiningRoom(board_pos[1], self.room_board)
            self.room_board[board_pos[1]].insert(board_pos[0], dining)

    def build_game_room(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception("board_pos[1] exceeded the actual number of floors", len(self.room_board),
                            self.room_board)
        else:
            gaming = GameRoom(board_pos[1], self.room_board)
            self.room_board[board_pos[1]].insert(board_pos[0], gaming)

    def build_conference_room(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception("board_pos[1] exceeded the actual number of floors", len(self.room_board),
                            self.room_board)
        else:
            conference = ConferenceRoom(board_pos[1], self.room_board)
            self.room_board[board_pos[1]].insert(board_pos[0], conference)

    def build_corridor(self, board_pos):
        self.corridors.append(Corridor(board_pos[1]))