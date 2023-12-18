from model.Employee.Abilities import Abilities


class Needs:
    def __init__(self):
        self.motivation = 100
        self.hunger = 25
        self.stress = 100
        self._abilities = Abilities()

    def eat(self):
        if self.hunger <= 100 - self._abilities.stomach:
            self.hunger += self._abilities.stomach
        else:
            self.hunger = 100

    def play(self):
        if self.stress <= 100 - self._abilities.anxiety:
            self.stress += self._abilities.anxiety
        else:
            self.stress = 100

    def meet(self):
        if self.motivation <= 100 - self._abilities.boredom:
            self.motivation += self._abilities.boredom

    def decrease_motivation(self):
        self.motivation -= self._abilities.boredom
        if self.motivation < 0:
            self.motivation = 0

    def decrease_stress(self):
        self.stress -= self._abilities.anxiety
        if self.stress < 0:
            self.stress = 0

    def decrease_hunger(self):
        self.hunger -= self._abilities.stomach
        if self.hunger < 0:
            self.hunger = 0
