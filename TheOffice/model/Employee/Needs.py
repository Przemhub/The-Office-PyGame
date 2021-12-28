from model.Employee.Abilities import Abilities


class Needs:
    def __init__(self):
        self.motivation = 100
        self.hunger = 100
        self.stress = 100
        self._abilities = Abilities()

    def eat(self):
        if self.hunger < 90:
            self.hunger += self._abilities.stomach * 2
        else:
            self.hunger = 100

    def decrease_motivation(self):
        self.motivation -= self._abilities.boredom

    def increase_stress(self):
        self.stress -= self._abilities.anxiety

    def increase_hunger(self):
        self.hunger -= self._abilities.stomach

    def is_hungry(self):
        return self.hunger <= 0

    def is_stressed(self):
        return self.stress <= 0

    def is_motivated(self):
        return self.motivation <= 0
