#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
d=1E-3
l=1.0
xgrid=10
ygrid=10
dx=l/xgrid
dy=l/ygrid
x=np.linspace(0,l,xgrid)
tmax=1.0
t_iter=10
dt=tmax/10
rho=np.empty((xgrid,ygrid,t_iter))   # particle concenteration in position x,y and t
rho[xgrid//2,ygrid//2, 0]=1.0      # initial configuration

for n in range(t_iter-1):
    for i in range(xgrid-1):
        for j in range(ygrid-1):
        
            rho[i,j,n+1]=rho[i,j,n] +(d*dt/dx**2) *(rho[i+1,j,n]+rho[i-1,j,n] -2*rho[i,j,n])+ (d*dt/dy**2)*(rho[i,j+1,n]-2*rho[i,j,n] +rho[i,j-1,n])
        rho[i,ygrid-1,n+1]=rho[i,ygrid-1,n] +(d *dt/dx**2) *(rho[i+1,ygrid-1,n]+rho[i-1,ygrid-1,n] -2*rho[i,ygrid-1,n])+ (d *dt/dy**2)*rho[i,0,n]-2*rho[i,ygrid-1,n] +rho[i,ygrid-2,n] #BC for last ygrid
        



for n in range(t_iter-1):
    for j in range(ygrid-1):
        rho[xgrid-1,j,n+1]=rho[xgrid-1,j,n] +(d *dt/dx**2) *(rho[0,j,n]+rho[xgrid-2,j,n] -2*rho[xgrid-1,j,n])+ (d *dt/dy**2)*rho[xgrid-1,j+1,n]-2*rho[xgrid-1,j,n] +rho[xgrid-1,j-1,n] # BC for last xgrid


plt.figure()
plt.pcolormesh(rho,x, vmin=0,vmx=0.5, cmap='pink')
#plt.imshow(rho,x)
plt.show()
