from pygame import sprite


class Room(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.action_objects = []

    def is_free(self):
        for action_obj in self.action_objects:
            if action_obj.taken == False:
                return True
        return False