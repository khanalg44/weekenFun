#!/usr/bin/env python

import numpy as np
import pylab as pl
import sys,time

def get_rho(N):
    rho=np.zeros((N,N),dtype=float)
    rho[N/2,N/2]=1.0  # initial condition
    #for i in range(N):
    #    for j in range(N):
    #        rho[0,0]=i+j
    #rho[N/2,N/2]=1.0
    #pl.figure(1)
    #pl.title('charge density')
    #pl.imshow(rho)
    #pl.show()
    return rho

if __name__=="__main__":
    N=100;  Nitt=20; delta=0.001
    Rho=get_rho(N)
    U=np.zeros((N,N),dtype=float)
    t1=time.time()
    for n in range(Nitt):
        print 'n=',n
        for ix in range(N):
            for iy in range(N):
                U[ix,iy]=U[(ix+1)%N,iy]+U[(ix-1)%N,iy]+U[ix,(iy+1)%N]+U[ix,(iy-1)%N] + np.pi*Rho[ix,iy]*delta**2
                U[ix,iy] *= 0.25
    
        t2=time.time()
        print 'time=',t2-t1,'s'
        pl.figure(2)
        pl.title('potential distribution')
        pl.imshow(U)
        #pl.colorbar()
        pl.pause(1)
        #pl.show()
