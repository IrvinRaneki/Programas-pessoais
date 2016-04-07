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

#impot para leitura
import socket
from struct import *

import random
################################################################################
lista_media = deque([0]*1000)
################################################################################
lista_cqi = deque([0]*1000)
valores_cqi = deque([0]*50)
contador_amostra_cqi = 0
flag_plot_cqi = False
################################################################################
lista_bler = deque([0]*1000)
contador_harq=0
contador_amostra_bler=1
################################################################################

def delete_item():
    global lista_bler, lista_media
    del lista_bler[len(lista_bler)-1]
    del lista_media[len(lista_media)-1]

def delete_cqi():
    global lista_cqi
    for i in range(0,50):
        del lista_cqi[len(lista_cqi)-1]
################################################################################
##
## Criacao da UI principal
##
################################################################################
###############################UI principal#####################################
################################################################################
class Window(Tkinter.Frame):
    """docstring for Window"""
    def __init__(self, parent):
        global parente,a

        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        parente = self.parent

        a = IntVar()
        olives_chk=Checkbutton(parente,text="Plot/NotPlot",variable=a)
        olives_chk.pack()


    def initUI(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu =  Menu(menubar)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        fileMenu.add_command(label="Plot", underline=0, command=self.init_plot)
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)


    #################################FUNCOES####################################

    def onExit(self):
        time.sleep(0.5)
        self.th_plot.stop()
        self.th_leitura.stop()
        self.parent.quit()
        #self.parent.destroy()

    def init_plot(self):
        self.th_plot = Trd_plot()
        self.th_plot.start()
        self.th_leitura = Trd_leitura()
        self.th_leitura.start()
################################################################################
##
## Criacao do Plot
##
################################################################################
##############################CLASS_THREAD######################################
################################################################################
class Trd_plot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.paused = True
        self.state  = threading.Condition()

    def run(self):
        global lista_cqi, flag_plot_cqi, parente, a
        ########################################################################
        #                     Criacao do Grafico e Tollbar                     #
        ########################################################################
        figura = pylab.figure(1)
        ax = figura.add_axes([0.1,0.1,0.8,0.8])
        ax.grid(True)


        ax.set_title("Plot Bler")
        ax.set_xlabel("Time - 0.5 segundos")
        ax.set_ylabel("Amplitude - porcentagem")
        ax.axis([0,1000,0,100])

        line_cqi, = pylab.plot(lista_cqi)

        canvas =  FigureCanvasTkAgg(figura, master=parente)
        canvas.get_tk_widget().pack(side=Tkinter.TOP,  expand=1)#fill=Tkinter.BOTH,
        canvas.show()

        toolbar = NavigationToolbar2TkAgg(canvas, parente)
        toolbar.update()
        canvas._tkcanvas.pack(side=Tkinter.TOP, expand=1)# fill=Tkinter.BOTH,


        ########################################################################
        #                         Geracao do grafico                           #
        ########################################################################

        while True:


            if flag_plot_cqi is True:
                delete_cqi()
                lista_cqi.extendleft(valores_cqi)
                line_cqi.set_ydata(lista_cqi)
                canvas.draw()

                flag_plot_cqi = False

    def stop(self):
        with self.state:
            self.stop = True
            self._running=False
################################################################################
##
## Leitura socket
##
################################################################################
##############################CLASS_THREAD######################################
################################################################################
class Trd_leitura(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.paused = True
        self.state  = threading.Condition()

    def run(self):
        global contador_amostra_cqi, flag_plot_cqi, valores_cqi
        ##########  conexao  ###############################################
        host=''
        port=8888
        local=(host, port)
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.bind(local)
        ####################################################################
        ############## ----- configuracoes de leitura  ----- ###############
        while True:
            contador_amostra_cqi = 0
            teste = a.get()
            while contador_amostra_cqi<50:
                if teste is 0:
                    valores_cqi[contador_amostra_cqi]=0
                    contador_amostra_cqi+=1
                else:
                    valores_cqi[contador_amostra_cqi]=(random.randint(150,180)-128)/2
                    contador_amostra_cqi+=1

                if(contador_amostra_cqi is 50):

                    flag_plot_cqi = True
                    time.sleep(0.1)

                else:
                    flag_plot_cqi = False

    def stop(self):
        with self.state:
            self.stop = True
            self._running=False
