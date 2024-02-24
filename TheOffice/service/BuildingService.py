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
        self.validate_board_pos(board_pos)
        if board_pos[0] == len(self.room_board[board_pos[1]]):
            office = OfficeRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]].append(office)
        else:
            office = OfficeRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]][board_pos[0]] = office

    def build_dining_room(self, board_pos):
        self.validate_board_pos(board_pos)
        if board_pos[0] == len(self.room_board[board_pos[1]]):
            dining_room = DiningRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]].append(dining_room)
        else:
            dining_room = DiningRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]][board_pos[0]] = dining_room


    def build_game_room(self, board_pos):
        self.validate_board_pos(board_pos)
        if board_pos[0] == len(self.room_board[board_pos[1]]):
            game_room = GameRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]].append(game_room)
        else:
            game_room = GameRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]][board_pos[0]] = game_room

    def build_conference_room(self, board_pos):
        self.validate_board_pos(board_pos)
        if board_pos[0] == len(self.room_board[board_pos[1]]):
            conference_room = ConferenceRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]].append(conference_room)
        else:
            conference_room = ConferenceRoom(board_pos, self.room_board)
            self.room_board[board_pos[1]][board_pos[0]] = conference_room

    def build_corridor(self, board_pos):
        self.validate_board_pos(board_pos)
        if board_pos[0] == len(self.room_board[board_pos[1]]):
            corridor = Corridor(board_pos, self.room_board)
            self.room_board[board_pos[1]].append(corridor)
        else:
            corridor = Corridor(board_pos, self.room_board)
            self.room_board[board_pos[1]][board_pos[0]] = corridor

    def validate_board_pos(self, board_pos):
        if board_pos[1] >= len(self.room_board):
            raise Exception(board_pos[1], "exceeded the actual number of floors to build on:", len(self.room_board))
        elif board_pos[0] > len(self.room_board[board_pos[1]]):
            raise Exception(board_pos[0], "exceeded the actual number of rooms to build:", len(self.room_board[board_pos[1]]))