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


def Branin_RCOS1(x, lb=-15, ub=15):
    '''
        2020-7-11
        Branin RCOS 1 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/13-branin-s-rcos-function-no-1
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[1]-5.1*math.pow(x[0], 2)/4/math.pow(math.pi, 2) +
                     5*x[0]/math.pi-6, 2)+10*(1-0.125/math.pi)*math.cos(x[0])+10
    y -= 0.39788735772973816
    return lb, ub, y


def SixHumpCamel(x, lb=-100, ub=100):
    '''
        2020-3-9
        Camel function: Six Hump function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (4-2.1*math.pow(x[0], 2)+math.pow(x[0], 4)/3.0)*math.pow(x[0],
                                                                     2)+x[0]*x[1]+(4*math.pow(x[1], 2)-4)*math.pow(x[1], 2)
    y += 1.0316
    return lb, ub, y


def Treccani(x, lb=-5, ub=5):
    '''
        2020-7-18
        Treccani's function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/70-treccani-s-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = x[0]**4+4*x[0]**3+4*x[0]**2+x[1]**2
    return lb, ub, y


def Trecannis(x, lb=-3, ub=3):
    '''
        2020-7-11
        Trecanni function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 4)-4*math.pow(x[0], 3)+4*x[0]+math.pow(x[1], 2)
    return lb, ub, y


def WayburnSeader1(x, lb=-100, ub=100):
    '''
        2020-7-18
        Wayburn-Seader's Function No.01
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/277-wayburn-seader-s-function-no-01
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (x[0]**6+x[1]**4-17)**2+(2*x[0]+x[1]-4)**2
    return lb, ub, y
