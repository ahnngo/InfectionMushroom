######################################################################
# Author: Anish Kharel
# Username: Kharel
###################################################################
from time import sleep
from tkinter import *
import backend as logic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Gui:
    def __init__(self):
        self.root = Tk()  # establish a base root window to put everything on
        self.root.state('zoomed')  # full screen
        self.drawWindow(self.root)  # initial call to draw function
        self.graph = None

        self.root.mainloop()

    def drawWindow(self, root):

        title = Label(root, text='Infection Simulator', font=('sans', 50)).grid(row=0, column=0, columnspan=3)

        paramframe = LabelFrame(root, width=450, height=400, highlightcolor='Red', relief='raised', pady=15, padx=10)
        paramframe.grid(row=1, column=0, pady=75, padx=120, sticky='n')

        canvas = Canvas(root).grid(row=1, column=1)

        # Establishes the initial state of the screen with sliders and entry objects
        param_head = Label(paramframe, text='Parameters', font=('times new roman', 30)).grid(row=0, column=0,
                                                                                             columnspan=3)
        ir_label = Label(paramframe, text='Infection Rate:', font=('times new roman', 20)).grid(row=1, column=0,
                                                                                                pady=10)
        ir_slider = Scale(paramframe, from_=0, to=100, orient=HORIZONTAL, length=150, tickinterval=25)
        ir_slider.grid(row=1, column=1, padx=15, columnspan=2)
        hr_label = Label(paramframe, text='Healing Rate:', font=('times new roman', 20)).grid(row=2, column=0, pady=10)
        hr_slider = Scale(paramframe, from_=0, to=100, orient=HORIZONTAL, length=150, tickinterval=25)
        hr_slider.grid(row=2, column=1, padx=15, columnspan=2)
        size_label = Label(paramframe, text='Sample Size:', font=('times new roman', 20)).grid(row=3, column=0, pady=10)
        size_input = Entry(paramframe, font=('times new roman', 12), justify='center')
        size_input.grid(row=3, column=1, padx=15, columnspan=2)
        days_label = Label(paramframe, text='Amount of days:', font=('times new roman', 20)).grid(row=4, column=0,
                                                                                                  pady=10)
        days_input = Entry(paramframe, font=('times new roman', 12), justify='center')
        days_input.grid(row=4, column=1, padx=15, columnspan=2)

        start = Button(root, text='Simulate', font=('times new roman', 30), bg='green',
                       command=lambda: startsimulation(int(size_input.get()), hr_slider.get(), ir_slider.get(), self,
                                                       int(days_input.get()))).grid(row=3, column=0, stick='n')
        # button to start the simulation which calls the atartsimulation function on click.

        self.graph = canvas

    def update_animate(self, visual_skin, day):
        """
        Updates the matplotb by re-processing the skins output and converting into a matplotlib
        which is converted into a tkinter canvas object then put on the screen
        :param visual_skin: The skin matrix
        :return: None
        """
        for i in range(len(visual_skin)):  # Converts the character matrix into a numbers one
            for j in range(len(visual_skin)):
                if visual_skin[i][j] == '.':
                    visual_skin[i][j] = int(0)
                elif visual_skin[i][j] == '*':
                    visual_skin[i][j] = int(1)
                else:
                    visual_skin[i][j] = int(2)

        visual_skin = np.array(visual_skin)
        # Establishes the color scheme by index number
        colors = np.array([[0, 255, 0],  # green
                           [255, 0, 0],  # red
                           [220, 220, 220]])  # gray

        # Creates a matlib plot with the visual skin using the color established above
        plotfin = colors[visual_skin]
        fig, ax = plt.subplots()
        # ax.plot(plotfin)

        ax.imshow(plotfin)
        canvas = plt.Figure()
        # Converts the matplotlib plot object into a canvas
        canvas = FigureCanvasTkAgg(fig,
                                   master=self.root)
        canvas.get_tk_widget().grid(row=1, column=1, padx=15, pady=20, sticky='w')
        # Refreshes the page so the new matrix can be displayed
        # self.graph.draw()
        self.root.update()      #Refreshes the page so the new matrix can be displayed
        # plt.show()


def startsimulation(size, healingrate, infectionrate, gui, days):
    """
    Button click function which takes all the input data and starts the simulation process
    :param size: Size of skin matrix
    :param healingrate: The rate of cells that get healed
    :param infectionrate: the rate of infection on non-immune cells
    :param gui: The GUI objects which we will call the functions on
    :param days: THe length of simulation in days
    :return: None
    """
    # create a skin object based on parameters
    simulation = logic.Skin(size=size, infected_rate=infectionrate / 100, healing_rate=healingrate / 100)
    print(infectionrate, healingrate)
    for i in range(days + 1):
        # Steps to the next day in the simulations and get the new skin matrix
        simulation.get_infected()
        # Gives the skin matrix we got above and updates the GUI accordingly
        gui.update_animate(simulation.get_visual().tolist(), i)


def main():
    screen = Gui()


main()
