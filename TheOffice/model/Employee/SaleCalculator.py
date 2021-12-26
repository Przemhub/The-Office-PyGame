class SaleCalculator:
    def __init__(self,needs,stats):
        self._stats = stats
        self._needs = needs
        self.init_const()

    def init_const(self):
        self.hunger_const = self._needs.hunger
        self.stress_const = self._needs.stress
        self.motivation_const = self._needs.motivation

    def calculate_sale(self):
        return int((self._stats.base + self.P()) * self.M() * self.H() * self.S())

    def M(self):
        M = int(self._needs.motivation / (self.motivation_const/3))
        if M == 0:
            return 1
        return M

    def H(self):
        if self._needs.hunger > self.hunger_const/2:
            return 1
        else:
            return 1/2

    def S(self):
        if self._needs.stress < self.stress_const/2:
            return 1/2
        elif self._needs.stress < self.stress_const/3:
            return 1/3
        return 1

    def P(self):
        return self._stats.papers_sold/100