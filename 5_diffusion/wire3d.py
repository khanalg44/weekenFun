#!/usr/bin/env python
from scipy import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def main():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Grab some test data.
    x=linspace(-1,1,5)
    y=linspace(-1,1,5)
    xp=x.transpose()
    xx,yy=np.meshgrid(x,y)

    zz=xx**2+yy**2
    #X, Y, Z = axes3d.get_test_data(0.05)

    print xx
    print
    print yy
    print 
    print xp
    print 
    print zz

    # Plot a basic wireframe.
    ax.plot_wireframe(xx, yy, zz)#, rstride=10, cstride=10)

    #plt.show()


if __name__=="__main__":
    main()
