#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as pl
import sys

def Sin(x,N):
	# start the full sum with a zero value
	tot=0
	# since we'll some N value we'll calculate each term separately and add them to the tot
	for k in range(N):
		# range(N)=[0,1,2,3,4.......N-1]
		#evaluate the term for each intermediate k such that k=1.. N-1
		val= (-1)**k * x**(2*k+1)/(np.math.factorial(2*k+1))
		#add this value to total
		tot = tot+val
	# Now return the total value
	return tot

def fSin(x,epsilon=0.1):
	n=0
	v_n= (-1)**n * x**(2*n+1)/(np.math.factorial(2*n+1))
	tot = 0.0
	ratio=float(tot)/float(v_n)
	while ratio<epsilon:
		#print n, v_n, tot, ratio
		n+=1
		tot+= (-1)**n * x**(2*n+1)/(np.math.factorial(2*n+1))
		if n>50:
			print 'n exceeds 50.'
			break
	print tot
	
def for_Q3():
	fSin(np.pi/2.0,0.00001)

def FOR_Q2():
	#Q2 test
	# some value of x, we are plotting  sin(x,N) vs N for a fixed value of x
	x=np.pi/2
	# I want to store all the values evaluated for each N
	# so I define some empty lists for both my_function and actual function
	my_func=[]  # empty list
	#will later append the values for Sin(x) for different N values to these empty list
	# lets take some values of N
	# range is a python defined module 
	# this case it'll take 1,11,21,... up to 60
	NN=range(10)
	# You want to calculate for each N value
	for N in NN:
		my_func.append(Sin(x,N))

	#sys.exit()
	pl.plot(NN,my_func,'-o',color='k',label='my_function')
	pl.legend(loc='best')
	pl.axhline(y=1.0,color='blue',lw=1.5,ls='--')
	pl.show()

	

if __name__=="__main__":
	
	for_Q3()
