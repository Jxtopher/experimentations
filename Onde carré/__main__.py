#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-04
# @Version: 1
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

if __name__ == '__main__':
    value : list = []
    for i in range(1,200):
        value += [i+i+1]
    print(value)
    for i in range(len(value)):
        fig, ax = plt.subplots(figsize=(5, 5))
        x = np.arange(0,10*np.pi,0.1)   # start,stop,step
        y = np.sin(x)
        for j in range(i):
            y += np.sin(value[j] * x) / value[j]
        

        plt.plot(x,
                y, 
                linestyle=next(linecycler), 
                marker=None, 
                label="x", 
                linewidth=1, 
                markersize=2, 
                markeredgewidth=1,
                color="black")

        size = 10
        plt.xlim(-2,32)
        plt.ylim(-1,1)
        plt.grid(True)
        plt.ylabel("y", fontsize=size)
        plt.xlabel("x", fontsize=size)
        plt.savefig("images/square-wave-"+str(i)+".png", dpi=150, bbox_inches='tight')
        plt.close()