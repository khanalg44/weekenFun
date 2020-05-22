#!/usr/bin/env python

from scipy import *
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D


def main():
    Nmax=60;Niter=50; V=zeros((Nmax,Nmax),dtype=float)

    for k in range(0,Nmax-1):
        V[k,0] =100.0

    for iter in range(Niter):
        if iter %10 ==0: print iter
        for i in range(1,Nmax-2):
            for j in range(1,Nmax-2):
                V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])
    
    x=range(0,Nmax-1,2);y=range(0,50,2)
    
    X,Y=np.meshgrid(x,y)

    def functz(V):
        return V[X,Y]

    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    Z=functz(V)
    #fig=pl.figure()
    #ax=Axes3D(fig)
    ax.plot_wirefreame(X,Y,Z, rstride=10, cstride=10)
    pl.show()


if __name__=="__main__":
    main()
