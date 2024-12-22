from pygame import image, transform

from model.Interface.InterfaceElement import InterfaceElement
from service.RoomType import RoomType


class BuildingElement(InterfaceElement):
    def __init__(self, rect, img, company):
        super().__init__(rect, img)
        self._company = company
        self._room_image_list = [
            transform.scale(image.load("../resources/rooms/office.png"), (220, 220)),
            transform.scale(image.load("../resources/rooms/dining_room.png"), (220, 220)),
            transform.scale(image.load("../resources/rooms/game_room.png"), (220, 220)),
            transform.scale(image.load("../resources/rooms/conference_room.png"), (220, 220)),
        ]
        self._room_cost_dict = {RoomType.OFFICE_ROOM: 1500, RoomType.DINING_ROOM: 1000, RoomType.GAME_ROOM: 1250,
                                RoomType.CONFERENCE_ROOM: 1000}
        self._room_index = 0

    def get_room_image(self):
        return self._room_image_list[self._room_index]

    def next_room(self):
        self._room_index += 1
        if self._room_index == len(self._room_image_list):
            self._room_index = 0

    def previous_room(self):
        self._room_index -= 1
        if self._room_index < 0:
            self._room_index = len(self._room_image_list) - 1

    def room_purchased(self):
        if self._company.money >= self._room_cost_dict.get(self._room_index):
            self._company.money -= self._room_cost_dict.get(self._room_index)
            return True
        else:
            return False
