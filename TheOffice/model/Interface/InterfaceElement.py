class InterfaceElement:
    def __init__(self, rect, image, on_click=None):
        self.rect = rect
        self.image = image
        self._on_click = on_click

    def click(self):
        self._on_click()
