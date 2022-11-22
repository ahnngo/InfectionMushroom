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

    def __init__(self):
        super(InfectedCell, self).__init__()
        self.status = '*'


class Skin:

    def __init__(self, size):

        self.size = size
        self.skin = [[[None] * self.size for _ in range(3)] * self.size for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.skin[i][j] = HealthyCell(i, j)

        self.skin[1][1] = ImmuneCell(1, 1)

    def get_skin(self):
        return self.skin


myskin = Skin(3)
batch = myskin.get_skin()

container = []
for i in range(3):
    sub = []
    for j in range(3):
        sub.append(batch[i][j].get_status())
    container.append(sub)

print(container)

