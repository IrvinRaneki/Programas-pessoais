#!/bin/python2
# -*- coding: cp1252 -*-
    #codigo para uso de caracteres especiais
from Tkinter import *
import tkMessageBox
import sys
import os
from matplotlib import *
from matplotlib.figure import Figure
import subprocess
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


################################################################################
#criacao da classe

class Packing(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)

        self.parent = parent
        self.initUI()
        self.initUI2()

################################################################################
#criacao da UI

    def initUI(self):
        self.parent.title("Program of Plot")

################################################################################
#Menubar
        menubar=Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu=Menu(menubar)
        helpMenu=Menu(menubar)
        editMenu=Menu(menubar)
        viewMenu=Menu(menubar)
        findMenu=Menu(menubar)
        packagesMenu=Menu(menubar)

        submenu=Menu(fileMenu)
        submenu.add_command(label="UE")

        fileMenu.add_command(label="Encontrar UE", underline=10, command=self.busca)
        fileMenu.add_separator()
        fileMenu.add_command(label="Plotar", underline=0, command=self.plot)
        fileMenu.add_separator()
        fileMenu.add_command(label="Salvar", underline=0)
        fileMenu.add_command(label="Salvar como", underline=1)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)

        menubar.add_cascade(label="File",underline=0, menu=fileMenu)


        editMenu.add_cascade(label="Adicionar UE's", menu=submenu, underline=0)
        menubar.add_cascade(label="Edit",underline=0,menu=editMenu)

        viewMenu.add_command(label="Vazio")
        menubar.add_cascade(label="View",underline=0,menu=viewMenu)

        findMenu.add_command(label="Vazio")
        menubar.add_cascade(label="Find",underline=0,menu=findMenu)

        packagesMenu.add_command(label="Vazio")
        menubar.add_cascade(label="Packages",underline=0,menu=packagesMenu)


        helpMenu.add_command(label="About Program of Plot", underline=0, command=self.about)
        menubar.add_cascade(label="Help",underline=0, menu=helpMenu)



################################################################################
#cricacao de outra layer
    def initUI2(self):
        frame=Frame(self.parent)
        frame.pack(side=TOP)

        self.b1=Button(frame, text='Encontrar UE',width=10, command=self.busca)
        self.b1.pack()

        self.b2=Button(frame, text='Adicionar UE ',width=10, )
        self.b2.pack()

        self.b3=Button(frame, text='Plotar Grafico',width=10, command=self.plot)
        #print bra
        self.b3.pack()

        self.b4=Button(frame, text='Exit',width=10, command=self.onExit)
        self.b4.pack()
################################################################################
#criacao de funcoes

    def plot(self):

        a=subprocess.Popen(["python2 /home/estagiario/Documents/plot_lib/plot_real_time.py"], shell=True)

    def about(self):
        tkMessageBox.showinfo("About","Ainda nao tem nada sobre!!")

    def busca(self):
        top = Toplevel()
        top.title("Loading...")

    def onExit(self):
        self.quit()

################################################################################
#main

def main():
    raiz=Tk()
    raiz.geometry("300x300")
    app=Packing(raiz)
    raiz.mainloop()


if __name__ == '__main__':
    main()
