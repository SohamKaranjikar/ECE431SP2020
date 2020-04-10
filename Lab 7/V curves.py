#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 05:08:31 2020

@author: Soham
"""

#import scipy as sc
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.get_backend()
def xfrange(start, stop, step):
    i = 0
    while start + i * step < stop:
        yield start + i * step
        i += 1

If = [.37,.64,.78,.9,.97,1.05,1.1,1.12,1.2,1.2]
V = [171,171,171,171,171,171]
Q0 = [706,176.9,-202.8,-496.8,-704.6,-866.7,-829.4,-1072,-1137.6]

Q1 = [728.9733054097386,
142.80504192779745,
114.70985917522509,
-426.6261595354884,
-602.2858374559374,
-767.0267791935297,
-892.7031309455568,
-924.8137271905083,
-1080.2426949533144]

Q2 = [821.2207194171369,
215.12793867835927,
165.69996982498193,
-347.84525295021626,
-569.507260708764,
-719.6304607227239,
-824.7934771808029,
-929.5164979708535]

Q3 = [298.17357361107656,
123.63041696928786,
-298.17357361107656,
-468.3486201538336,
-660.9867396551915,
-786.4414027758205]

delta = [0,5*np.pi/180,10*np.pi/180,15*np.pi/180,22*np.pi/180]
delta2= [0,.2567,.1371,.1171,.1125]
Pmax = [0,-124.6,-354.5,-505.4,-599.5]
Pin = [0,0,0,0,0]

Ia=[2.6,2.4,2.6,2.9,3.3,3.6]
P = [90,-30,-115,-205,-290]
for i in range(len(P)):
    S = np.sqrt(3)*V[i]*Ia[i]
    Q = S**2-P[i]**2
    #print(np.sqrt(Q))
print(2**3)

for i in range(len(Pmax)):
    Pin[i] = Pmax[i]*np.sin(delta2[i])
    print(Pin[i])
    
Pexp = [90,-30,-115,-205,-290]

plt.plot(delta,Pin,label="Theoretical")
plt.plot(delta,Pexp,label="Experimental")
plt.legend()