import numpy as np
import pylab as plt
import sys

def fixPlatesV(V,Nx, Ny, px, d):
    for j in (Ny//2 - d,):
        for i in range(Nx//2 - px, Nx//2 + px):
            V[i,j] = 1.0

    for j in (Ny//2 + d,):
        for i in range(Nx//2 - px, Nx//2 + px):
            V[i,j] = -1.0
    return V

def main():
    Nx = 60
    Ny = 60
    px = 20
    d = 10
    V = np.zeros((Nx,Ny))
    Vp = np.zeros((Nx,Ny))
    Vp = fixPlatesV(Vp, Nx, Ny, px, d)

    dV = 1.0
    t = 0
    maxiter = 10000
    tol = 1E-5

    while (dV > tol) and (t < maxiter):
        for i in range(1, Nx-1):
            for j in range(1, Ny-1):
                V[i,j] = (1.0/4)*(Vp[i-1,j] + Vp[i+1,j] + Vp[i,j+1] + Vp[i,j-1])
        V = fixPlatesV(V, Nx, Ny, px, d)
        dV = np.sum(np.abs(V - Vp))/(Nx*Ny)
        Vp = V.copy()
        t+=1
        
    print(t)
    plt.figure()
    ax = plt.axes(aspect='equal')
    #ax.pcolormesh(V.T, cmap='bwr') # pcolormesh always interprets columns as x and rows as y
    plt.imshow(V.T,cmap='bwr')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'$V(x,y)$')
    plt.show()

if __name__=="__main__":
    main()
