import matplotlib.pyplot as plt
import time
import random
from collections import deque

tamanho=30

def gera_num():
    val = 7
    while True:
        val = random.randint(-10,10)
        pause=random.randint(0,5)

        time.sleep(pause)
        return val, pause

lista = deque([0]*tamanho)
plt.axes(xlim=(0,tamanho), ylim=(-10,10))

line, = plt.plot(lista)
plt.grid(color='r')
plt.xticks([i for i in range(0,tamanho)])
plt.ion()
plt.show()

for i in range(0,20):

    y, x = gera_num()
    print y,x
    for i in range(0,x):
        lista.appendleft(False)
        datatoplot = lista.pop()

    lista.appendleft(y)
    datatoplot = lista.pop()
    line.set_ydata(lista)
    #plt.plot(b,a,'ko')

    plt.draw()
    plt.pause(0.1)
