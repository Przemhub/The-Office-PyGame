from pygame import Surface


class InterfaceElement:
    def __init__(self, rect, image, on_click=None, on_hover=None):
        self.rect = rect
        self.image = image
        self.hover_surface = Surface(self.rect.size)
        self.hover_surface.set_alpha(128)
        self.hover_surface.fill((255, 255, 255))

        self._on_click = on_click
        self._on_hover = on_hover
        self.NO_EFFECT = 0
        self.DROP_SHADOW = 1
        self.hover_effect = self.NO_EFFECT

    def click(self):
        if self._on_click is not None:
            self._on_click()

    def hover(self, element):
        if self._on_hover is not None:
            self._on_hover(element)
