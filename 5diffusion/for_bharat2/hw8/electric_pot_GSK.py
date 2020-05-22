#!/usr/bin/env python

import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import sys

def get_plate(Nx,Ny,d,px):
    V=np.zeros((Nx,Ny))
    V[Nx/2-px:Nx/2+px,Ny/2-d] =1.0
    V[Nx//2-px:Nx//2+px,Ny//2+d] =-1.0
    #pl.show()
    #sys.exit()
    return V

def dist(x1,x2):
    d= np.sqrt( (x1[0]-x2[0])**2 + (x1[1]-x2[1])**2  )
    return d

def solve_poisson(Nx,Ny,d,px):
    V=get_plate(Nx,Ny,d,px)

    for i in range(Nx):
        for j in range(Ny):

            sum1=0.0
            for k in range(Nx//2-px,Nx//2+px):
                if ( np.abs(i-k)>1e-5 ) and ( np.abs(j-(Ny//2-d)) > 1e-5 ):
                    l=(Ny//2-d)
                    sum1+= 1.0 / dist( [i,j], [k,l]  )
                if ( np.abs(i-k)>1e-5 ) and ( np.abs(j-(Ny//2+d)) > 1e-5 ):
                    l=(Ny//2+d)
                    sum1+= 1.0 / dist( [i,j], [k,l]  )
            
            V[i,j] = sum1
    return V

def get_crease_plate(Nx, Ny, px, c, d):
    V=np.zeros((Nx,Ny))
    #for line1
    # we know x values go from (Nx-px)/2 to Nx/2
    for x in range((Nx-px)/2,Nx/2):
        m1=2.0*c/px
        b1=-0.5*( 2.0*c*Nx/float(px)  - Nx -d -2*c  )
        y=int(m1*x+ b1)
        V[x,y]=1.0

    pl.imshow(V)
    pl.show()

def Plates3D():
    Nx=20;Ny=20;Nz=20;px=int(0.8*Nx);pz=int(0.8*Nz);d=int(0.6*Ny)
    V=np.zeros((Nx,Ny,Nz),dtype=float)

    #define the parallel plates
    V[(Nx-px)/2:(Nx+px)/2, (Ny-d)/2, (Nz-pz)/2:(Nz+pz)/2] =1.0
    V[(Nx-px)/2:(Nx+px)/2, (Ny+d)/2, (Nz-pz)/2:(Nz+pz)/2] =-1.0
    
    for i in range(1,Nx-1):
        for j in range(1, Ny-1):
            for k in range(1,Nz-1):
                V[i,j,k] = (1./6.)*(V[i+1,j,k] + V[i-1,j,k] + V[i,j+1,k] + V[i,j-1,k]+V[i,j,k-1]+V[i,j,k+1])

    for i in range(1,Nz,2):
        pl.title('z layer='+str(i))
        pl.imshow(V[:,:,i])
        pl.pause(1)
    sys.exit()
    #x=range(Nx);y=range(Ny)
    #X,Y=pl.meshgrid(x,y)
    #Z=V[X,Y]
    #fig=pl.figure()
    #ax=Axes3D(fig)
    #ax.plot_wireframe(X,Y,Z)
    #ax.scatter[V]
    #pl.show()

def fixPlatesV(V,Nx, Ny, px, d):

    for j in (Ny//2 - d,):
        for i in range(Nx//2 - px, Nx//2 + px):
            V[i,j] = 1.0

    for j in (Ny//2 + d,):
        for i in range(Nx//2 - px, Nx//2 + px):
            V[i,j] = -1.0

    return V
def main():
    Nx = 60;Ny = 60;px = 20;d = 10
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
    pl.figure()
    ax = pl.axes(aspect='equal')
    #ax.pcolormesh(V.T, cmap='bwr') # pcolormesh always interprets columns as x and rows as y
    pl.imshow(V.T,cmap='bwr')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(r'$V(x,y)$')
    pl.show()

if __name__=="__main__":

    Nx=80;Ny=80;px=35;d=5;c=2
    #Nx=40;Ny=40;d=8 ;px=2
    #Plates3D()
    #get_crease_plate(Nx, Ny, px, c, d)
    V_initial=get_plate(Nx,Ny,d,px)
    V1=solve_poisson(Nx,Ny,d,px)
    pl.figure(1)
    pl.imshow(V_initial.T)
    pl.figure(2)
    pl.imshow(V1.T)
    pl.show()
    #main()
    #print get_line([20,50],[40,55])


