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


def Beale(x, lb=-100, ub=100):
    '''
        2020-3-8
        Beale function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(1.5-x[0]-x[0]*x[1], 2)+math.pow(2.25-x[0]-x[0] *
                                                     math.pow(x[1], 2), 2)+math.pow(2.625-x[0]-x[0]*math.pow(x[1], 3), 2)
    return lb, ub, y


def Easom(x, lb=-0, ub=6):
    '''
        2020-3-9
        Easom function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -math.cos(x[0])*math.cos(x[1]) * \
            math.exp(-math.pow(x[0]-math.pi, 2)-math.pow(x[1]-math.pi, 2))
    y += 1
    return lb, ub, y


def Engvall(x, lb=-100, ub=100):
    '''
        2020-7-12
        Engvall's function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/116-engvall-s-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = x[0]**4+x[1]**4+2*x[0]**2*x[1]**2-4*x[0]+3
    return lb, ub, y


def GoldsteinPrice(x, lb=-20, ub=20):
    '''
        2020-3-18
        Goldstein Price function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (1+math.pow(x[0]+x[1]+1, 2)*(19-14*x[0]+3 *
                                         math.pow(x[0], 2)-14*x[1]+6*x[0]*x[1]+3*math.pow(x[1], 2)))*(30+math.pow(2*x[0]-3*x[1], 2)*(18-32*x[0]+12*math.pow(x[0], 2)+48*x[1]-36*x[0]*x[1]+27*math.pow(x[1], 2)))
    y -= 3
    return lb, ub, y


def MovedAxisParallelHyperEllipsoid(x, lb=-100, ub=100):
    '''
        2020-7-19
        Moved-Axis Parallel Hyper-Ellipsoid Function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/230-moved-axis-parallel-hyper-ellipsoid-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += ((i+1)*(x[i]-5*(i+1)))**2
    return lb, ub, y


def PowellBadlyScaled(x, lb=-10, ub=10):
    '''
        2020-7-18
        Powell's Badly Scaled function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/65-powell-s-badly-scaled-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (10**4*x[0]*x[1]-1)**2+(math.exp(-x[0])+math.exp(-x[1])-1.001)**2
    return lb, ub, y


def Price3(x, lb=-100, ub=100):
    '''
        2020-4-8
        Price 3 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 100*math.pow(x[1]-math.pow(x[0], 2), 2)+6 * \
            math.pow(6.4*math.pow(x[1]-0.5, 2)-x[0]-0.6, 2)
    return lb, ub, y


def Quadratic(x, lb=-100, ub=100):
    '''
        2020-4-9
        Quadratic function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -3803.84-138.08*x[0]-232.92*x[1]+128.08 * \
            math.pow(x[0], 2)+203.64*math.pow(x[1], 2)+182.25*x[0]*x[1]
    y += 3873.7243
    return lb, ub, y


def Schwefel2p4(x, lb=-100, ub=100):
    '''
        2020-5-20
        Schwefel 1.2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i]-1, 2)+math.pow(x[0]-math.pow(x[i], 2), 2)
    return lb, ub, y


def Schwefel2p25(x, lb=-100, ub=100):
    '''
        2020-5-21
        Schwefel 2.25 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i]-1, 2)+math.pow(x[0]-math.pow(x[i], 2), 2)
    return lb, ub, y


def Step2(x, lb=-100, ub=100):
    '''
        2020-7-10
        Step 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(math.floor(x[i]+0.5), 2)
    return lb, ub, y


def WayburnSeader3(x, lb=-100, ub=100):
    '''
        2020-7-18
        Wayburn-Seader's Function No.03
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/277-wayburn-seader-s-function-no-03
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 2/3*x[0]**3-8*x[0]**2+33*x[0]-x[0] * \
            x[1]+5+((x[0]-4)**2+(x[1]-5)**2-4)**2
    y -= 19.105879794567979
    return lb, ub, y


def Zettl(x, lb=-10, ub=10):
    '''
        2020-7-11
        Zettl function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(math.pow(x[0], 2)+math.pow(x[1], 2)-2*x[0], 2)+0.25*x[0]
    y += 0.003791
    return lb, ub, y
