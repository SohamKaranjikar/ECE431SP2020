#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:27:05 2020

@author: Soham
"""


from matplotlib import pyplot as plt
import numpy as np

T = np.array([0.000,
0.500,
1.000,
1.500,
2.000,
2.500,
3.000,
3.500,
4.000,
4.500,
5.000,
5.500,
6.000])

Ia = np.array([.677,
        .94,
        1.2,
        1.46,
        1.73,
        2,
        2.27,
        2.55,
        2.83,
        3.11,
        3.39,
        3.68])

V = np.array([239,
        239,
        238.7,
        238.7,
        238.6,
        238,
        238,
        238,
        237.9,
        237.7,
        237.6,
        237])

Speed = np.array([1200,
1196,
1194,
1190,
1188,
1186,
1184,
1184,
1182,
1182,
1182,
1184,
1186])

w = Speed*2*np.pi/60

Ian = (240-w*2.05*(.8)-w*.064)/(w*.12+.75+5)

Tn = .064*Ian+2.05*Ian*.8+.12*Ian*Ian

plt.plot(Speed,Tn, label="Theo")
plt.plot(Speed,T, label="Data")
plt.legend()
