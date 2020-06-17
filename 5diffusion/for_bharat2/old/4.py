#!/usr/bin/env python

from math import *
import numpy as np
from matplotlib import pylab as plt
from fractions import Fraction as Fr


def fsin(x,epsilon):
    n = 0
    term =((-1)**n)*(x**(1+2*n))/factorial(1+2*n)
    s = term
    while abs(term/s) > epsilon:
        n = n + 1
        term =((-1)**n)*(x**(1+2*n))/factorial(1+2*n)
        s = s + term
    return s, n

def fcos(x,epsilon):
    n = 0
    term =((-1)**n)*(x**(2*n))/factorial(2*n)
    s = term
    while abs(term/s) > epsilon:
        n = n + 1
        term =((-1)**n)*(x**(2*n))/factorial(2*n)
        s = s + term        
    return s, n

def ftan(x,N):
    def B2n(n):
        A = [0] * (n+1)
        for m in range(n+1):
            A[m] = Fr(1, m+1)
            for j in range(m, 0, -1):
              A[j-1] = j*(A[j-1] - A[j])
        return A[0] 

    n = 1
    term=B2n(2*n)*(((-4)**n)*(1-(4)**n)*(x**(2*n-1)))/factorial(2*n)
    s = term
    while abs(term/s) > epsilon:
        n = n + 1
        term=B2n(2*n)*(((-4)**n)*(1-(4)**n)*(x**(2*n-1)))/factorial(2*n)
        s = s + term
    return s, n


if __name__=="__main__":
	x = float(raw_input("Enter value of x (in degree) =  "))
	x = x*pi/180
	print "   epsilon      sin(x)   cos(x)   tan(x)"
	for k in range(1,9):
		epsilon = 10**(-k)
		sinx, n1 = fsin(x,epsilon)
		cosx, n2 = fcos(x,epsilon)
		tanx, n3 = ftan(x,epsilon)
		print "%10.1e %8d %8d %8d" %(epsilon,n1,n2,n3)