#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def iter_map(a,N):
    x=np.zeros(N)
    x[0]=0.5
    for i in range(N-1):
        d=(a*x[i]*2**n +b)%2**n
        x[i+1]=d/2**n
    return x

N=5
n=8


a_min = 1.0
a_max = 4
step = 0.01
plt.figure()
for b in [0,1]:
    for a in np.arange(a_min, a_max, step):
        x = iter_map(a, 8)
        plt.plot(a*np.ones_like(x),x)

plt.xlabel('a')
plt.ylabel('$x^*$')
plt.show()
