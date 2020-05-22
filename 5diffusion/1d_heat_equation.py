#!/usr/bin/env python

import numpy as np
import pylab as pl

def compute_T(Nx,Nt, eta):
    T=np.zeros((Nx,Nt),dtype=float)
    T[Nx/2,Nt/2]=100

    Nitt=4
    for itt in range(Nitt):
        for i in range(Nx):
            for j in range(Nt):
                T[i,j]= T[i,(j+1)%Nt]-eta*(T[(i+1)%Nx,j]+T[(i-1)%Nx,j]-2*T[i,j])

        pl.imshow(T)
        pl.show()



if __name__=="__main__":
    
    kap=100; rho=30; C=1.0;
    dx= 0.01; dt=0.01

    eta= kap * dt /(rho * C * dx*dx)

    Nx=05; Nt=07;
    compute_T(Nx,Nt, eta)
