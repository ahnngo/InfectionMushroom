import copy
import random
INFECTED = 3


class Cell:

    def __init__(self, x, y):
        self.status = None
        self.xCor = x
        self.yCor = y

    def get_status(self):
        return self.status


class HealthyCell(Cell):

    def __init__(self, x, y):
        super(HealthyCell, self).__init__(x, y)
        self.status = '.'


class ImmuneCell(Cell):

    def __init__(self, x, y):
        super(ImmuneCell, self).__init__(x, y)
        self.status = '#'


class InfectedCell(Cell):

    def __init__(self, x, y):
        super(InfectedCell, self).__init__(x, y)
        self.infected = INFECTED
        self.status = '*'

    def heal(self):
        self.infected -= 1

    def get_infected_rate(self):
        return self.infected

class Skin:

    def __init__(self, size, infected_rate=0.5, healing_rate=0.5):
        self.size = size
        self.skin = [[[None] * self.size for _ in range(self.size)] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.skin[i][j] = HealthyCell(i, j)

        self.skin[2][2] = InfectedCell(2, 2)
        self.infected_rate = infected_rate
        self.healing_rate = healing_rate

    def get_skin(self):
        return self.skin

    def get_visual(self):
        visual_skin = []
        for i in range(self.size):
            sub = []
            for j in range(self.size):
                sub.append(self.skin[i][j].get_status())
            visual_skin.append(sub)
        return visual_skin

    def get_infected_score(self):
        visual_skin = []
        for i in range(self.size):
            sub = []
            for j in range(self.size):
                if self.skin[i][j].get_status() == '*':
                    sub.append(self.skin[i][j].get_infected_rate())
                else:
                    sub.append(self.skin[i][j].get_status())
            visual_skin.append(sub)
        return visual_skin


    def get_infected(self, infected_rate=0.5):
        identical_skin = self.get_visual()

        for i in identical_skin:
            print(i)
        print()

        identical_skin_score = self.get_infected_score()

        for i in identical_skin_score:
            print(i)
        print()

        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for row in range(self.size):
            for col in range(self.size):
                infected_nbrs = 0
                if identical_skin[row][col] == '#':
                    break
                for nbr in nbrs:
                    r = row + nbr[0]
                    c = col + nbr[1]
                    if (0 <= r < self.size) and (0 <= c < self.size) and (identical_skin[r][c] == "*"):
                        infected_nbrs += 1

                if identical_skin[row][col] == "*":
                    healing_chance = random.uniform(0, 1)
                    if healing_chance > (infected_nbrs / 8):
                        self.skin[row][col].heal()
                    if self.skin[row][col].get_infected_rate() == 0:
                        self.skin[row][col] = ImmuneCell(row, col)
                else:
                    if infected_nbrs != 0:
                        infected_chance = random.uniform(0, 1)
                        if 1 - infected_chance < (infected_nbrs / 8):
                            self.skin[row][col] = InfectedCell(row, col)


myskin = Skin(10)
for i in range(50):
    myskin.get_infected()
    myskin.get_infected_score()



