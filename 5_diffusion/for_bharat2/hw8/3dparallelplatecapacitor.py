import numpy as np
import matplotlib.pyplot as plt
import sys

Nx = 40
Ny = 40
Nz = 40
px = 10
py = 10
d = 5 
c = 2.0   

V = np.zeros((Nx,Ny,Nz))
Vp = np.zeros((Nx,Ny,Nz))

def fixPlatesV(V, Nx, Ny,Nz, px,py, d):
    for j in range(Ny//2 - px, Ny//2 + py):
       for i in range(Nx//2 - px, Nx//2 + px):
          if(i < Nx//2):
             k = -int(round((c/px)*(i-(Nx//2 - px)))) + (Nz//2 - d)
          else:
             k = -int(round((c/px)*((Nx//2 + px) - i))) + (Nz//2 - d)
          V[i,j,k] = -1.0

    for j in range(Ny//2 - px, Ny//2 + py):
       for i in range(Nx//2 - px, Nx//2 + px):
          if(i <= Nx//2):
             k = int(round((c/px)*(i-(Nx//2 - px)))) + (Nz//2 + d)
          else:
             k = int(round((c/px)*((Nx//2 + px) - i))) + (Nz//2 + d)
          V[i,j,k] = 1.0

    return V
    
M=fixPlatesV(V, Nx, Ny,Nz, px,py, d)

for i in range(Nz):
    plt.title('z layer='+str(i))
    plt.pcolormesh(M[:,:,i])
    plt.pause(1)

sys.exit()
dV = 1.0
t = 0
maxiter = 100
 
while (dV > 1E-3) or (t < maxiter):
    print t
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            for k in range(1,Nz-1):
                V[i,j,k] = (1.0/6)*(Vp[i+1,j,k] + Vp[i-1,j,k] + Vp[i,j+1,k] + Vp[i,j-1,k]+Vp[i,j,k-1]+Vp[i,j,k+1])
    V=fixPlatesV(V, Nx, Ny,Nz, px,py, d)
    dV = np.sum(np.abs(V - Vp))/(Nx*Ny*Nz)
    Vp = V.copy()
    t+=1

print(t)

plt.figure()
ax = plt.axes(aspect='equal')
plt.pcolormesh(V[:,10,:], cmap = 'bwr') 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'$V(x,y,z)$')
plt.show()

    
#Electric field part
x = np.arange(0,Nx)
y = np.arange(0,Ny)
z = np.arange(0,Nz)

def grad(f):
    gx = np.zeros_like(f)
    gy = np.zeros_like(f)
    gz = np.zeros_like(f)
    for n in range(1,Nx-1):
        for m in range(1,Ny-1):
            for k in range(1,Nz-1):
                gx[n,m,k] = (V[n+1,m,k]-V[n-1,m,k])/(x[n+1]-x[n-1]);
                gy[n,m,k] = (V[n,m+1,k]-V[n,m-1,k])/(y[m+1]-y[m-1]);
                gz[n,m,k] = (V[n,m,k+1]-V[n,m,k-1])/(z[k+1]-z[k-1]);
    return gx, gy, gz


gx,gy,gz = grad(V)

X, Y = np.meshgrid(x,y)

plt.figure('with X and Y')
plt.contour(X, Y, V[:,10,:])
plt.colorbar()
plt.quiver(X, Y, 10*gx[:,10,:], 10*gy[:,10,:])
plt.xlabel("X")
plt.ylabel("Y")
plt.axes().set_aspect('equal')

plt.show()
