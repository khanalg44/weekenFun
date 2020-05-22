#!/usr/bin/env python

import numpy as np
import pylab as pl
from scipy import weave
import sys

def finite_diff():
    Nx=100;Ny=100;Nt=1000;
    rho=np.zeros((Nx,Ny,Nt),dtype=float)
    # initial condition (1)
    rho[Nx/2,:,0] =1.0
    rho[:,Ny/2,0] =1.0
    # initial condition (2)
    #rho[:,0] =1.0
    #rho[Nx/2-5:Nx/2+5]=0

    dx=float(1./Nx); dt=float(1./Nt); D=1e-3
    Nitt=100
    for it in range(Nitt):
        for i in range(Nx):
            for i in range(Nx):
                for n in range(Nt-1):
                    rho[i,n+1] = rho[i,n] + D*dt/(dx*dx) * (rho[(i+1)%Nx,n] + rho[(i-1)%Nx, n]  - 2* rho[i,n]   )
    pl.pcolormesh(rho, vmin=0, vmax=0.5, cmap='pink')
    #pl.pause(1)
    pl.show()

def random_walker():
    Nx=100;Nt=200;
    rho=np.zeros((Nx,Nt))

    rho_0=np.zeros((Nx,Nt))
    # initial condition
    rho[:,0] =1.0
    rho[Nx/2-5:Nx/2+5,0]=0
    # visualize initial distributione
    #pl.title('initial distribution')
    #pl.pcolormesh(rho_0)
    #sys.exit()
    
    # obtain the <x^2>
    sumsq=0.0
    for x in range(Nx):
        sumsq += x**2
    avgsq=np.sqrt(sumsq/Nx)

    dx=float(1./Nx); dt=float(1./Nt); D=1e-3
    Nitt=5 
    for it in range(Nitt):
        for i in range(Nx):
            for n in range(Nt-1):
                rho[i,n] = rho[i,0]*np.exp(-i**2/(2*avgsq)) /np.sqrt(2*np.pi*avgsq)
        pl.title('n='+str(it+1))
        pl.pcolormesh(rho)#, vmin=0, vmax=0.5)#, cmap='pink')
        pl.pause(1)
        #pl.show()



if __name__=="__main__":
    random_walker()
    finite_diff()
