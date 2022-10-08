#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt

def main():
    d=1E-3
    l=1.0
    xgrid=100
    ygrid=100
    dx=l/xgrid
    dy=l/ygrid
    x=np.linspace(0,l,xgrid)
    y=np.linspace(0,l,ygrid)
    tmax=1.0
    t_iter=100
    dt=tmax/t_iter
    rho=np.zeros((xgrid,ygrid,t_iter))  # particle concenteration in position x,y and t
    rho[xgrid//2,ygrid//2, 0]=1.0      # initial configuration

    for n in range(t_iter-1):
        for j in range(xgrid-1):
            for i in range(ygrid-1):
                rho[i,j,n+1]=rho[i,j,n] +(d*dt/dx**2) *(rho[i+1,j,n]+rho[i-1,j,n] -2*rho[i,j,n])+ (d*dt/dy**2)*(rho[i,j+1,n]-2*rho[i,j,n] +rho[i,j-1,n])
                rho[i,ygrid-1,n+1]=rho[i,ygrid-1,n] +(d *dt/dx**2) *(rho[i+1,ygrid-1,n]+rho[i-1,ygrid-1,n] -2*rho[i,ygrid-1,n])+ (d *dt/dy**2)*rho[i,0,n]-2*rho[i,ygrid-1,n] +rho[i,ygrid-2,n] #BC for last ygrid
                rho[xgrid-1,j,n+1]=rho[xgrid-1,j,n] +(d *dt/dx**2) *(rho[0,j,n]+rho[xgrid-2,j,n] -2*rho[xgrid-1,j,n])+ (d *dt/dy**2)*rho[xgrid-1,j+1,n]-2*rho[xgrid-1,j,n] +rho[xgrid-1,j-1,n]


    plt.figure()
    plt.pcolormesh(rho[:,:,50])
    plt.show()


if __name__=="__main__":
    main()

