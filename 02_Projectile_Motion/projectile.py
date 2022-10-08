#!/usr/bin/env python3

import numpy as np
import pylab as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

import sys

def comp_x_y_t_max(params):
    v0,theta=params
    angle=theta*np.pi/180

    st=np.sin(angle)
    s2t=np.sin(2*angle)

    st2=st**2
    ymax= v0**2 * st2 /(2*g)
    xmax= v0**2 * s2t /g
    tmax= 2*v0* st/g
    return (xmax, ymax, tmax)

def comp_pos(params, t):
    v0,theta=params
    angle=theta*np.pi/180

    vx= v0 * np.cos(angle)
    vy= v0 * np.sin(angle)
    x =  vx * t
    y =  vy * t - 0.5 * g * t**2
    return (x,y)

def comp_animation(params):
    v0,theta=params
    angle=theta*np.pi/180

    xmax, ymax, tmax =comp_x_y_t_max(params)

    fig,ax=plt.subplots()
    xdata,ydata=[],[]
    ln, = plt.plot([],[], '-o', color='maroon')
    plt.xlabel("Horizontal distance", fontsize=14)
    plt.ylabel("Height", fontsize=14)
    plt.title("Projectile motion at $\\theta =$ "+str(theta)+'$\degree $ and $v_{0}$='+str(v0) , fontsize=14)

    def set_init():
        ax.set_xlim(0, 1.1*xmax)
        ax.set_ylim(0, 1.1*ymax)

    def update(frame):
        (x, y)=comp_pos(params, frame)
        xdata.append(x)
        ydata.append(y)
        ln.set_data(xdata, ydata)

    my_ani = FuncAnimation(fig, update, frames=np.linspace(0, tmax, 20), init_func=set_init())
    my_ani.save('./figs/anim.gif', writer='MovieWriter', fps=5)
    plt.show()
    return my_ani
    #my_ani.save('anim.gif', writer='MovieWriter', fps=5)

def plot_with_angles(params):
    v0,theta=params
    thetaL=[30, 60, 45]
    plt.title('projectile motion at different angles', fontsize=14)
    for theta in thetaL:
        params=[v0, theta]
        xmax, ymax, tmax =comp_x_y_t_max(params)
        tL=np.linspace(0, tmax, 45)
        (x, y)=comp_pos(params, tL)
        plt.plot(x, y, ls='--',label='$\\theta=$'+str(theta)+'$\degree$')
        plt.legend(frameon=False, fontsize=14)
        plt.axis( [0, 11, 0, 4 ])
    plt.xlabel("Horizontal distance (m)", fontsize=14)
    plt.ylabel("Height (m)", fontsize=14)
    plt.savefig('./figs/plot_with_angle.pdf')
    plt.show()


if __name__=="__main__":
    
    import time
    time.sleep(1)

    #-------input parameters--------
    v0=10; theta=10; g=9.81
    ################

    params=[v0, theta]
    #my_ani=comp_animation(params)
    plot_with_angles(params)


