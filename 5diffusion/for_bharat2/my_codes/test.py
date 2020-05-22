#!/usr/bin/env python

import pylab as pl
from scipy import *

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


def hermite(n,x):
    # hermite polynomial of order n
    if n==0:
        return 1.0
    elif n==1:
        return x
    else:
        return 2*x*hermite(n-1,x)-2*(n-1.0)*hermite(n-2,x)


def test(1)
    NN=[1,2,3,4,5]
    for n in NN:
        xx=linspace(-2,2,100)
        lst=[]
        for x in xx:
            lst.append(hermite(n,x))
        pl.plot(xx,lst,label="n="+str(n))
        pl.legend(loc='best')
        pl.show()  

    

if __name__=="__main__":
    test1()

