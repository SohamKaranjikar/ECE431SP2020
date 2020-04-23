# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy as sc
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import *

def xfrange(start, stop, step):
    i = 0
    while start + i * step < stop:
        yield start + i * step
        i += 1

ws = 120*np.pi
wi = 120*np.pi
If = 1.2
Lasf = .4
P = 6
xs = 9
Vt = 230/np.sqrt(3)
D = .3
J = .4
Ef = ws*Lasf*If/np.sqrt(2)
deltaT = 0
Te = (3*(Vt)*Ef/((2/P)*ws*xs))*np.sin(-deltaT)
Td = -D*(2/P)*(wi-ws)
dDelta = wi - ws
Pm = 0
Tm = -Pm/((2/P)*(ws))
dwi = (1/J)*(6/2)*(Te+Td+Tm)
wiarr = np.array([])
deltaTarr = np.array([])
Iaarr = np.array([])
t = np.arange(0,20.0005,.0005)

# for i in xfrange(0, 20.0005, .0005):
#     if(i == .01):
#         Pm = 4210
#     wi = wi + dwi*.0005
#     deltaT = deltaT + dDelta*.0005
#     wiarr = np.append(wiarr,wi)
#     deltaTarr = np.append(deltaTarr,deltaT)
#     Ia = abs((Vt - (Ef*np.cos(-deltaT)+Ef*1j*np.sin(-deltaT)))/xs)
#     Iaarr = np.append(Iaarr, Ia)
#     Te = (3*(Vt)*Ef/((2/P)*ws*xs))*np.sin(-deltaT)
#     Td = -D*(2/P)*(wi-ws)
#     Tm = -Pm/((2/P)*(ws))
#     dDelta = wi - ws
#     dwi = (1/J)*(P/2)*(Te+Td+Tm)

# plt.figure(0)
# plt.plot(t,wiarr)
# plt.ylabel('Speed')
# plt.xlabel('time')
# plt.suptitle('Speed Vs. time')
# plt.savefig("svt5")

# plt.figure(1)
# plt.plot(t,deltaTarr)
# plt.ylabel('Delta')
# plt.xlabel('time')
# plt.suptitle('Delta Vs. time')
# plt.savefig("dvt5")


# plt.figure(2)
# plt.plot(wiarr,deltaTarr)
# plt.ylabel('Delta')
# plt.xlabel('Speed')
# plt.suptitle('Delta Vs. Speed')
# plt.savefig("dvs5")

# plt.figure(3)
# plt.plot(t,Iaarr)
# plt.ylabel('Ia')
# plt.xlabel('time')
# plt.suptitle('Ia Vs. time')
# plt.savefig("ivt5")

#Equal area criteria
Pe = 3*(Ef*Vt/xs)
def findDelta(MaxLoad,i):
    if(i==0):
        d= Symbol('d')
        e1 = Eq(MaxLoad - Pe*sin(d))
        ans = solve(e1, d)
    else:
        d= Symbol('d')
        e1 = Eq(MaxLoad - Pe*sin(d))
        ans = solve(e1, d)
    return ans

def integrandA1(x,MaxLoad):
    return MaxLoad - Pe*sin(x)

def integrandA2(x,MaxLoad):
    return Pe*sin(x)-MaxLoad


for x in xfrange(0, Pe, 1):
    delta = findDelta(x,0)
    a = quad(integrandA1, 0, delta, args=(x))
    b = quad(integrandA2, delta, 3.1416 - delta, args=(x))
    if(abs(a-b)<5):
        print(x)



