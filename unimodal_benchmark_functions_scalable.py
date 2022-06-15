'''
    Coder:
        Greenby
    Begin date:
        2020-3-3
    End date:
        2020-8-26
    Functions:
        1) Listed the unimodal benchmark functions with their names
        2) All of the unimodal benchmark functions are symmetric, continuous, scalable and have no flat-like peaks in their three dimensional profiles
        3) All of the information should be invoved, even with notes.
        4) All of the unimodal benchmark functions have one global optimum in the definitional domain
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


def Ackley1(x, lb=-100, ub=100):
    '''
        2020年3月6日
        Ackley 1 Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    for i in range(d):
        y1 += math.pow(x[i], 2)
        y2 += math.cos(2*math.pi*x[i])
    y = 20+math.exp(1)-20*math.exp(-0.02*math.sqrt(y1/d))-math.exp(y2/d)
    return lb, ub, y


def Exponential(x, lb=-3, ub=3):
    '''
        2020-3-10
        Exponential Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 2)
    y = 1-math.exp(-0.5*y)
    return lb, ub, y


def PowellSum(x, lb=-1, ub=1):
    '''
        2020-4-8
        Powell Sum function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(math.fabs(x[i]), i+1)
    return lb, ub, y


def Sargan(x, lb=-100, ub=100):
    '''
        2020-5-20
        Sargan function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y1 = 0.0
        for j in range(d):
            if i != j:
                y1 += x[i]*x[j]
        y += d*(math.pow(x[i], 2)+0.4*y1)
    return lb, ub, y


def Schwefel2p20(x, lb=-100, ub=100):
    '''
        2020-5-21
        Schwefel 2.20 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.fabs(x[i])
    return lb, ub, y


def Schwefel2p21(x, lb=-100, ub=100):
    '''
        2020-5-21
        Schwefel 2.21 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        yt = math.fabs(x[i])
        if yt > y:
            y = yt
    return lb, ub, y


def Sphere(x, lb=-100, ub=100):
    '''
        2020年3月3日
        Sphere function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 2)
    return lb, ub, y


def Step(x, lb=-100, ub=100):
    '''
        2020-7-10
        Step function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.floor(math.fabs(x[i]))
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


def Step3(x, lb=-100, ub=100):
    '''
        2020-7-10
        Step 3 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.floor(math.pow(x[i], 2))
    return lb, ub, y
