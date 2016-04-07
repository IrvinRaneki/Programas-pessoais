#!/bin/python
import sys
# Complete the function below.

def  StairCase(n):

    for i in range(0,n):
        print ' '*(n-(i+1)),
        print '#'*(i+1)



_n = int(raw_input());
StairCase(_n);
