from math import *
from numpy import *
import matplotlib.pyplot as plt
from fractions import Fraction as Fr

print "Trigonometic fucntion from Taylor's series"

x = 45
N = 30
x = x*pi/180

exact_sin = sin(x)
exact_cos = cos(x)
exact_tan = tan(x)

def fsin(x,N):
    nn = []
    sinx = []
    n = 0
    term =((-1)**n)*(x**(1+2*n))/factorial(1+2*n)
    s = term
    for n in range(1,N+1):
        term =((-1)**n)*(x**(1+2*n))/factorial(1+2*n)
        s = s + term
        nn.append(n)
        sinx.append(s)
    return nn,sinx

def fcos(x,N):
    nn = []
    cosx = []
    n = 0
    term=((-1)**n)*(x**(2*n))/factorial(2*n)
    s = term
    for n in range(1,N+1):
        term=((-1)**n)*(x**(2*n))/factorial(2*n)
        s = s + term
        nn.append(n)
        cosx.append(s)
    return nn,cosx
    
n1, sinx = fsin(x,N)
n2, cosx = fcos(x,N)

def b(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0]


tanx=[]
nn=[]
s=0
for k in range (N):
	p=b(2*k)*(((-4)**k)*(1-(4)**k)*(x)**(2*k-1))/factorial (2*k)
	s+=p
	nn.append(k)
	tanx.append(s)


fig1 = plt.figure('%error of sin(x)')
sinx_err = []
for i in range(N):
   error = (exact_sin-sinx[i])/exact_sin*100
   sinx_err.append(error)
plt.plot(n1,sinx_err,'r--o',label='%error')
plt.legend()
plt.xlabel('Number of term (N)')
plt.ylabel('%error')
plt.show()

fig2 = plt.figure('%error of cos(x)')
cosx_err = []
for i in range(N):
   error = (exact_cos-cosx[i])/exact_cos*100
   cosx_err.append(error)
plt.plot(n1,cosx_err,'r--o',label='%error')
plt.legend()
plt.xlabel('Number of term (N)')
plt.ylabel('%error')
plt.show()

fig3 = plt.figure('%error of tan(x)')
tanx_err = []
for i in range(N):
   error = (exact_tan-tanx[i])/exact_tan*100
   tanx_err.append(error)
plt.plot(nn,tanx_err,'r--o',label='%error')
plt.legend()
plt.ylim(-20,25)
plt.xlabel('Number of term (N)')
plt.ylabel('%error')
plt.show()
