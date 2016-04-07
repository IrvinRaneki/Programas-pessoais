#!/bin/python2
import matplotlib.pyplot as plt
import time
import random
from collections import deque
import numpy as np

def random_gen():
    val=7
    while True:
        #val=random.randint(-10,10)
        if val == 7:
            val=-7
        else:
            val =7
        #val = raw_input()
        pause=random.randint(0,5)
        print pause
        time.sleep(pause)
        yield val
        #time.sleep(0.1)

a1 = deque([0]*100)
ax = plt.axes(xlim=(0, 100), ylim=(0, 10))
d = random_gen()

line, = plt.plot(a1)
plt.ion()
plt.ylim([-15,15])
plt.show()

for i in range(0,100):
    a1.appendleft(next(d))
    datatoplot = a1.pop()
    line.set_ydata(a1)
    plt.draw()
    print a1[0]
    i += 1
    #time.sleep(0.1)
    plt.pause(0.1)
