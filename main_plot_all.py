'''
    Coder:
        Greenby
    Begin date:
        2020-3-3
    End date:
        2020-8-26
    Functions:
        1) introduced the other coded py files here
        2) plot the three dimensional profiles
    Notes:
        1) plot and saved
        2) in English
    Cited: This work has been published in a book cited as follows:
        Zheng-Ming GAO, Juan ZHAO. Benchmark functions with Python[M]. Riga, Latvia: Golden Light Academic Publishing, 2020.9: 3-5.
        You can get access via: https://morebooks.shop/store/gb/book/benchmark-functions-with-python/isbn/978-620-2-41254-4
'''

# imports
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import sys
import os
import random
import unimodal_benchmark_functions_scalable
import unimodal_benchmark_functions_Nonscalable
import multimodal_benchmark_functions_scalable
import multimodal_benchmark_functions_Nonscalable
import basins_unimodal_benchmark_functions_scalable
import NonSymmetric_multimodal_benchmark_functions_scalable

# random initialize
random.seed()


def plots():
    # Fun = multimodal_benchmark_functions_scalable.StyblinskiTang
    Fun = NonSymmetric_multimodal_benchmark_functions_scalable.Alpine2
    d = 2
    ub, lb, _ = Fun(np.random.rand(d, 1))
    separator = 500
    x = np.linspace(lb, ub, num=separator)
    y = np.linspace(lb, ub, num=separator)
    z = np.zeros((separator, separator))
    for i in range(separator):
        for j in range(separator):
            _, _, z[i][j] = Fun([x[i], y[j]])
    X, Y = np.meshgrid(x, y)
    best_pos = np.unravel_index(z.argmin(), z.shape)
    print("Best: at Point(%f, %f) and valued: %e" %
          (x[best_pos[0]], y[best_pos[1]], z[best_pos[0]][best_pos[1]]))
    fig = plt.figure()
    axes = fig.gca(projection='3d')
    Z = np.array(z)
    axes.plot_surface(X, Y, Z, cmap=mpl.cm.rainbow)
    axes.contour(X, Y, Z, zdir='z', offset=0)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title(Fun.__name__)
    plt.savefig('./profiles/'+Fun.__name__+'.jpg')
    plt.show()


if __name__ == '__main__':
    plots()
