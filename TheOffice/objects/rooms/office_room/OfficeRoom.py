from pygame import sprite, image, mask
from pygame.rect import Rect

from objects.rooms.Room import Room
from data.rooms.office_room.OfficeRoom import OfficeRoomData
from objects.rooms.office_room.OfficeDesk import OfficeDesk


class OfficeRoom(Room):
    def __init__(self, x, y, id):
        self.id = id
        self.init_sprite(x, y)
        self.init_desks()
        self._data = OfficeRoomData(list(map(lambda desk: desk._data, self.action_objects)))

    def init_sprite(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("resources/rooms/office.png")
        self.mask = mask.from_surface(self.image)
        self.rect = Rect(x * self.image.get_width(), 230 - y * self.image.get_height(), self.image.get_width(),
                         self.image.get_height())

    def init_desks(self):
        self.action_objects= [
            OfficeDesk(self.rect.x + 35, self.rect.y + 300),
            OfficeDesk(self.rect.x + 120, self.rect.y + 300),
            OfficeDesk(self.rect.x + 200, self.rect.y + 300),
            OfficeDesk(self.rect.x + 275, self.rect.y + 300)
        ]
