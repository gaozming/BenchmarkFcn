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


def Brown(x, lb=-5, ub=5):
    '''
        2020-3-9
        Brown function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += math.pow(math.pow(x[i], 2), math.pow(x[i+1], 2)+1) + \
            math.pow(math.pow(x[i+1], 2), math.pow(x[i], 2)+1)
    return lb, ub, y
