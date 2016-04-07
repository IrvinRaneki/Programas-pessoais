import matplotlib.pyplot as plt
import random
import numpy as np
from collections import deque
import time
import threading

#x=range(0,5)
y=range(0,25)           #global y que eh plotado
a1=deque([0]*2000)       #lista para plotar em sequencia
################################################################################
#                          deleta os primeiros da lista                        #
################################################################################
def delete():
    global a1
    for i in range(0,25):
        del a1[2000-(i+1)]

################################################################################
#                          thread da geracao do grafico                        #
################################################################################
def principal():
    global a1
    ######### ----- configuracoes do grafico ----- #########
    ax=plt.axes(xlim=(0,2000),ylim=(-15,15))
    line, = plt.plot(a1)
    plt.ion()
    plt.show()
    ########################################################
    for i in range(0,100):
        delete()
        a1.extendleft(y) #adiciona novos pontos a lista
    ######### ----- desenhando  no  grafico  ----- #########
        line.set_ydata(a1)
        plt.draw()

################################################################################
#                          thread da geracao de random                         #
################################################################################
def random_gen():
    val=0
    for i in range(0,100):
        for i in range(0,25):
            val=random.randint(-10,10)
            y[i]=val
            time.sleep(0.001)





################################################################################
#					main
################################################################################
def main():
    th1=threading.Thread(target=principal)
    th2=threading.Thread(target=random_gen)
    th1.start()
    th2.start()

if __name__ == '__main__':
	main()
