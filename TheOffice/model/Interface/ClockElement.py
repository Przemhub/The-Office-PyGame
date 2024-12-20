import math

from pygame import image, Rect

from model.Interface.InterfaceElement import InterfaceElement


class ClockElement(InterfaceElement):
    def __init__(self):
        super().__init__(Rect(20, 0, 1, 45), image.load("../resources/interface/top.png"))
        self.clk_pointer = (397, 15)
        self._radius = 35
        self.progress = 95

    def tick(self):
        self.progress = (self.progress + 1) % 100

    def get_progress_str(self):
        return str(self.progress)

    def update_clock(self, theta):
        radiant = 2 * math.pi * theta / 360
        self.clk_pointer = (397 + (math.sin(radiant).real * self._radius), 55 - (math.cos(radiant).real * self._radius))
