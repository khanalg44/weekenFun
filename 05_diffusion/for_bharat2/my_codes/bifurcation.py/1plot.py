import matplotlib.pyplot as plt
import numpy as np
def iter_map(a,N):
    x=np.zeros(N)
    x[0]=0.5
    for i in range(N-1):
        d=(a*x[i]*2**n +b)%2**n
        x[i+1]=d/2**n
    return x

N=400
n=8
colors = ["#2078B5", "#FF7F0F", "#2CA12C", "#D72827", "#9467BE"]

a=[1,2,3]
plt.figure()
fig,axes=plt.subplots(len(a),1, sharex=True, sharey=False)
for b in [0,1]:
	for i in range(len(axes)):
		x=iter_map(a[i],N)
  		axes[i].plot(np.arange(0,N),x, color=colors[i], markeredgecolor=colors[i])
		axes[i].legend(loc='best', frameon=True)
		axes[i].set_ylabel('x')
		axes[i].set_xlabel('iter')	

plt.show()
plt.legend()
