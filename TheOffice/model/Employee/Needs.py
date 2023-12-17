from model.Employee.Abilities import Abilities


class Needs:
    def __init__(self):
        self.motivation = 100
        self.hunger = 25
        self.stress = 100
        self._abilities = Abilities()

    def eat(self):
        if self.hunger < 90:
            self.hunger += self._abilities.stomach
        else:
            self.hunger = 100

    def play(self):
        if self.stress < 90:
            self.stress += self._abilities.anxiety
        else:
            self.stress = 100

    def decrease_motivation(self):
        self.motivation -= self._abilities.boredom

    def increase_stress(self):
        self.stress -= self._abilities.anxiety

    def increase_hunger(self):
        self.hunger -= self._abilities.stomach
        if self.hunger < 0:
            self.hunger = 0
