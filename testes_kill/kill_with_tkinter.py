import Tkinter
from Tkinter import *

import threading
import time

class Trd_teste(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.paused = True
        self.state = threading.Condition()

    def run(self):
        while True:
            print( 'thread iniciada')
            time.sleep(1)

    def stop(self):
        print( 'thread cancelada')
        with self.state:
            self.stop = True

    def pause(self):
        print( 'thread pausada')
        with self.state:
            self.pause = True

    def resume(self):
        print( 'thread retornada')
        with self.state:
            self.pause = False

class Tela(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initUI2()

    def initUI(self):
        frame = Frame(self.parent)
        frame.pack()
        self.btn1 = Button(frame, text = 'inicia thread',width=10, command=lambda:self.thread_init())
        self.btn1.pack()
        self.btn2 = Button(frame, text = 'pause thread',width=10, command=lambda:self.thread_pause())
        #self.btn2.pack()
        self.btn3 = Button(frame, text = 'resume thread',width=10, command=lambda:self.thread_resume())
        #self.btn3.pack()
        self.btn4 = Button(frame, text = 'kill thread',width=10, command=lambda:self.thread_kill())
        self.btn4.pack()

    def initUI2(self):
        frame2 = Frame(self.parent)
        frame2.pack()
        self.btn = Button(frame2, text = 'sair', width=10, command=lambda:self.on_exit())
        self.btn.pack()

    def thread_init(self):
        self.init_thread = Trd_teste()
        self.init_thread.start()

    def thread_pause(self):
        self.init_thread.pause()

    def thread_resume(self):
        self.init_thread.resume()

    def thread_kill(self):
        self.init_thread.stop()

    def on_exit(self):
        self.parent.destroy()

def main():
    #init_thread = Trd_teste()
    #init_thread.start()
    root = Tkinter.Tk()
    root.wm_title("Janela")
    root.geometry("200x200")
    app = Tela(root)
    root.mainloop()

if __name__ == '__main__':
    main()
