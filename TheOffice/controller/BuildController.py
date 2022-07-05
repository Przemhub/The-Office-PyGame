from service.BuildingService import BuildingService


class BuildingController:
    def __init__(self):
        self.building_service = BuildingService()

    def get_building_service(self):
        return self.building_service

    def build_office(self, board_pos):
        self.building_service.build_office(board_pos)

    def build_dining_room(self, board_pos):
        self.building_service.build_dining_room(board_pos)

    def get_room_board(self):
        return self.building_service.room_board
