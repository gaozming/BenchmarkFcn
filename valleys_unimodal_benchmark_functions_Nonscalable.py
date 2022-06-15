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


def DekkerAarts(x, lb=-20, ub=20):
    '''
        2020-7-12
        Dekker-Aarts' function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/53-dekker-aarts-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 10**5*x[0]**2+x[1]**2 - \
            (x[0]**2+x[1]**2)**2+10**(-5)*(x[0]**2+x[1]**2)**4
    y += 24777
    return lb, ub, y


def Matyas(x, lb=-100, ub=100):
    '''
        2020-4-4
        Matyas function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.26*(math.pow(x[0], 2)+math.pow(x[1], 2))-0.48*x[0]*x[1]
    return lb, ub, y


def Rump(x, lb=-100, ub=100):
    '''
        2020-5-20
        Rump function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (333.75-math.pow(x[0], 2))*math.pow(x[1], 6)+math.pow(x[0], 2)*(11*math.pow(
            x[0], 2)*math.pow(x[1], 2)-121*math.pow(x[1], 4)-2)+5.5*math.pow(x[1], 8)+x[0]/(2*x[1])
    return lb, ub, y


def ThreeHumpCamel(x, lb=-100, ub=100):
    '''
        2020-3-9
        Camel function: Three Hump function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 2*math.pow(x[0], 2)-1.05*math.pow(x[0], 4) + \
            math.pow(x[0], 6)/6.0+x[0]*x[1]+math.pow(x[1], 2)
    return lb, ub, y
