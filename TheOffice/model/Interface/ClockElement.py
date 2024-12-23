import math

from pygame import image, Rect

from model.Interface.StaticElement import StaticElement


class ClockElement(StaticElement):
    def __init__(self, rect, image):
        super().__init__(rect, image)
        self.clk_pointer = (397, 15)
        self._radius = 35
        self.progress = 0

    def tick(self):
        self.progress = (self.progress + 1) % 100

    def get_progress_str(self):
        return str(self.progress)

    def update_clock(self, theta):
        radiant = 2 * math.pi * theta / 360
        self.clk_pointer = (397 + (math.sin(radiant).real * self._radius), 55 - (math.cos(radiant).real * self._radius))
