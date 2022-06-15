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


def Bird(x, lb=-2*math.pi, ub=2*math.pi):
    '''
        2020-3-9
        Bartels Conn function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.sin(x[0])*math.exp(math.pow(1-math.cos(x[1]), 2))+math.cos(x[1]) * \
            math.exp(math.pow(1-math.sin(x[0]), 2))+math.pow(x[0]-x[1], 2)
    y += 106.764537
    return lb, ub, y


def Camel(x, lb=-2, ub=2):
    '''
        2020-7-11
        Camel function
        cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/31-camel-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 7.0625+(math.pow(x[0], 4)-4.5*math.pow(x[0],
                                                   2)-2)/math.exp(2*math.pow(x[1], 2))
    return lb, ub, y


def CrossInTray(x, lb=-10, ub=10):
    '''
        2020-7-11
        Cross-In Tray function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/44-cross-in-tray-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -0.0001*(math.fabs(math.exp(math.fabs(100 -
                                                  (math.sqrt(x[0]**2+x[1]**2)/math.pi)))*math.sin(x[0])*math.sin(x[1]))+1)**0.1
    y += 2.062611870822739
    return lb, ub, y


def HolderTable1(x, lb=-10, ub=10):
    '''
        2020-7-10
        Holder table 1 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y += -math.fabs(math.cos(x[0])*math.cos(x[1])) * \
            math.exp(
                math.fabs(1-math.sqrt(math.pow(x[0], 2)+math.pow(x[1], 2))/math.pi))
    y += 26.91899
    return lb, ub, y


def HolderTable2(x, lb=-10, ub=10):
    '''
        2020-7-10
        Holder table 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y += -math.fabs(math.sin(x[0])*math.cos(x[1])) * \
            math.exp(
                math.fabs(1-math.sqrt(math.pow(x[0], 2)+math.pow(x[1], 2))/math.pi))
    y += 19.20283
    return lb, ub, y


def HolderTable3(x, lb=-10, ub=10):
    '''
        2020-7-10
        Holder table 3 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y += -math.pow(math.cos(x[0])*math.cos(x[1]) * math.exp(math.fabs(1 -
                                                                          math.sqrt(math.pow(x[0], 2)+math.pow(x[1], 2))/math.pi)), 2)/30
    y += 24.15441
    return lb, ub, y


def Keane(x, lb=-10, ub=10):
    '''
        2020-4-4
        Keane function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = - (math.pow(math.sin(x[0]-x[1]), 2)*math.pow(math.sin(x[0] +
                                                                  x[1]), 2))/math.sqrt(math.pow(x[0], 2)+math.pow(x[1], 2))
    y += 0.673668
    return lb, ub, y


def ModifiedSchaffer3(x, lb=-100, ub=100):
    '''
        2020-7-17
        Modified Schaffer's No.3 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/99-modified-schaffer-s-function-no-3
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+((math.sin(math.cos(math.fabs(x[0]**2-x[1]**2))))**2-0.5) / \
            (1+0.001*(x[0]**2+x[1]**2))**2
    y -= 0.001566854526004
    return lb, ub, y


def ModifiedSchaffer4(x, lb=-10, ub=10):
    '''
        2020-7-17
        Modified Schaffer's No.4 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/99-modified-schaffer-s-function-no-4
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+((math.cos(math.sin(math.fabs(x[0]**2-x[1]**2))))**2-0.5) / \
            (1+0.001*(x[0]**2+x[1]**2))**2
    y -= 0.292578632035980
    return lb, ub, y


def Parsopoulos(x, lb=-5, ub=5):
    '''
        2020-7-17
        Parsopoulos's function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/252-parsopoulos-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (math.cos(x[0]))**2+(math.sin(x[1]))**2
    return lb, ub, y


def PenHolder(x, lb=-10, ub=10):
    '''
        2020-7-18
        Pen-Holder function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/64-pen-holder-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -math.exp(-1/math.fabs(math.cos(x[0])*math.cos(x[1])*math.exp(
            math.fabs(1-math.sqrt(x[0]**2+x[1]**2)/math.pi))))
    y += 0.9635348327265058
    return lb, ub, y


def Price1OrBeckerLago(x, lb=-10, ub=10):
    '''
        2020-7-17
        Price's 1 function or Becker-Lago's function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/28-becker-lago-s-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (math.fabs(x[0])-5)**2+(math.fabs(x[1])-5)**2
    return lb, ub, y


def TesttubeHolder(x, lb=-10, ub=10):
    '''
        2020-7-10
        Testtube Holder  function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y += -4*(math.sin(x[0])*math.cos(x[1])*math.exp(
            math.fabs(math.cos(math.pow(x[0], 2)+math.pow(x[1], 2))/200)))
    y += 4.019439
    return lb, ub, y
