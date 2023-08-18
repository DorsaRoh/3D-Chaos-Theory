import time
startTime = time.time()
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
from scipy.integrate import solve_ivp

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.integrate import odeint
from matplotlib import animation
from matplotlib.colors import cnames
from matplotlib import cm
from scipy import integrate
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib as mpl
 
def main(inputs):
    global t
    global tf
    global h
    t = inputs['t']
    tf = inputs['tf']
    h = inputs['h']
    #These variables were used since they can be easily found for comparison, for example, in Wikipedia under the Lorenz system article
 
    #Derivative function to work with RK4 loop
    def derivative(p,t):
        x = p[0]
        y = p[1]
        z = p[2]
        global s
        global r
        global b
        s = inputs['s']
        r = inputs['r']
        b = inputs['b']
        return np.array([s * (y - x), x * (r - z) - y, (x * y) - (b * z)])
 
    time = np.array([]) #Empty time array to fill for the x-axis
    x = np.array([]) #Empty array for x values
    y = np.array([]) #Empty array for y values
    z = np.array([]) #Empty array for z values
    p = np.array([1.0, 1.0, 1.0]) #Initial conditions array
 
    for i in range(True):
        while (t <= tf ):
            #Appending values to graph
            time = np.append(time, t)
            z = np.append(z, p[2])
            y = np.append(y, p[1])
            x = np.append(x, p[0])
            #RK4 Step method
            k1 = h*derivative(p,t)
            k2 = h*derivative(p+k1/2,t+h/2)
            k3 = h*derivative(p+k2/2,t+h/2)
            k4 = h*derivative(p+k3,t+h)
            p += (k1+2*k2+2*k3+k4)/6
            #Updating time value with step size
            t = t + h
 
    n = 100
    cmap1 = plt.cm.spring
    cmap2 = plt.cm.winter
    cmap3 = plt.cm.summer
 
    plt8, (ax3,ax2,ax1) = plt.subplots(1,3, figsize = (15, 5))
    ax1.plot(x, y, color=cmap1(i/n))
    ax1.set_title("X Axis , Y Axis")
    ax2.plot(x, z, color=cmap2(i/n))
    ax2.set_title("X Axis , Z Axis")
    ax3.plot(y, z, color=cmap3(i/n))
    ax3.set_title("Y Axis , Z Axis")
    plt.show()
 
 
    plot8 = plt_show(plt8, 900)
