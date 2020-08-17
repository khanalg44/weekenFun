#!/usr/bin/env python

import pylab as pl
import numpy as np
from scipy import weave
import sys


def logistic(mu,n):
    if n==0:
        #return np.random.random()
        return 0.01
    else:
        return mu*logistic(mu,n-1)*(1.0-logistic(mu,n-1))


def test1():
    lst=[]
    mu_list=[0.5, 1.0, 1.5, 3.3, 3.45, 3.55, 3.8]
    #mu_list=[0.5, 1.0, 1.5]
    NN=20
    for mu in mu_list:
        lst=[] 
        for n in range(NN):
            lst.append(logistic(mu,n))
        pl.plot(range(NN),lst,'-o',label='$\mu=$'+str(mu))
        pl.legend(loc='best')
        pl.show()

# Bifurcation plot starts from here.

def logistic_map(r,x):
    return r*x*(1.0-x)

def bifurcation():
    rr=np.linspace(2.4,4.0,100)
    for r in rr:
        # start with some initial state
        s=0.1
        # discard some initial states (before convergence)
        for i in range(20):
            s = logistic_map(r,s)   
        # Once the state converges
        # find all possible states we can have.
        # for that set up a cut off (=1000) in this case
        r_vals=[];r_state=[]
        for i in range(1000):
            s=logistic_map(r,s)
            r_vals.append(r)
            r_state.append(s)
        pl.plot(r_vals,r_state,'k,')
        #pl.plot(r_vals,r_state,ls=':',ms=0.1)
        #pl.plot(r_vals,r_state,ms=0.2,c='black',lw=0.5, ls='--')
        #pl.scatter(r_vals,r_state,marker='o',color='black')
        pl.xlim([2.4,4.01])
    pl.show()

def bifurcation2():
    rr=np.linspace(2.4,4.0,10)
    for r in rr:
        # start with some initial state
        s=0.1
        # discard some initial states (before convergence)
        for i in range(10):
            s = logistic(r,i)   
        # Once the state converges
        # find all possible states we can have.
        # for that set up a cut off (=1000) in this case
        r_vals=[];r_state=[]
        for j in range(5 ):
            s=logistic(r,s)
            r_vals.append(r)
            r_state.append(s)
        pl.plot(r_vals,r_state,'k,')
        #pl.plot(r_vals,r_state,ls=':',ms=0.1)
        #pl.plot(r_vals,r_state,ms=0.2,c='black',lw=0.5, ls='--')
        #pl.scatter(r_vals,r_state,marker='o',color='black')
        pl.xlim([2.4,4.01])
    pl.show()
if __name__=="__main__":
    sys.setrecursionlimit(500)
    bifurcation2()
    #bifurcation()
    #test1()
