#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
def iter_map(a,N):
    x=np.zeros(N)
    n=8
    b=1
    x[0]=0.5
    for i in range(N-1):
        x[i+1]=((a*x[i]*(2**n) +b)%(2**n))/(2**n)
        
    return x

N=6
a_min = 0.0
a_max = 10
step = 0.01
plt.figure()

for a in np.arange(a_min, a_max, step):
    x = iter_map(a, 8)
    plt.plot(a*np.ones_like(x),x)

plt.xlabel(r'$a$')
plt.ylabel(r'$x$')
plt.show()
