#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-04
# @Version: 1
# @Purpose: 
#           see https://fr.wikipedia.org/wiki/Probabilités_des_dés
#

import numpy as np
from itertools import cycle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# roll of numDice rolls simpleSize times
def throwDice(numDice, simpleSize):
    if numDice == 0:
        return []
    simple = [np.random.randint(6, size=simpleSize)]
    for i in range(0, numDice-1) :
        simple = simple + [np.random.randint(6, size=simpleSize)]
    return simple

# the statistics computation
def statistics(simple):
    s = np.sum(simple, axis=0)
    unique_elements, counts_elements = np.unique(s, return_counts=True)
    counts_elements_normalize = np.true_divide(counts_elements, np.sum(counts_elements))
    assert((1 - np.sum(counts_elements_normalize)) < 0.1)
    return unique_elements, counts_elements_normalize

#

lines = ["-"]#,"--","-.",":"]
markers = ["o", "v", "^", "^", ">", "1", "2", "3", "4", "8", "s", "p", "*", "h", "H", "+", "<", "D"]
colors = ["black", "blue", "green", "red", "brown", "magenta", "silver", "pink"]
linecycler = cycle(lines)
markercycler = cycle(markers)
colorcycler = cycle(colors)

if __name__ == '__main__':
    maxNumDice = 14
    maxXlabel = 0
    for numDice in range(1, maxNumDice):

        print("#Dice>"+str(numDice))
        #10000000
        r = throwDice(numDice, 10000000)
        x, y = statistics(r)

        maxXlabel = np.max(x)

        label = ur"#d = %s" % (numDice)

        plt.plot(x, 
                y, 
                linestyle=next(linecycler), 
                marker=next(markercycler), 
                label=label, 
                linewidth=1, 
                markersize=2, 
                markeredgewidth=1,
                color=next(colorcycler))
    
    size = 10
    plt.xticks(np.arange(0, np.max(maxXlabel), step=3))
    plt.ylabel("Probability", fontsize=size)
    plt.xlabel("Reward", fontsize=size)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("probabilities-of-the-dice.pdf", bbox_inches='tight')
    plt.savefig("probabilities-of-the-dice.svg", bbox_inches='tight')