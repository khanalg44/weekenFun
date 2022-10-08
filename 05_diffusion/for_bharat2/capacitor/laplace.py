#!/usr/bin/env python

import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import sys

def test(N):
    M=np.zeros((N,N),dtype=float)
    for i in range(N):
        for j in range(N):
            M[i,j]=(i+j)%N
    x=range(N);y=range(N)
    X,Y=pl.meshgrid(x,y)
    Z=M[X,Y]
    fig=pl.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    pl.show()

def capacitor():
    Nmax=100
    Niter=70
    V=np.zeros((Nmax,Nmax),float)

    V[:,0]=100  # line at 100V
    V[:,-1]=100  # line at 100V

    #pl.pcolormesh(V)
    #pl.show()

    #sys.exit()

    for it in range(Niter):
        for i in range(1,Nmax-2):
            for j in range(1,Nmax-2):
                V[i,j] = 0.25 * ( V[(i+1), j] + V[(i-1),j] + V[i,(j+1)]+ V[i,(j-1)] )
                #V[i,j] = 0.25 * ( V[(i+1)%N, j] + V[(i-1)%N,j] + V[i,(j+1)%N]+ V[i,(j-1)%N] ) + np.pi * rho[i,j]
    x = range(0,Nmax-1,2); y = range(0,Nmax-1,2)
    X,Y=pl.meshgrid(x,y)
    Z=V[X,Y]
    fig=pl.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Potential')
    pl.show()

def ComputeU(N):
    U=np.zeros((N,N),dtype=float)

    # initial charge distribution
    rho=np.zeros((N,N),dtype=float)
    rho[0,:]=1

    pl.figure(1)
    pl.imshow(rho)
    pl.pause(1.1)

    pl.figure(2)
    Nitt=10
    for it in range(Nitt):
        pl.title('iteration:'+str(it))  
        pl.imshow(U)
        pl.pause(1.1)

        for i in range(N):
            for j in range(N):
                U[i,j] = 0.25 * ( U[(i+1)%N, j] + U[(i-1)%N,j] + U[i,(j+1)%N]+ U[i,(j-1)%N] ) + np.pi * rho[i,j]

        #pl.title('iteration:'+str(it))  
        #pl.imshow(U)
        #pl.pause(1.1)


if __name__=="__main__":
    #ComputeU(4)
    capacitor()
    #main()
    #N=10
    #test(N)

