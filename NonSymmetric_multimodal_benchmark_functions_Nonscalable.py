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


def Adjiman(x, lb=-2, ub=2):
    '''
        2020年3月8日
        Adjiman function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
        And:Adjiman, C. S., et al. (1998). "A global optimization method, αBB, for general twice-differentiable constrained NLPs — I. Theoretical advances." Computers & Chemical Engineering 22(9): 1137-1158.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 2.02181+math.cos(x[0])*math.sin(x[1])-x[0]/(math.pow(x[1], 2)+1)
    return lb, ub, y


def Bukin6(x, lb=-100, ub=100):
    '''
        2020-7-11
        Bukin's 6 function
        cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/52-bukin-s-function-no-6
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 100 * \
            math.sqrt(math.fabs(x[1]-0.01*math.pow(x[0], 2))
                      )+0.01*math.fabs(x[0]+10)
    return lb, ub, y


def ChenBird(x, lb=-100, ub=100):
    '''
        2020-3-9
        Chen Bird function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -0.001 / (math.pow(0.001, 2) + math.pow(x[0] - 0.4 * x[1] - 0.1, 2)) - 0.001 / (
            math.pow(0.001, 2) + math.pow(2 * x[0] + x[1] - 1.5, 2))
    y += 2000
    return lb, ub, y


def ChenV(x, lb=-100, ub=100):
    '''
        2020-3-9
        Chen V function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -0.001/(math.pow(0.001, 2) + math.pow(math.pow(x[0], 2) + math.pow(x[1], 2) - 1, 2)) - 0.001 / (math.pow(0.001, 2) + math.pow(
            math.pow(x[0], 2) + math.pow(x[1], 2) - 0.5, 2)) - 0.001/(math.pow(0.001, 2) + math.pow(math.pow(x[0], 2)-math.pow(x[1], 2), 2))
    y += 2000
    return lb, ub, y


def Damavandi(x, lb=-5, ub=5):
    '''
        2020-3-10
        Damavandi Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (1-math.pow(math.fabs(math.sin(math.pi*(x[0]-2))*math.sin(math.pi*(x[1]-2))/(
            math.pow(math.pi, 2)*(x[0]-2)*(x[1]-2))), 5))*(2+math.pow(x[0]-7, 2)+2*math.pow(x[1]-7, 2))
    return lb, ub, y


def Giunta(x, lb=-1, ub=1):
    '''
        2020-3-18
        Giunta function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        for i in range(d):
            y += math.sin(16 / 15 * x[i] - 1) + math.pow(
                math.sin(16 / 15 * x[i] - 1), 2) + 1 / 50 * math.sin(4 * (16 / 15 * x[i] - 1))
    y = y+0.6-0.060447
    return lb, ub, y


def GramacyLee(x, lb=-1.5, ub=1.5):
    '''
        2020-7-12
        Gramacy-Lee's function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/260-gramacy-lee-s-function-no-03
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y1 = math.exp(-(x[0]-1)**2)+math.exp(-0.8*(x[0]+1)
                                             ** 2)-0.05*math.sin(8*(x[0]+0.1))
        y2 = math.exp(-(x[1]-1)**2)+math.exp(-0.8*(x[1]+1)
                                             ** 2)-0.05*math.sin(8*(x[1]+0.8))
    y = 1.040825908416920-y1*y2
    return lb, ub, y


def H1Filter(x, lb=-10, ub=10):
    '''
        2020-7-12
        H1 filter function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/155-h1-filter
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 2-(math.sin((x[0]-x[1]/8)**2)+math.sin((x[1]+x[0]/8)**2)) / \
            (1+math.sqrt((x[0]-36/13*math.pi)**2+(x[1]-28/13*math.pi)**2))
    return lb, ub, y


def Mishra3(x, lb=-10, ub=10):
    '''
        2020-4-7
        Mishra 3 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    if d == 2:
        y = -math.sqrt(
            math.fabs(math.cos(math.sqrt(math.fabs(math.pow(x[0], 2)+math.pow(x[1], 2))))))+0.01*(x[0]+x[1])
    y += 1.17777
    return lb, ub, y


def Mishra4(x, lb=-10, ub=10):
    '''
        2020-4-7
        Mishra 4 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    if d == 2:
        y = math.sqrt(
            math.fabs(math.sin(math.sqrt(math.fabs(math.pow(x[0], 2)+math.pow(x[1], 2))))))+0.01*(x[0]+x[1])
    y += 0.105472
    return lb, ub, y


