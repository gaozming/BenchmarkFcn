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


def ChungReynolds(x, lb=-100, ub=100):
    '''
        2020-3-9
        Chung Reynolds Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 2)
    y = math.pow(y, 2)
    return lb, ub, y


def Csendes(x, lb=-100, ub=100):
    '''
        2020-3-10
        Csendes Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 6)*(2+math.sin(1/x[i]))
    return lb, ub, y


def Holzman2(x, lb=-100, ub=100):
    '''
        2020-7-19
        Holzman's Function No.02
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/272-holzman-s-function-no-02
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += (i+1)*x[i]**4
    return lb, ub, y


def HyperEllipsoid(x, lb=-100, ub=100):
    '''
        2020-7-19
        Hyper-Ellipsoid Function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/177-hyper-elipsoid-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += (i+1)**2*x[i]**2
    return lb, ub, y


def SchumerSteiglitz2(x, lb=-100, ub=100):
    '''
        2020-5-20
        Revised on 2020-7-19
        Schumer Steiglitz function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
        And https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/242-schumer-steiglitz-s-function-no-2
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 4)
    return lb, ub, y


def Schwefel(x, lb=-100, ub=100):
    '''
        2020-5-20
        Schwefel function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    a = 2
    for i in range(d):
        y += math.pow(x[i], 2)
    y = math.pow(y, 2)
    return lb, ub, y


def Schwefel2p22(x, lb=-100, ub=100):
    '''
        2020-5-21
        Schwefel 2.22 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y1 = 0.0
    y2 = 1.0
    for i in range(d):
        y1 += math.fabs(x[i])
        y2 *= math.fabs(x[i])
    y = y1+y2
    return lb, ub, y


def Schwefel2p23(x, lb=-100, ub=100):
    '''
        2020-5-21
        Schwefel 2.23 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 10)
    return lb, ub, y
