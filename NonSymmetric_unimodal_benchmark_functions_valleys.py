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


def BiggsExp2(x, lb=-0, ub=10):
    '''
        2020-3-10
        Exp 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        try:
            for i in range(10):
                y += (math.exp(-i*x[0]/10) - /
                      5*math.exp(-i * x[1]/10)-math.exp(-i/10) + /
                      5*math.exp(-i))**2
        except OverflowError:
            y = np.inf
    return lb, ub, y


def Booth(x, lb=-100, ub=100):
    '''
        2020-3-9
        Booth  function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0]+2*x[1]-7, 2)+math.pow(2*x[0]+x[1]-5, 2)
    return lb, ub, y


def Branin_RCOS2(x, lb=-100, ub=100):
    '''
        2020-3-9
        Branin RCOS 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[1]-5.1*math.pow(x[0], 2)/(4*math.pow(math.pi, 2))+5*x[0]/math.pi-6, 2)+10*(
            1-1/(math.pi*8))*math.cos(x[0])*math.cos(x[1])*math.log(math.pow(x[0], 2)+math.pow(x[1], 2)+1)+10
    y -= 5.559037
    return lb, ub, y


def Bukin4(x, lb=-100, ub=100):
    '''
        2020-7-11
        Bukin's 4 function
        cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/51-bukin-s-function-no-4
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 100*math.pow(x[1], 2)+0.01*math.fabs(x[0]+10)
    return lb, ub, y


def Chichinadze(x, lb=-100, ub=100):
    '''
        2020-3-9
        Chichinadze function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0], 2)-12*x[0]+11+10*math.cos(math.pi*x[0]/2)+8*math.sin(
            5*math.pi*x[0]/2)-math.pow(1/5, 0.5)*math.exp(-0.5*math.pow(x[1]-0.5, 2))
    y += 43.3159
    return lb, ub, y


def Complex(x, lb=-10, ub=10):
    '''
        2020-7-11
        Complex function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/43-complex-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = (x[0]**3-3*x[0]*x[1]**2-1)**2+(3*x[1]*x[0]**2-x[1]**3)**2
    return lb, ub, y


def Cube(x, lb=-100, ub=100):
    '''
        2020-3-10
        Cube Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y += 100*math.pow(x[1]-math.pow(x[0], 3), 2)+math.pow(1-x[0], 2)
    return lb, ub, y


def DixonAndPrice(x, lb=-100, ub=100):
    '''
        2020-3-9
        Dixon & Price Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        if i == 0:
            y += math.pow(x[0] - 1, 2)
        else:
            y += (i+1)*math.pow(2*math.pow(x[i], 2)-x[i-1], 2)
    return lb, ub, y


def ElAttarVidyasagarDutta(x, lb=-100, ub=100):
    '''
        2020-3-10
        El-Attar-Vidyasagar-Dutta function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(math.pow(x[0], 2)-x[1]-10, 2)+math.pow(x[0]+math.pow(x[1], 2) -
                                                            7, 2)+math.pow(math.pow(x[0], 2)+math.pow(x[1], 3)-1, 2)
    y -= 0.470427
    return lb, ub, y


def F26(x, lb=-100, ub=100):
    '''
        2020-7-12
        Engvall's function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/253-f26-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.25*x[0]**4-0.5*x[0]**2+0.1*x[0]+0.5*x[1]**2
    return lb, ub, y


def FreudensteinRoth(x, lb=-10, ub=10):
    '''
        2020-3-10
        Freudenstein Roth function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(x[0]-13+((5-x[1])*x[1]-2)*x[1], 2) + \
            math.pow(x[0]-29+((x[1]+1)*x[1]-14)*x[1], 2)
    return lb, ub, y


def GeneralizedDixonPriceRosenbrock(x, lb=-100, ub=100):
    '''
        2020-7-18
        Generalized Dixon-Price-rosenbrock's function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/237-generalized-dixon-price-rosenbrock-s-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += 100*(x[i+1]-x[i]**2)**8+(x[i]-1)**8
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


def Himmelblau(x, lb=-100, ub=100):
    '''
        2020-3-18
        Himmelblau function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.pow(math.pow(x[0], 2)+x[1]-11, 2) + \
            math.pow(x[0]+math.pow(x[1], 2)-7, 2)
    return lb, ub, y


def Leon(x, lb=-100, ub=100):
    '''
        2020-4-4
        Leon function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 100*math.pow(x[1]-math.pow(x[0], 2), 2)+math.pow(1-x[0], 2)
    return lb, ub, y


def McCormick(x, lb=-10, ub=10):
    '''
        2020-4-4
        McCormick function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = math.sin(x[0] + x[1]) + math.pow(x[0] - x[1], 2) - \
            3.0 / 2 * x[0] + 5.0 / 2 * x[1] + 1
    y += 11
    return lb, ub, y


def Mishra1(x, lb=-1, ub=1):
    '''
        2020-4-4
        Mishra 1 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    try:
        for i in range(d-1):
            y1 += x[i]
        y = math.pow(1+d-y1, d-y1)-2
    except:
        y = np.inf
    return lb, ub, y


def Mishra2(x, lb=-1, ub=1):
    '''
        2020-4-4
        Mishra 2 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    for i in range(d-1):
        y1 += 0.5*(x[i]+x[i+1])
    y = math.pow(1+d-y1, d-y1)-2
    return lb, ub, y


def Rosenbrock(x, lb=-100, ub=100):
    '''
        2020-4-9
        Rosenbrock function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += 100*math.pow(x[i+1]-math.pow(x[i], 2), 2)+math.pow(x[i]-1, 2)
    return lb, ub, y


def RosenbrockModified(x, lb=-100, ub=100):
    '''
        2020-4-9
        Rosenbrock Modified function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 74+100*math.pow(x[1]-math.pow(x[0], 2), 2)+math.pow(1-x[0], 2) - \
            400*math.exp(-10*(math.pow(x[0]+1, 2)+math.pow(x[1]+1, 2)))
    return lb, ub, y


def S3(x, lb=-10, ub=10):
    '''
        2020-7-18
        S3 function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/118-s3-function
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 2.0+(x[1]-0.7)**2-math.atan(x[0])
    y -= 0.528872325696265
    return lb, ub, y


def ZirilliorAluffiPentini(x, lb=-10, ub=10):
    '''
        2020-7-11
        Zirilli or Aluffi-Pentini's function
        Cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    if d == 2:
        y = 0.25*math.pow(x[0], 4)-0.5*math.pow(x[0], 2) + \
            0.1*x[0]+0.5*math.pow(x[1], 2)
    y += 0.3523
    return lb, ub, y
