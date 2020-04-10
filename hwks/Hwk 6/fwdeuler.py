# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy as sc
import numpy as np
#import matplotlib.pyplot as plt

def xfrange(start, stop, step):
    i = 0
    while start + i * step < stop:
        yield start + i * step
        i += 1

w = 120*sc.pi

dd = w - 120*sc.pi

T = .6

d = np.arcsin(-.6/2)

dw = -2*np.sin(d)-T

T = 1.0

dd = w - 120*sc.pi
dw = -2*np.sin(d)-T


for i in xfrange(0, 0.006, .001):
    print("At t = "+str(i)+" Delta = "+str(d))
    print("At t = "+str(i)+" w = "+str(w))
    print("At t = "+str(i)+" dDelta/dt = "+str(dd))
    print("At t = "+str(i)+" dw/dt = "+str(dw))
    d=d+.001*dd
    w = w+.001*dw
    dd = w - 120*sc.pi
    dw = -2*np.sin(d)-T