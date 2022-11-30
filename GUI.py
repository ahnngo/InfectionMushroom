######################################################################
# Author: Anish Kharel
# Username: Kharel
###################################################################
from tkinter import *

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.drawWindow(self.root)

        self.root.mainloop()

    def drawWindow(self, root):

        title = Label(root, text='Infection Simulator',font=('sans',50)).grid(row=0,column=0,columnspan=3)

        paramframe = LabelFrame(root,width=450,height=400,highlightcolor='Red',relief='raised',pady=15,padx=30)
        paramframe.grid(row=1,column=0,pady=100,padx=120,sticky='n')

        animframe = LabelFrame(root,width=450,height=550,pady=15,padx=15).grid(row=1,column=1,padx=75,pady=25)


        param_head = Label(paramframe,text='Parameters',font=('times new roman',30)).grid(row=0,column=0,columnspan=3)
        ir_label = Label(paramframe,text= 'Infection Rate:',font=('times new roman',20)).grid(row=1,column=0,pady=10)
        ir_slider = Scale(paramframe, from_=0, to=100, orient=HORIZONTAL,length=150,tickinterval=25).grid(row=1,column=1,padx=15,columnspan=2)
        hr_label = Label(paramframe,text= 'Healing Rate:',font=('times new roman',20)).grid(row=2,column=0,pady=10)
        hr_slider = Scale(paramframe, from_=0, to=100, orient=HORIZONTAL,length=150,tickinterval=25).grid(row=2,column=1,padx=15,columnspan=2)
        size_label = Label(paramframe,text= 'Sample Size:',font=('times new roman',20)).grid(row=3,column=0,pady=10)
        size_slider = Scale(paramframe, from_=0, to=100, orient=HORIZONTAL,length=150,tickinterval=25).grid(row=3,column=1,padx=15,columnspan=2)

    def updateWindow(self):
        pass
    