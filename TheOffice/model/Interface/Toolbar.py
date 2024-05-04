import math

from pygame import image, Rect


class Toolbar:
    def __init__(self):
        self.image = image.load("../resources/interface/top.png")
        self.rect = Rect(20, 0, 1, 1)
        self.clk_pointer = (397, 15)
        self.radius = 40

    def update_clock(self, theta):
        radiant = 2 * math.pi * theta / 360
        self.clk_pointer = (397 + (math.sin(radiant).real * self.radius), 55 - (math.cos(radiant).real * self.radius))
