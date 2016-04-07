#!/bin/python2
# -*- coding: cp1252 -*-


#impott para window
import Tkinter
from Tkinter import *
import time

#import para plot
import threading
import pylab
from pylab import *
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from collections import deque

import random

vai = 0

num1=75
num2=45
num3=15
lista1 = deque([0]*1000)
lista2 = deque([0]*1000)
lista3 = deque([0]*1000)


class Window(Tkinter.Frame):
    """docstring for Window"""
    def __init__(self, parent):

        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        global num1, num2, num3, vai
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        a = IntVar()
        chk1 = Checkbutton(self.parent,text="Plot 1",variable=a)
        chk1.pack()
        b = IntVar()
        chk2 = Checkbutton(self.parent,text="Plot 2",variable=b)
        chk2.pack()
        c = IntVar()
        chk3 = Checkbutton(self.parent,text="Plot 3",variable=c)
        chk3.pack()
        print 'to aqui'
        self.init_plot()

    def init_plot(self):
        self.th=threading.Thread(target=self.plot)
        self.th.daemon()
        self.th.state = threading.Condition()
        self.th.start()

    def plot(self):

        figura = pylab.figure(1)
        ax = figura.add_axes([0.1,0.1,0.8,0.8])
        ax.grid(True)

        ax.axis([0,1000,0,100])

        line1, = pylab.plot(lista1)
        line2, = pylab.plot(lista2)
        line3, = pylab.plot(lista3)

        canvas =  FigureCanvasTkAgg(figura, master=self.parent)
        canvas.get_tk_widget().pack(side=Tkinter.TOP,  expand=1)
        canvas.show()

        while True:
            num1 = (random.randint(75,90))
            num2 = (random.randint(45,60))
            num3 = (random.randint(15,30))

            del lista1[len(lista1)-1]
            del lista2[len(lista2)-1]
            del lista3[len(lista3)-1]

            lista1.appendleft(num1)
            lista2.appendleft(num2)
            lista3.appendleft(num3)

            line1.set_ydata(lista1)
            line2.set_ydata(lista2)
            line3.set_ydata(lista3)

            canvas.draw()




def main():

    root = Tkinter.Tk()
    root.wm_title("Fapi Analyzer 2.0")

    app = Window(root)

    root.geometry("700x600")
    root.mainloop()

if __name__ == '__main__':
    main()
