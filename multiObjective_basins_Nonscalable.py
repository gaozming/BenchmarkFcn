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


def Kearfott(x, lb=-100, ub=100):
    '''
        2020-7-13
        Kearfott's function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/59-kearfott-s-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (x[0]**2+x[1]**2-2)**2+(x[0]**2-x[1]**2-1)**2
    return lb, ub, y


def Mishra10bOrSeqP2(x, lb=-10, ub=10):
    '''
        2020-7-13
        Mishra's Function No.10b (or SeqP Function No.02)
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/153-mishra-s-function-no-10b-or-seqp-function-no-2
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.fabs(x[0]+x[1]-x[0]*x[1])
    return lb, ub, y


def Mishra10aOrSeqP1(x, lb=-10, ub=10):
    '''
        2020-7-15
        Mishra's Function No.10a (or SeqP Function No.01)
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/152-mishra-s-function-no-10a-or-seqp-function-no-1
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (x[0]+x[1]-x[0]*x[1])**2
    return lb, ub, y


def Price3OrModifiedRosenbrockOrPriceRosenbrock(x, lb=-10, ub=10):
    '''
        2020-7-18
        Price's Function No.03 (Modified Rosenbrock's or Price-Rosenbrock's Function)
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/160-price-s-function-no-3-modified-rosenbrock-s-or-price-rosenbrock-s-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 100*(x[1]-x[0]**2)**2+(6.4*(x[1]-0.5)**2-x[0]-0.6)**2
    return lb, ub, y


def Price4(x, lb=-100, ub=100):
    '''
        2020-7-18
        Price's Function No.04
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/159-price-s-function-no-4
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (2*x[0]**3*x[1]-x[1]**3)**2+(6*x[0]-x[1]**2+x[1])**2
    return lb, ub, y
