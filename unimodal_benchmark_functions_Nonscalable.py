'''
    Coder:
        Greenby
    Begin date:
        2020-3-6
    End date:
        2020-8-26
    Functions:
        1) Listed the unimodal fixed dimensionality benchmark functions with their names, only two-dimensional are invovled here.
        2) All of the unimodal fixed dimensionality benchmark functions are symmetric, continuous,  and have no flat-like peaks in their three dimensional profiles
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


def Ackley2(x, lb=-100, ub=100):
    '''
        2020年3月6日
        Ackley 1 Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 200-200 * \
            math.exp(-0.02*math.sqrt(math.pow(x[0], 2)+math.pow(x[1], 2)))
    return lb, ub, y


def BananaShape(x, lb=-3, ub=3):
    '''
        2020-7-11
        Banana Shape function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/48-banana-shape-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 25-100 / \
            (10*math.pow(math.pow(x[0]+1, 2) -
                         math.pow(x[1]+1, 2), 2)+math.pow(x[0], 2)+4)
    return lb, ub, y


def Bartels_Conn(x, lb=-100, ub=100):
    '''
        2020-3-8
        Bartels Conn function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.fabs(math.pow(x[0], 2)+math.pow(x[1], 2)+x[0]*x[1]) + \
            math.fabs(math.sin(x[0]))+math.fabs(math.cos(x[1]))
    y -= 1
    return lb, ub, y


def Bohachevsky1(x, lb=-100, ub=100):
    '''
        2020-3-9
        Bohachevsky 1  function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)+2*math.pow(x[1], 2)-0.3 * \
            math.cos(3*math.pi*x[0])-0.4*math.cos(4*math.pi*x[1])+0.7
    return lb, ub, y


def Bohachevsky2(x, lb=-100, ub=100):
    '''
        2020-3-9
        Bohachevsky 2  function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)+2*math.pow(x[1], 2)-0.3 * \
            math.cos(3*math.pi*x[0])*0.4*math.cos(4*math.pi*x[1])+0.3
    return lb, ub, y


def Bohachevsky3(x, lb=-100, ub=100):
    '''
        2020-3-9
        Bohachevsky 3  function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)+2*math.pow(x[1], 2)-0.3 * \
            math.cos(3*math.pi*x[0]+4*math.pi*x[1])+0.3
    return lb, ub, y


def Brent(x, lb=-100, ub=100):
    '''
        2020-3-9
        Brent function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0]+10, 2)+math.pow(x[1]+10, 2) + \
            math.exp(-math.pow(x[0], 2)-math.pow(x[1], 2))
    return lb, ub, y


def DownhillStep(x, lb=-10, ub=10):
    '''
        2020-7-11
        Downhill Step function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/114-downhill-step-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.floor(10*(10-math.exp(-x[0]**2-3*x[1]**2)))/10-9
    return lb, ub, y


def EggCrate(x, lb=-100, ub=100):
    '''
        2020-3-10
        Egg Crate function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)+math.pow(x[1], 2)+25 * \
            (math.pow(math.sin(x[0]), 2)+math.pow(math.sin(x[1]), 2))
    return lb, ub, y


def Schaffer7(x, lb=-100, ub=100):
    '''
        2020-7-18
        Schaffer's 7 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/101-schaffer-s-function-no-7
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (x[0]**2+x[1]**2)**0.25*(1+50*(x[0]**2+x[1]**2)**0.1)
    return lb, ub, y
