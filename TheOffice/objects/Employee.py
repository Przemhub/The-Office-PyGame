from sys import maxsize
from pygame import sprite, mask,image
from pygame.rect import Rect

from data.employee.Employee import EmployeeData


class EmployeeObject(sprite.Sprite):
    def __init__(self,x,y,name,company):
        self._data = EmployeeData(name, company)
        self.init_sprite(x,y)


    def init_sprite(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = image.load("resources/employees/employee.png")
        self.mask = mask.from_surface(self.image)
        self.rect = Rect(x,y,self.image.get_width(),self.image.get_height())

    # def look_for_room(self,rooms):
    #     scope = Rect(self.rect.x,self.rect.y,rooms[0].rect.width,rooms[0].rect.height)
    #     room_in_scope = Rect(maxsize,maxsize,0,0)
    #     for room in rooms:
    #         if scope.colliderect(room) and room_in_scope.x > room.rect.x:
    #             room_in_scope


