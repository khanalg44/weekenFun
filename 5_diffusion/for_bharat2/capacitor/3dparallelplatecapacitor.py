import scipy as sp
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
Nx = 20
Ny = 20
Nz=20
px = 6
py=6
d = 4

Vp = np.zeros((Nx,Ny,Nz))
V = np.zeros((Nx,Ny,Nz))

def fixPlatesV(V, Nx, Ny,Nz, px,py, d):
    for k in (Nz//2 - d,):
        for i in range(Nx//2 - px, Nx//2 + px,):
            for j in range(Ny//2 - px, Nx//2 + px,):
                V[i,j,k] = -1.0

    for k in (Nz//2 + d,):
        for i in range(Nx//2 - px, Nx//2 + px,):
            for j in range(Ny//2 - px, Nx//2 + px,):
                V[i,j,k] = 1.0
    return V

Vp = fixPlatesV(V, Nx, Ny, Nz,px,py, d)

dV = 1.0
t = 0
maxiter = 100
tol = 1E-3

while (dV > tol) or (t < maxiter):
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            for k in range(1,Nz-1):

                V[i,j,k] = (1.0/6)*(Vp[i+1,j,k] + Vp[i-1,j,k] + Vp[i,j+1,k] + Vp[i,j-1,k]+Vp[i,j,k-1]+Vp[i,j,k+1])
    V = fixPlatesV(V, Nx, Ny,Nz, px,py, d)
    dV = np.sum(np.abs(V - Vp))/(Nx*Ny*Nz)
    Vp = V.copy()
    t+=1

print sp.shape(V)
#pl.pcolormesh(V.transpose())
pl.imshow(V)
pl.show()

#plt.figure()
#ax = plt.axes(aspect='equal')
#ax.pcolormesh(V.T, cmap='bwr')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_Zlabez('z')                                    
#ax.set_title(r'$V(x,y,z)$')
#plt.show()
