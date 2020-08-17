#!/usr/bin/env python

import numpy as np
import pylab as pl
import sys

def iter(n,a,b):
    if n==0:
        return 0.2
    else:
        #return (int(iter(n-1,a,b)*2**n) *a +b)%(2**n) /2**n
        return ((a*iter(n-1,a,b)*2**n) +b)%(2**n) /2**n


if __name__=="__main__":
    n=50;
    beta=[0,1,100]

    for b in beta:
        lst_a=[]
        for a in np.linspace(-5.0,10.0,100):
            lst_a.append(iter(n,a,b))
        pl.plot(np.linspace(-5,10,100),lst_a,'o')
        pl.show()

