'''
    Coder:
        Greenby
    Begin date:
        2020-3-6
    End date:
        2020-8-26
    Functions:
        1) Listed the multimodal fixed dimensionality benchmark functions with their names
        2) All of the multimodal fixed dimensionality benchmark functions are symmetric, continuous,  and have no flat-like peaks in their three dimensional profiles
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


def Ackley3(x, lb=-100, ub=100):
    '''
        2020年3月6日
        Ackley 1 Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 195.6316-200*math.exp(-0.02*math.sqrt(math.pow(x[0], 2)+math.pow(
            x[1], 2)))+5*math.exp(math.cos(3*x[0])+math.sin(3*x[1]))
    return lb, ub, y


def Davis(x, lb=-100, ub=100):
    '''
        2020-7-11
        Davis' function
        cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/47-davis-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(math.pow(x[0], 2)+math.pow(x[1], 2), 0.25)*(1+math.pow(
            math.sin(50*math.pow(3*math.pow(x[0], 2)+math.pow(x[1], 2), 0.1)), 2))
    return lb, ub, y


def DropWave(x, lb=-5, ub=5):
    '''
        2020-7-12
        Drop-Wave function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/54-drop-wave-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 1 - \
            (1-math.cos(12*math.sqrt(x[0]**2+x[1]**2))
             )/(0.5*(x[0]**2+x[1]**2)+2)
    return lb, ub, y


def ModifiedSchaffer1(x, lb=-10, ub=10):
    '''
        2020-7-17
        Modified Schaffer's No.1 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/96-modified-schaffer-s-function-no-1
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+((math.sin(x[0]**2+x[1]**2))**2-0.5) / \
            (1+0.001*(x[0]**2+x[1]**2))**2
    return lb, ub, y


def ModifiedSchaffer2(x, lb=-100, ub=100):
    '''
        2020-7-17
        Modified Schaffer's No.2 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/97-modified-schaffer-s-function-no-2
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+((math.sin(x[0]**2-x[1]**2))**2-0.5) / \
            (1+0.001*(x[0]**2+x[1]**2))**2
    return lb, ub, y


def Periodic(x, lb=-10, ub=10):
    '''
        2020-4-7
        Periodic function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.1+math.pow(math.sin(x[0]), 2)+math.pow(math.sin(x[1]), 2) - \
            0.1*math.exp(-math.pow(x[0], 2)-math.pow(x[1], 2))
    return lb, ub, y


def Price2OrPeriodic(x, lb=-100, ub=100):
    '''
        2020-4-8
        Revised at 2020-7-18
        Price 2 or Periodic function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
        And https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/158-price-s-function-no-2
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.1+math.pow(math.sin(x[0]), 2)+math.pow(math.sin(x[1]), 2) - \
            0.1*math.exp(-math.pow(x[0], 2)-math.pow(x[1], 2))
    return lb, ub, y


def Sawtoothxy(x, lb=-100, ub=100):
    '''
        2020-7-18
        Sawtoothxy function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/66-sawtoothxy-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        r = math.sqrt(x[0]**2+x[1]**2)
        t = math.atan2(x[1], x[0])
        gr = (math.sin(4)-math.sin(2*r)/2+math.sin(3*r) /
              3-math.sin(4*r)/4+4)*(r**2/(r+1))
        ht = 1/2*math.cos(2*t-1/2)+math.cos(t)+2
        y = gr*ht
    return lb, ub, y


def Scahffer1(x, lb=-10, ub=10):
    '''
        2020-5-20
        Scahffer 1 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+(math.pow(math.sin(math.pow(math.pow(x[0], 2)+math.pow(x[1], 2), 2)), 2)-0.5)/(
            1+0.001*math.pow(math.pow(x[0], 2)+math.pow(x[1], 2), 2))
    return lb, ub, y


def Scahffer2(x, lb=-10, ub=10):
    '''
        2020-5-20
        Scahffer 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+(math.pow(math.sin(math.pow(math.pow(x[0], 2)-math.pow(x[1], 2), 2)), 2)-0.5)/(
            1+0.001*math.pow(math.pow(x[0], 2)+math.pow(x[1], 2), 2))
    return lb, ub, y


def Schaffer6(x, lb=-10, ub=10):
    '''
        2020-7-18
        Schaffer's 6 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/100-schaffer-s-function-no-6
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.5+(math.pow(math.sin(math.sqrt(x[0]**2+x[1]**2)),
                          2)-0.5)/(1+0.001*(x[0]**2+x[1]**2))**2
    return lb, ub, y


def Tsoulos(x, lb=-1, ub=1):
    '''
        2020-7-18
        Tsoulos' function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/106-tsoulos-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = x[0]**2+x[1]**2-math.cos(18*x[0])-math.cos(18*x[1])
    y += 2
    return lb, ub, y


def Ursem3(x, lb=-2, ub=2):
    '''
        2020-7-18
        Ursem 3 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/107-ursem-function-no-3
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -(3-math.fabs(x[0]))/2*(2-math.fabs(x[1]))/2*math.sin(2.2*math.pi*x[0]+0.5*math.pi)-(
            2-math.fabs(x[0]))/2*(2-math.fabs(x[1]))/2*math.sin(0.5*math.pi*x[1]**2+0.5*math.pi)
    y += 2.5
    return lb, ub, y


def Ursem4(x, lb=-2, ub=2):
    '''
        2020-7-18
        Ursem 4 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/107-ursem-function-no-4
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -3*math.sin(0.5*math.pi*x[0]+0.5*math.pi) * \
            (2-math.sqrt(x[0]**2+x[1]**2))/4
    y += 1.5
    return lb, ub, y


def VenterSobiezcczanskiSobieski(x, lb=-10, ub=10):
    '''
        2020-7-11
        Venter Sobiezcczanski-Sobieski function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)-100*math.pow(math.cos(x[0]), 2)-100*math.cos(math.pow(x[0], 2)/30) + \
            math.pow(x[1], 2)-100*math.pow(math.cos(x[1]), 2) - \
            100*math.cos(math.pow(x[1], 2)/30)
    y += 400
    return lb, ub, y
