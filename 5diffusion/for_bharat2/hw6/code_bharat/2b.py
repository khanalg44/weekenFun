#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def iter_map(b,N):
    x = np.zeros(N)
    x[0] = 0.5
    for i in range(N-1):
        x[i+1]=(int((x[i])*(2**n) +b)%(2**n)) /(2**n)
    return x

if __name__=="__main__":
  
    b=1
    a_min=1
    a_max=4
    step=0.001
    N=10
    n=8
   
    plt.figure(1)
   
    for a in np.arange(a_min, a_max, step):
        x = iter_map(a, n)
        plt.plot(a*np.ones_like(x),x)

    plt.xlabel(r'$a$')
    plt.ylabel(r'$x$')
    plt.show()
