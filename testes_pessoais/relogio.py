#!/bin/python2
# -*- coding: cp1252 -*-

from Tkinter import *
from time import *


class Janela:

    def __init__(self,parent):

        self.relogio = Frame(parent)
        self.relogio.pack()
        parent.title('Relogio')

        self.reloginho()

        def reloginho():
            self.relogio=tkinter.Label()
            self.relogio['text']='Relogio'
            self.relogio.pack()
            self.relogio['font']='Helvetica 50 bold'
            print('',strftime('%H:%M:%S'))
        #def tic():
    #        relogio['text'] = strftime('%H:%M:%S')

#        def tac():
#            tic()
#            relogio.after(1000,tac)

def main():
    raiz = Tk()
    raiz.geometry("300x300")
    app=Janela(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    main()
