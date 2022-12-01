import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sandBox import *


root = tk.Tk()



figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
skin = Skin(100)
for i in range(10):
    skin.get_infected()
skin.visualize()
ax.set_title('The Title for your chart')

root.mainloop()