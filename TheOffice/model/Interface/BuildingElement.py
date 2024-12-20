from pygame import image, transform

from model.Interface.InterfaceElement import InterfaceElement


class BuildingElement(InterfaceElement):
    def __init__(self, rect, img):
        super().__init__(rect, img)
        self.room_image_list = [
            transform.scale(image.load("../resources/rooms/office.png"), (220, 220)),
            transform.scale(image.load("../resources/rooms/dining_room.png"), (220, 220)),
            transform.scale(image.load("../resources/rooms/game_room.png"), (220, 220)),
            transform.scale(image.load("../resources/rooms/conference_room.png"), (220, 220)),
        ]
        self.room_index = 0

    def get_room_image(self):
        return self.room_image_list[self.room_index]
