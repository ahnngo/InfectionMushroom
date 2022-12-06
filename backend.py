import random
import numpy as np
import matplotlib.pyplot as plt


class Cell:

    def __init__(self):
        self.status = None

    def get_status(self):
        return self.status


class HealthyCell(Cell):

    def __init__(self):
        super(HealthyCell, self).__init__()
        self.status = '.'


class ImmuneCell(Cell):

    def __init__(self):
        super(ImmuneCell, self).__init__()
        self.status = '#'


class InfectedCell(Cell):

    def __init__(self):
        super(InfectedCell, self).__init__()
        self.infected = 6
        self.status = '*'
        self.infectedDay = 0

    def heal(self):
        self.infected -= 1

    def get_infected_score(self):
        return self.infected

    def increment_infected_day(self):
        self.infectedDay += 1

    def get_infected_day(self):
        return self.infectedDay


class Skin:

    def __init__(self, size, infected_rate, healing_rate):
        self.size = size
        self.skin = [[[None] * self.size for _ in range(self.size)] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.skin[i][j] = HealthyCell()

        x, y = random.randint(0, self.size - 1), random.randrange(0, self.size - 1)
        self.skin[x][y] = InfectedCell()
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
        return np.array(visual_skin)

    def get_infected_matrix(self):
        visual_skin = []
        for i in range(self.size):
            sub = []
            for j in range(self.size):
                if self.skin[i][j].get_status() == '*':
                    sub.append(self.skin[i][j].get_infected_score())
                else:
                    sub.append(self.skin[i][j].get_status())
            visual_skin.append(sub)
        return np.array(visual_skin)

    def get_infected_day_matrix(self):
        visual_skin = []
        for i in range(self.size):
            sub = []
            for j in range(self.size):
                if self.skin[i][j].get_status() == '*':
                    sub.append(self.skin[i][j].get_infected_day())
                else:
                    sub.append(self.skin[i][j].get_status())
            visual_skin.append(sub)
        return np.array(visual_skin)

    def get_infected(self):

        nbrs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for row in range(self.size):
            for col in range(self.size):
                infected_nbrs = 0

                # if the cell is completely immune, do nothing
                if self.skin[row][col].get_status() == '#':
                    continue

                # count the number of infected cells
                for nbr in nbrs:
                    r = row + nbr[0]
                    c = col + nbr[1]
                    if (0 <= r < self.size) and (0 <= c < self.size) and (self.skin[r][c].get_status() == "*"):
                        infected_nbrs += 1

                # if the cell is infected, calculate the probability of getting healed
                if self.skin[row][col].get_status() == "*":
                    self.skin[row][col].increment_infected_day()
                    healing_chance = random.uniform(0, .8) + self.skin[row][col].get_infected_day() * 0.05 - infected_nbrs * 0.05
                    # print('hr',healing_chance,self.healing_rate)
                    if healing_chance < self.healing_rate:
                        self.skin[row][col].heal()
                    # if the infected score is 0, the cell becomes immune
                    if self.skin[row][col].get_infected_score() == 0:
                        self.skin[row][col] = ImmuneCell()

                else:
                    if infected_nbrs != 0:
                        infected_chance = random.uniform(0, .8) + infected_nbrs * 0.05
                        # print(infected_chance, self.infected_rate)
                        if infected_chance < self.infected_rate:
                            self.skin[row][col] = InfectedCell()

    def visualize(self):
        """
        Visualize the skin using matplotlib
        :return: None
        """
        visual_skin = self.get_visual().tolist()
        for i in range(len(visual_skin)):
            for j in range(len(visual_skin)):
                if visual_skin[i][j] == '.':
                    visual_skin[i][j] = int(0)
                elif visual_skin[i][j] == '*':
                    visual_skin[i][j] = int(1)
                else:
                    visual_skin[i][j] = int(2)

        visual_skin = np.array(visual_skin)
        colors = np.array([[0, 255, 0],         # green
                           [255, 0, 0],         # red
                           [220, 220, 220]])    # gray

        plot = colors[visual_skin]
        plt.imshow(plot)
        plt.show()


def main():
    size = int(input("Skin size (n x n): "))
    myskin = Skin(size)
    while True:
        next_step = int(input("Update step (int, put 0 to visualize the skin patch)? : "))
        if next_step > 0:
            for i in range(next_step):
                myskin.get_infected()
                myskin.visualize()
        else:
            myskin.visualize()
            stop = input("Stop? (y/n): ")
            if stop == "y":
                return
            else:
                continue


if __name__ == "__main__":
    main()



