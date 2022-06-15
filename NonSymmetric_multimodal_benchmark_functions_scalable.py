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


def Ackley4(x, lb=-10, ub=10):
    '''
        2020-3-6
        Ackley 1 Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
        Note:
            This function is not recommended to be involved in optimization
    '''
    d = len(x)
    y = 1.0
    for i in range(d-1):
        y += math.exp(-0.2*math.sqrt(math.pow(x[i], 2)+math.pow(x[i+1], 2)))+3*(
            math.cos(2*x[i])+math.sin(2*x[i+1]))
    return lb, ub, y


def Alpine2(x, lb=0, ub=10):
    '''
        2020-3-8
        Alpine 2 Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.999
    for i in range(d):
        y *= math.sqrt(x[i])*math.sin(x[i])
    y = math.pow(2.808, d)-y
    return lb, ub, y


def DeflectedCorrugatedSpring(x, lb=-0, ub=10):
    '''
        2020-7-18
        Deflected Corrugated Spring function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/238-deflected-corrugated-spring-function
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    a = 5
    k = 5
    for i in range(d):
        y1 += (x[i]-a)**2
    y = 1+0.1*y1-math.cos(k*math.sqrt(y1))
    return lb, ub, y


def EggHolder(x, lb=-512, ub=512):
    '''
        2020-3-10
        Egg Holder Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += -(x[i+1]+47)*math.sin(math.sqrt(math.fabs(x[i+1]+x[i]/2+47))
                                   )-x[i]*math.sin(math.sqrt(math.fabs(x[i]-(x[i+1]+47))))
    y += 959.64
    return lb, ub, y


def GeneralizedSchwefel2p26(x, lb=-500, ub=500):
    '''
        2020-7-19
        Generalized Schwefel's Function No.2.26
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/176-generalized-schwefel-s-problem-2-26
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += -x[i]*math.sin(math.sqrt(math.fabs(x[i])))
    y += 418.982887272433799807913601398*d
    return lb, ub, y


def Sinusoidal(x, lb=0, ub=180):
    '''
        2020-7-19
        Sinusoidal Function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/186-sinusoidal-function
    '''
    d = len(x)
    y = 0.0
    A = 2.5
    B = 5
    Z = 30
    y1 = 1.0
    y2 = 1.0
    for i in range(d):
        y1 *= math.sin(math.radians(x[i]-Z))
        y2 *= math.sin(math.radians(B*(x[i]-Z)))
    y = A+1-(A*y1+y2)
    return lb, ub, y


def Trigonometric2(x, lb=-math.pi, ub=math.pi):
    '''
        2020-7-11
        Trigonometric 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += 8*math.pow(math.sin(7*math.pow(x[i]-0.9, 2)), 2)+6*math.pow(
            math.sin(14*math.pow(x[0]-0.9, 2)), 2)+math.pow(x[i]-0.9, 2)
    return lb, ub, y


def XinSheYang7(x, lb=-10, ub=10):
    '''
        2020-7-19
        Xin-She Yang's Function No.07
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/263-xin-she-yang-s-function-no-07
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        u = np.random.uniform(0, 1)
        y += u*math.fabs(x[i]-1/(i+1))
    return lb, ub, y
