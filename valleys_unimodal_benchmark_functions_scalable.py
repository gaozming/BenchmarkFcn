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


def BentCigar(x, lb=-100, ub=100):
    '''
        2020-7-18
        Bent Cigar function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/164-bent-cigar-function
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    for i in range(d):
        if i == 0:
            y += x[0]**2
        else:
            y1 += x[i]**2
    y += y1*10**6
    return lb, ub, y


def GeneralizedModifiedRosenbrock2OrHollowGroundBentKnifeEdge(x, lb=-100, ub=100):
    '''
        2020-7-18
        Generalized Modified Rosenbrock's Function No.02 (or Hollow-Ground Bent Knife-Edge Function)
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/171-generalized-modified-rosenbrock-s-no-2-or-hollow-ground-bent-knife-edge-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += 100*math.sqrt(math.fabs(x[i+1]-x[i]**2))+(1-x[i])**2
    y -= 1
    return lb, ub, y


def GeneralizedRosenbrockValleyOrBananaOrDeJong2(x, lb=-100, ub=100):
    '''
        2020-7-18
       Generalized Rosenbrock's Valley (Banana or 2nd De Jong's) Function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/175-generalized-rosenbrock-s-valley-banana-or-2nd-de-jong-s-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += 100*(x[i+1]-x[i]**2)**2+(x[i]-1)**2
    return lb, ub, y


def Quartic(x, lb=-100, ub=100):
    '''
        2020-4-9
        Quartic function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += i*math.pow(x[i], 4)
    return lb, ub, y


def Schwefel1p2(x, lb=-100, ub=100):
    '''
        2020-5-20
        Schwefel 1.2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    a = 2
    for i in range(d):
        y1 = 0
        for j in range(i):
            y1 += x[j]
        y += math.pow(y1, 2)
    return lb, ub, y


def SumSquares(x, lb=-100, ub=100):
    '''
        2020-5-25
        Sum Squares function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += i*math.pow(x[i], 2)
    return lb, ub, y


def Zakharov(x, lb=-10, ub=10):
    '''
        2020-7-11
        Zakharov function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    for i in range(d):
        y1 += math.pow(x[i], 2)
        y2 += (i+1)*x[i]
    y = y1+math.pow(y2/2, 2)+math.pow(y2/2, 4)
    return lb, ub, y
