import random

INFECTED = 6
IMMUNE = 4
SIZE = 23


class Cell:

    def __init__(self):
        self.status = 0
        self.i = 0
        self.j = 0

    def show_status(self):
        return self.status

    def set_location(self, a, b):
        self.i = a
        self.j = b

    def get_i(self):
        return self.i

    def get_j(self):
        return self.j

    def print(self):
        print('.')


class HealthyCell(Cell):

    def __init__(self):
        super().__init__()
        self.status = 1

    def show_status(self):
        return self.status

    def if_change(self):
        return random.uniform(0, 1)
    
    def print(self):
        print('-')


class ImmuneCell(Cell):

    def __init__(self, n=0, k=IMMUNE):
        super().__init__()
        self.status = 2
        self.count = k
        self.next = n

    def show_status(self):
        return self.status

    def set_next(self, n):
        self.next = n

    def get_next(self):
        return self.next

    def change(self):
        self.count -= 1
        return self.count == 0

    def print(self):
        print('#')

    def make_healthy(self, c=Cell()):
        h = HealthyCell()
        h.set_location(c.get_i(), c.get_j())


class InfectedCell(ImmuneCell):

    def __init__(self):
        super().__init__()
        self.status = 3
        ImmuneCell(0, INFECTED)

    def make_imm(self, c=Cell()):
        pass













