import numpy as np
import matplotlib.pyplot as plt
def iter_map(b,N):
    x = np.zeros(N)
    x[0] = 0.5
    for i in range(N-1):
        x[i+1]=(int((x[i])*(2**n) +b)%(2**n)) /(2**n)
    return x

if __name__=="__main__":
  
    a=3       
    N=100
    n=8
    plt.figure(1)
   
    for b in [7,9,11,13]:
        fig,axes=plt.subplots(4,1,sharex=True, sharey=True )
        for i in range(len(axes)):
            x=iter_map(b[i],N)
            axes[i].plot(np.arange(0,N) ,x)
            axes[i].legend(loc='best')
            axes[i].set_ylabel('x')
            axes[i].set_ylim(0,1)
            axes[i].set_xlim(0,N)
            axes[i].set_xlabel('iteration')


plt.show()