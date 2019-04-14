#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: *
# @License: *
# @Date: *
# @Version: *
# @Purpose: approximation de pi par la méthode de Monte-Carlo
#           see https://fr.wikipedia.org/wiki/Méthode_de_Monte-Carlo#Détermination_de_la_valeur_de_π
#

import numpy as np



from itertools import cycle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

lines = ["-"]#,"--","-.",":"]
markers = ["o", "v", "^", "^", ">", "1", "2", "3", "4", "8", "s", "p", "*", "h", "H", "+", "<", "D"]
colors = ["black", "blue", "green", "red", "brown", "magenta", "silver", "pink"]
linecycler = cycle(lines)
markercycler = cycle(markers)
colorcycler = cycle(colors)


def approximationPI():
    result_x = []
    result_y = []

    inTheCircle = 0
    outsideTheCircle = 0
    step = 0
    while (step < 5010):

        if (np.sqrt(pow(np.random.uniform(), 2) + pow(np.random.uniform(), 2))  <= 1):
            inTheCircle += 1
        else:
            outsideTheCircle += 1

        x = inTheCircle / float(inTheCircle + outsideTheCircle)
        step +=1
        result_x += [step]
        result_y += [x*4]
    return result_x, result_y

if __name__ == '__main__':
    x, y = approximationPI()

    plt.plot(x,
            [3.141592653589793]*len(x), 
            linestyle=next(linecycler), 
            marker=None, 
            label=ur"π", 
            linewidth=1, 
            markersize=2, 
            markeredgewidth=1,
            color=next(colorcycler))

    plt.plot(x,
            y, 
            linestyle=next(linecycler), 
            marker=None,#next(markercycler), 
            label=ur"Approximation of π", 
            linewidth=1, 
            markersize=2, 
            markeredgewidth=1,
            color=next(colorcycler))



    size = 10
    plt.xticks(np.arange(0, np.max(x), step=500))
    plt.grid(True)
    plt.ylabel("Value", fontsize=size)
    plt.xlabel("Steps", fontsize=size)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("approximation-of-PI.pdf", bbox_inches='tight')
    plt.savefig("approximation-of-PI.svg", bbox_inches='tight')
