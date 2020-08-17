import matplotlib.pyplot as plt
import numpy as np 

dt=0.1
tmax=12
v=7
m=70
rho=1.2
A=0.33
P=13
p=400
f=p/v
c=1
t=np.arange(0,tmax,dt)
v=np.zeros_like(t)
v[0]=7

for i in range (len(t)-1):
  
  v[i+1] = v[i] + (f/m)*dt - c*rho*A*v[i]**2*dt/(2.0*m)

plt.figure ()
plt.plot(t,v)
plt.legend(loc='lower right')
plt.show()
