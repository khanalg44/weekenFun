#!/usr/bin/env python

import numpy as np
import pylab as pl

def bf(n,r):
    if n==0:
        return 0.5
    else:
        return r*bf(n-1,r)*(1.0-bf(n-1,r))
        
      
if __name__=="__main__":
    Nr=100
    rr=np.linspace(2.1,4.5, Nr)
    NN=15
    lst=[]
    for r in rr:
        sum1=0.0
        for n in range(NN):
            sum1 += bf(n,r)
        lst.append(sum1)
    pl.plot(range(Nr),lst)
    pl.show()
