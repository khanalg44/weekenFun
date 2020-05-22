#!/usr/bin/env python


def q1(n, a, b):
    # base case
    if n==0:
        return 0.5
    else:
        #return q1(n-1,a,b)
        
        return q1(n-1,a,b)



if __name__=="__main__":


    n=4;
    beta=0;
    alpha=0.1;
    #print q1(n,alpha,beta)
    
    for i in range(n):
        print q1(n,alpha,beta)
