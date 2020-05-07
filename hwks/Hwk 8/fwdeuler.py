# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy as sc
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve

def xfrange(start, stop, step):
    i = 0
    while start + i * step < stop:
        yield start + i * step
        i += 1

wref = 104.72

G = np.arange(0,8.0,.1)

w = symbols('w')

V = 98.2+G[0]*(wref-w)

Te = (.75*1.25*V-(.75*1.25)*(.75*1.25)*w)/(.02*5.0)

Tm = .03*w*w/5.0
dw = Te-Tm


warr = np.array([])
tarr = np.array([])

gc = 0
for i in xfrange(0, 7.99, .1):
    print("At G = "+str(i)+" w = "+str(w))
    print("At G = "+str(i)+" dw/dt = "+str(dw))
    dw = Te-Tm
    sol = solve(dw)
    V = 98.2+G[gc]*(wref-w)
    gc+=1
    Te = (.75*1.25*V-(.75*1.25)*(.75*1.25)*w)/(.02*5.0)
    Tm = .03*w*w/5.0
    warr = np.append(warr,sol[1])
    tarr = np.append(tarr,.03*sol[1]**2)


fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Gain')
ax1.set_ylabel('Speed (RPM)', color=color)
ax1.plot(G, warr, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 
color = 'tab:blue'
ax2.set_ylim((280,350))
ax2.set_ylabel('Torque (Nm)', color=color)  # we already handled the x-label with ax1
ax2.plot(G, tarr, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()