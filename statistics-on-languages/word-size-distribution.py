#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-04
# @Version: 1
# @Purpose: 
#           see https://packages.debian.org/jessie/wordlist
#           see /usr/share/dict/
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


def wordSizeDistribution(language):
    lenght = []
    filepath = '/usr/share/dict/' + language
    with open(filepath) as fp:  
        line = fp.readline()
        while line:
            lenght.append(len(line.strip()))
            line = fp.readline()

    x = range(1, lenght[np.argmax(lenght)] + 1)
    y = [0] * (lenght[np.argmax(lenght)])
    for i in lenght:
        y[i - 1] += 1

    # Normalisation
    s = np.sum(y)
    for i in range(0, len(y)):
        y[i] = y[i] / float(s)

    label = language
    return x, y, label

if __name__ == '__main__':
    languages = ["french", "american-english", "british-english", "italian", "ngerman", "spanish"]

    for l in languages:
        x, y, l = wordSizeDistribution(l)

        plt.plot(x, 
                y, 
                linestyle=next(linecycler), 
                marker=next(markercycler), 
                label=l, 
                linewidth=1, 
                markersize=2, 
                markeredgewidth=1,
                color=next(colorcycler))
    
    size = 10
    plt.ylabel("Proportion of words", fontsize=size)
    plt.xlabel("Word size", fontsize=size)
    plt.grid(True)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("word-size-distribution.pdf", bbox_inches='tight')
    plt.savefig("word-size-distribution.svg", bbox_inches='tight')