'''
    Coder: 
        Greenby
    Begin date: 
        2020-3-6
    End date:

    Functions:
        1) Listed the unimodal  basin dimensionality benchmark functions with their names
        2) All of the unimodal  basin dimensionality benchmark functions are continuous, scalable and have no flat-like peaks in their three dimensional profiles
        3) All of the information should be invoved, even with notes.
    Notes:
        1) All of the notes should be written in English in order to communicated.
        2) All of the functions should be named with English and not serials
        3) All of the source of functions should be mentioned here
        4) No main functions and other self defined functions should be involved here.
'''

# imports
import numpy as np
import math
import os
import sys
import io
import random

# random distribution
random.seed(0)


def JennrichSampson(x, lb=-1, ub=1):
    '''
        2020-7-11
        jennrich-Sampson's function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/134-jennrich-sampson-s-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        for i in range(10):
            y += (2+2*(i+1)-(math.exp((i+1)*x[0])+math.exp(i+1)*x[1]))**2
    y -= 124.36218235561473896
    return lb, ub, y


def Mishra8OrDecanomial(x, lb=-4, ub=3):
    '''
        2020-7-15
        Mishra's Function No.8 or Decanomial function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/49-mishra-s-function-no-8-or-decanomial-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        g = x[0]**10-20*x[0]**9+180*x[0]**8-960*x[0]**7+3360*x[0]**6-8064 * \
            x[0]**5+13340*x[0]**4-15360*x[0]**3+11520*x[0]**2-5120*x[0]+2624
        h = x[1]**4+12*x[1]**3+54*x[1]**2+108*x[1]+81.0
        y = 0.0001*(math.fabs(g)+math.fabs(h))**2
    return lb, ub, y


def Schwefel2p36(x, lb=-0, ub=100):
    '''
        2020-7-10
        Schwefel 2.36 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -x[0]*x[1]*(72-2*x[0]-2*x[1])+3456
    return lb, ub, y


def Simpletonn(x, lb=-0, ub=10):
    '''
        2020-7-19
        Simpleton-n Function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/273-simpleton-n-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y -= x[i]
    y += 10*d
    return lb, ub, y
