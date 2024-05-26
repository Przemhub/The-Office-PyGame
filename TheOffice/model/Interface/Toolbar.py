import math

import pygame.image
from pygame import image, Rect

from model.Interface.Icon import Icon
from model.Interface.Wing import Wing


class Toolbar:
    def __init__(self,calendar):
        self.image = image.load("../resources/interface/top.png")
        self.rect = Rect(20, 0, 1, 45)
        self.clk_pointer = (397, 15)
        self._radius = 35
        self.left_wing = Wing(20, -250, 322, 250)
        self.right_wing = Wing(457, -250, 322, 250)
        self.calendar = calendar
        self.init_icons()


    def init_icons(self):
        self.calendar_icon = Icon(pygame.image.load("../resources/interface/icons/calendar.png"),270,8)

    def update_clock(self, theta):
        radiant = 2 * math.pi * theta / 360
        self.clk_pointer = (397 + (math.sin(radiant).real * self._radius), 55 - (math.cos(radiant).real * self._radius))

