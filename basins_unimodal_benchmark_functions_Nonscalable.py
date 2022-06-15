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


def RotatedEllipse1(x, lb=-100, ub=100):
    '''
        2020-4-9
        Revised 2020-7-18
        Rotated Ellipse 1 function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
        And https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/126-rotated-ellipse-function-no-1
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 7*math.pow(x[0], 2)-6*math.sqrt(3)*x[0]*x[1]+13*math.pow(x[1], 2)
    return lb, ub, y


def RotatedEllipse2(x, lb=-100, ub=100):
    '''
        2020-4-9
        Rotated Ellipse 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)-x[0]*x[1]+math.pow(x[1], 2)
    return lb, ub, y
