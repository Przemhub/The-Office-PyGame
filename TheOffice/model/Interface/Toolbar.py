import math

import pygame.image
from pygame import image, Rect


class Toolbar:
    def __init__(self):
        self.image = image.load("../resources/interface/top.png")
        self.rect = Rect(20, 0, 1, 45)
        self.clk_pointer = (397, 15)
        self.radius = 35
        self.left_wing = Rect(20, -250, 322, 250)
        self.right_wing = Rect(457, -250, 322, 250)
        self.init_icons()

    def init_icons(self):
        self.calendar = pygame.image.load("../resources/interface/calendar.png")
        self.calendar_rect = Rect(270, 8, self.calendar.get_width(), self.calendar.get_height())

    def update_clock(self, theta):
        radiant = 2 * math.pi * theta / 360
        self.clk_pointer = (397 + (math.sin(radiant).real * self.radius), 55 - (math.cos(radiant).real * self.radius))

