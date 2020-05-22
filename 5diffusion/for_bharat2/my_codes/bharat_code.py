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

def Sin(x,N):
	tot=0
	tot =0.0
	for i in range(N):
		val= (-1)**i * x**(2*i+1)/(np.math.factorial(2*i+1))
		tot +=val
	return tot

if __name__=="__main__":
	#Q2 test
	#print np.sin(np.pi/2)
	#sys.exit()
	x=np.pi/2
	my_func=[]
	act_func=[]
	NN=range(1,60,10)
	print NN
	for N in NN:
		my_func.append(Sin(x,N))
		act_func.append(np.sin(x))	
	pl.plot(NN,my_func,'-o',label='my_function')
	pl.legend(loc='best')
	pl.plot(NN,act_func,'--',label='actual function')
	pl.legend(loc='best')
	pl.show()
