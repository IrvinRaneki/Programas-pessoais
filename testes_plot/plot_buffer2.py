import matplotlib.pyplot as plt
import random
import numpy as np
from collections import deque
import time
import threading

x=range(0,50)
y=range(0,5)
flag=False

def random_():
    global y
    global flag
    val=0
    for i in range(0,5):
        val=random.randint(-10,10)
        y[i]=val
        #print i
        if (i!=4):
            flag=False
        else:
            flag = True
            print flag


def passa_valor():
    for i in range(0,10):
        random_()
        time.sleep(0.1)

def plot():
    global y
    global flag
    #for i in range(0,10):
    while True:
        if (flag==True):
            print y
        time.sleep(0.1)

th1=threading.Thread(target=passa_valor)
th1.start()
th2=threading.Thread(target=plot)
th2.start()
