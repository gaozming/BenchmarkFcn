'''
    Coder:
        Greenby
    Begin date:
        2020-3-6
    End date:
        2020-8-26
    Functions:
        1) Listed the multimodal  dimensionality benchmark functions with their names
        2) All of the multimodal  dimensionality benchmark functions are symmetric, continuous, scalable and have no flat-like peaks in their three dimensional profiles
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


def Alpine1(x, lb=-10, ub=10):
    '''
        2020-3-8
        Alpine 1 Function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.fabs(x[i]*math.sin(x[i])+0.1*x[i])
    return lb, ub, y


def CosineMixture(x, lb=-1, ub=1):
    '''
        2020-7-18
        Cosine Mixture function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/166-cosine-mixture-function
        Notice that it seems that the global maxima is always equal to n/10. But this is not true, because when n is large the global maxima will drift away from n/10.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    for i in range(d):
        y1 += math.cos(5*math.pi*x[i])
        y2 += x[i]**2
    y = d/10+y2-y1/10
    return lb, ub, y


def Griewank(x, lb=-100, ub=100):
    '''
        2020-3-18
        Griewank function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 1.0
    for i in range(d):
        y1 += math.pow(x[i], 2) / 4000
        y2 *= math.cos(x[i] / math.sqrt(i+1))
    y = y1-y2+1
    return lb, ub, y


def InvertedCosineWave(x, lb=-5, ub=5):
    '''
        2020-7-19
        Inverted Cosine-Wave Function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/178-inverted-cosine-wave-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += -math.exp(-(x[i]**2+x[i+1]**2+0.5*x[i]*x[i+1])/8) * \
            math.cos(4*math.sqrt(x[i]**2+x[i+1]**2+0.5*x[i]*x[i+1]))
    y += d-1
    return lb, ub, y


def Pathological(x, lb=-100, ub=100):
    '''
        2020-4-7
        Pathological function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    for i in range(d - 1):
        y1 = math.pow(
            math.sin(math.sqrt(100 * math.pow(x[i], 2) + math.pow(x[i + 1], 2))), 2) - 0.5
        y2 = 1 + 0.001 * \
            math.pow(math.pow(x[i], 2) - 2 * x[i] *
                     x[i + 1] + math.pow(x[i + 1], 2), 2)
        y += 0.5+y1/y2
    return lb, ub, y


def Rastrigin(x, lb=-500, ub=500):
    '''
        2020-7-18
        Generalized Rastrigin's Function
        Cited from  https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/174-generalized-rastrigin-s-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += x[i]**2-10*math.cos(2*math.pi*x[i])+10
    return lb, ub, y


def Salomon(x, lb=-100, ub=100):
    '''
        2020-5-20
        Salomon function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += math.pow(x[i], 2)
    y = 1-math.cos(2*math.pi*math.sqrt(y))+0.1*math.sqrt(y)
    return lb, ub, y


def SchumerSteiglitz3(x, lb=-100, ub=100):
    '''
        2020-7-19
        Schumer-Steiglitz's Function No.03
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/243-schumer-steiglitz-s-function-no-3
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        a = np.random.uniform(0.1, 1)
        y += a*x[i]**2
    return lb, ub, y


def Shubert6(x, lb=-10, ub=10):
    '''
        2020-5-21
        Shubert 6 function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += 0.5+(math.pow(math.sin(math.sqrt(math.pow(x[i], 2)+math.pow(x[i+1], 2))), 2)-0.5)/math.pow(
            1+0.001*(math.pow(x[i], 2)+math.pow(x[i+1], 2)), 2)
    return lb, ub, y


def StrechedVSineWave(x, lb=-10, ub=10):
    '''
        2020-5-25
        Streched V Sine Wave function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d-1):
        y += math.pow(math.pow(x[i+1], 2)+math.pow(x[i], 2), 0.25)*(math.pow(
            math.sin(50*math.pow(math.pow(x[i+1], 2)+math.pow(x[i], 2), 0.1)), 2)+0.1)
    return lb, ub, y


def StyblinskiTang(x, lb=-5, ub=5):
    '''
        2020-7-10
        Styblinkski-Tang function
        cited from Jamil, M. and X.-S. Yang (2013). "A literature survey of benchmark functions for global optimization problems." Int. Journal of Mathematical Modelling and Numerical Optimisation 4(2): 150-194.
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += 0.5*(math.pow(x[i], 4)-16*math.pow(x[i], 2)+5*x[i])
    y += 78.332
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


def VenterSobiezcczanskiSobieski(x, lb=-10, ub=10):
    '''
        2020-7-18
        Venter and Sobiezcczanski-Sobieski's Function
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/108-venter-and-sobiezcczanski-sobieski-s-function
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        y += x[i]**2-100*(math.cos(x[i]))**2-100*math.cos(x[i]**2/30)
    y += 400
    return lb, ub, y


def XinSheYang3(x, lb=-2*math.pi, ub=2*math.pi):
    '''
        2020-7-19
        Xin-She Yang's Function No.03
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/263-xin-she-yang-s-function-no-03
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    for i in range(d):
        y1 += math.fabs(x[i])
        y2 += math.sin(x[i]**2)
    y = y1*math.exp(-y2)
    return lb, ub, y


def XinSheYang5(x, lb=-10, ub=10):
    '''
        2020-7-19
        Xin-She Yang's Function No.05
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/263-xin-she-yang-s-function-no-05
    '''
    d = len(x)
    y = 0.0
    for i in range(d):
        u = np.random.uniform(0, 1)
        y += u*math.pow(math.fabs(x[i]), i)
    return lb, ub, y


def XinSheYang6(x, lb=-10, ub=10):
    '''
        2020-7-19
        Xin-She Yang's Function No.06
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/263-xin-she-yang-s-function-no-06
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    y3 = 0.0
    for i in range(d):
        y1 += math.pow(math.sin(x[i]), 2)
        y2 += x[i]**2
        y3 += math.pow(math.sin(math.sqrt(math.fabs(x[i]))), 2)
    y = 1+(y1-math.exp(-y2))*math.exp(-y3)
    return lb, ub, y


def XinSheYang8(x, lb=-10, ub=10):
    '''
        2020-7-19
        Xin-She Yang's Function No.08
        Cited from https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/263-xin-she-yang-s-function-no-08
    '''
    d = len(x)
    y = 0.0
    y1 = 0.0
    y2 = 0.0
    for i in range(d):
        u = np.random.uniform(0, 1)
        y1 += u*x[i]**2
        y2 += u*math.pow(math.sin(2*d*math.pi*x[i]), 2)
    y = math.fabs(1-math.exp(-y1))+y2
    return lb, ub, y
