#!/usr/bin/env python

import numpy as np
from matplotlib import pylab as pl

def main():

    N=10

    Z=np.zeros((N,N,N))

    for i in range(N):
        for j in range(N):
            for k in range(N):
                Z[i,j,k]=(i+j-k)%(3*N)


    for i in range(N):
        pl.title('using imshow')
        pl.imshow(Z[i])
        pl.pause(1)

    for j in range(N):
        pl.title('using pcolormesh')
        pl.pcolormesh(Z[i])
        pl.pause(1)


if __name__=="__main__":
    main()
