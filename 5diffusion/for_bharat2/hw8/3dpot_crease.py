import numpy as np
import matplotlib.pyplot as plt

Nx = 20
Ny = 20
Nz=20
px = 10
py=10
d = 5 
c=2   #crease's grid     # It tried my unused brain here dai, hernu ta k hunxa but Shows some error fixed garna milxa hola ni error

V = np.zeros((Nx,Ny,Nz))
Vp = np.zeros((Nx,Ny,Nz))

def fixPlatesV(iteration):
  for k in (Nz//2+d+c,):                      # crease is in z axis, so deviating it by 5 from middle
    for i in range(Nx//2 - px, Nx//2 + px):
      for j in range(Ny//2 - px, Ny//2 + py):
         V[i,j,k] = -1.0
  for k in (Nz//2 + d,):                          ## same plate but it is one the end of the plate with reduced z value
    for i in range(Nx//2 - px, Nx//2 + px): 
      for j in range(Ny//2 - px, Ny//2 + py):
        V[i,j,k] = -1.0

  for k in (Nz//2 - d-c,):                         ## # crease is in z axis, so deviating it by 5 from middle so substracting
    for i in range(Nx//2 - px, Nx//2 + px):
       for j in range(Ny//2 - py, Ny//2 + py):
          V[i,j,k] = 1.0
                
  for k in (Nz//2 - d,):
    for i in range(Nx//2 - px, Nx//2 + px):         ## ## # crease is in z axis, so deviating it by 5 and it is on the end of same parallel plate downward
       for j in range(Ny//2 - px, Ny//2 + py):
          V[i,j,k] = 1.0
  return V
    
# mistake 1 after defining function remove the indentation
dV = 1.0
t = 0
maxiter = 10000

while (dV > 1E-3) and (t < maxiter):
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            for k in range(1,Nz-1):
                V[i,j,k] = (1.0/6)*(Vp[i+1,j,k] + Vp[i-1,j,k] + Vp[i,j+1,k] + Vp[i,j-1,k]+Vp[i,j,k-1]+Vp[i,j,k+1])
    #mistake 3 this function is not defined
    # your defined function is named differently
    V=fixPlatesV(t)
    #V=fixplates(iteraton)
    dV = np.sum(np.abs(V - Vp))/(Nx*Ny*Nz)
    Vp = V.copy()
    t+=1
print(t)
#plt.figure()
#ax = plt.axes(aspect='equal')
for i in range(Nz):
    plt.pcolormesh(V[:,:,i])
    plt.pause(1)
#plt.pcolormesh(V.T ) 
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')                                       
#ax.set_title(r'$V(x,y,z)$')

    
