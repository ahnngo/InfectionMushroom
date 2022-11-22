import copy
import random
INFECTED = 6


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

    def get_status(self):
        return self.status


class ImmuneCell(Cell):

    def __init__(self, x, y):
        super(ImmuneCell, self).__init__(x, y)
        self.status = '#'

    def get_status(self):
        return self.status


class InfectedCell(Cell):

    def __init__(self, x, y):
        super(InfectedCell, self).__init__(x, y)
        self.infected = INFECTED
        self.status = '*'

    def heal(self):
        self.infected -= 1


class Skin:

    def __init__(self, size):
        self.size = size
        self.skin = [[[None] * self.size for _ in range(self.size)] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.skin[i][j] = HealthyCell(i, j)

        self.skin[1][1] = InfectedCell(1, 1)

    def get_skin(self):
        return self.skin


    def get_infected(self, infected_rate=0.5):
        identical_skin = []
        for i in range(self.size):
            sub = []
            for j in range(self.size):
                sub.append(self.skin[i][j].get_status())
            identical_skin.append(sub)

        print("Identical Skin:", identical_skin)

        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for row in range(self.size):
            for col in range(self.size):
                infected_nbrs = 0
                for nbr in nbrs:
                    r = row + nbr[0]
                    c = col + nbr[1]
                    if (0 <= r < self.size) and (0 <= c < self.size) and identical_skin[r][c] == "*":
                        infected_nbrs += 1
                        break
                if infected_nbrs == 1:
                    self.skin[row][col] = InfectedCell(row, col)




myskin = Skin(5)
batch = myskin.get_skin()

container = []

myskin.get_infected()
container = []
for i in range(5):
    sub = []
    for j in range(5):
        sub.append(batch[i][j].get_status())
    container.append(sub)

print(container)