def Mishra5(x, lb=-10, ub=10):
    '''
        2020-4-7
        Mishra 5 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    if d == 2:
        y = math.pow(math.pow(
            math.sin(math.pow(math.cos(x[0])+math.cos(x[1]), 2)), 2)+math.pow(math.cos(math.pow(math.sin(x[0])+math.sin(x[1]), 2)), 2)+x[0], 2)+0.01*(x[0]+x[1])
    y += 0.11855
    return lb, ub, y


def Mishra6(x, lb=-10, ub=10):
    '''
        2020-7-17
        Mishra's 6 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/151-mishra-s-function-no-6
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        f1 = (math.sin((math.cos(x[0])+math.cos(x[1]))**2))**2
        f2 = (math.cos((math.sin(x[0])+math.sin(x[1]))**2))**2
        f3 = 0.1*((x[0]-1)**2+(x[1]-1)**2)
        y = -math.log((f1-f2+x[0])**2)+f3
    y += 2.29
    return lb, ub, y


def Mineshaft3(x, lb=-2, ub=2):
    '''
        2020-7-17
        Mineshaft 3 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/115-mineshaft-function-no-3
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -5*math.exp(-1000*((x[0]-0.5)**2+(x[1]-0.3)**2)) - \
            7*math.exp(-2000*((x[0]-0.8)**2+(x[1]-1.3)**2))
    y += 7
    return lb, ub, y


def Peaks(x, lb=-4, ub=4):
    '''
        2020-7-17
        Peaks function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/115-mineshaft-function-no-3
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        f1 = 3*(1-x[0])**2*math.exp(-x[0]**2-(x[1]+1)**2)
        f2 = 10*(x[0]/5-x[0]**3-x[1]**5)*math.exp(-x[0]**2-x[1]**2)
        f3 = 1/3*math.exp(-(x[0]+1)**2-x[1]**2)
        y = f1-f2-f3
    y += 6.551133332622496
    return lb, ub, y


def Scahffer3(x, lb=-10, ub=10):
    '''
        2020-5-20
        Scahffer 3 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.49843315+(math.pow(math.sin(math.cos(math.fabs(math.pow(x[0], 2)-math.pow(x[1], 2)))), 2)-0.5)/(
            1+0.001*math.pow(math.pow(x[0], 2)+math.pow(x[1], 2), 2))
    return lb, ub, y


def Scahffer4(x, lb=-10, ub=10):
    '''
        2020-5-20
        Scahffer 4 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.207421+(math.pow(math.cos(math.sin(math.pow(x[0], 2)-math.pow(x[1], 2))), 2)-0.5)/(
            1+0.001*math.pow(math.pow(x[0], 2)+math.pow(x[1], 2), 2))
    return lb, ub, y


def Trefethen(x, lb=-10, ub=10):
    '''
        2020-7-11
        Trefethen function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.exp(math.sin(50*x[0]))+math.sin(60*math.exp(x[1]))+math.sin(70*math.sin(x[0]))+math.sin(
            math.sin(80*x[1]))-math.sin(10*(x[0]+x[1]))+0.25*(math.pow(x[0], 2)+math.pow(x[1], 2))
    y += 3.30686865
    return lb, ub, y


def Ursem1(x, lb=-3, ub=3):
    '''
        2020-7-18
        Ursem 1 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/107-ursem-function-no-1
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -math.sin(2*x[0]-0.5*math.pi)-3*math.cos(x[1])-0.5*x[0]
    y += 4.816814063734823
    return lb, ub, y


def UrsemWaves(x, lb=-1.2, ub=1.2):
    '''
        2020-7-18
        Ursem-Waves function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/132-ursem-wave-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = -(0.3*x[0])**3+(x[1]**2-4.5*x[1]**2)*x[0]*x[1]+4.7 * \
            math.cos(3*x[0]-x[1]**2*(2+x[0]))*math.sin(2.5*math.pi*x[0])
    y += 7.306998731324462
    return lb, ub, y
