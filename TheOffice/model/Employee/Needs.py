from model.Employee.Abilities import Abilities


class Needs():
    def __init__(self):
        self.motivation = 100
        self.hunger = 50
        self.stress = 100
        self._abilities = Abilities()

    def decrease_needs(self):
        self.motivation -= self._abilities.boredom
        self.hunger -= self._abilities.stomach
        self.stress -= self._abilities.anxiety

    def is_hungry(self):
        return self.hunger <= 0

    def is_stressed(self):
        return self.stress <= 0

    def is_motivated(self):
        return self.motivation <= 0