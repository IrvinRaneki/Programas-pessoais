#!/bin/python2
# -*- coding: cp1252 -*-

##
## principal para a criacao do fapi Analyzer de modo completo
##

import Tkinter
import window

def main():

    root = Tkinter.Tk()
    root.wm_title("Fapi Analyzer 2.0")

    app = window.Window(root)

    root.geometry("700x600")
    root.mainloop()

if __name__ == '__main__':
    main()
