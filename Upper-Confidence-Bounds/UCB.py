#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-05
# @Version: 1
# @Purpose: Sationnary reward solt machine.
#           UCB's implementation
#           see : Auer - 2002 - Finite-time Analysis of the Multiarmed Bandit Problem
#           see : DaCosta et al. - 2008 - Adaptive Operator Selection with Dynamic Multi-Armed Bandits

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

class UCB:
    def __init__(self, nbMachine, C):
        self.mean = [0.0] * nbMachine
        self.nbSelectMachine = [0.0] * nbMachine
        self.nbSelectTotal = 0.0
        self.C = C
        self.estimator = [0.0] * nbMachine
        self.nbMachine = nbMachine

    def update(self, machine, reward):
        self.mean[machine] = (self.mean[machine] * self.nbSelectMachine[machine] + reward) / (self.nbSelectTotal + 1.0)
        self.nbSelectMachine[machine] = self.nbSelectMachine[machine] + 1.0
        self.nbSelectTotal = self.nbSelectTotal + 1.0
    
    def upperConfidenceBand(self):
        for m in range(0, self.nbMachine):
            self.estimator[m] = self.mean[m] + self.C * np.sqrt( 2 * np.log(self.nbSelectTotal) / self.nbSelectMachine[m])
        return  self.estimator
        
    def SelectBestMachine(self):
        return np.argmax(self.estimator)

def experimentation(slotMachine, maxRounds, C):
    parameterSelect = []

    ucb = UCB(len(slotMachine), C)

    i = 0
    while i < maxRounds:

        for m in range(0, len(slotMachine)):
            ucb.update(m, np.random.normal(slotMachine[m][0],slotMachine[m][1]))
        

        ucb.upperConfidenceBand()
        parameterSelect += [ucb.SelectBestMachine()]
        i+=1
    return parameterSelect

if __name__ == '__main__':
    np.random.seed(seed=None)
    slotMachine = [[], []]
    slotMachine[0] = [0, 1] # mean (mu) and standard deviation (sigma)
    slotMachine[1] = [1, 1] # mean (mu) and standard deviation (sigma)


    exp = []
    nbexp = 5000
    maxSteps = 50
    for i in range(0, nbexp):
        exp += [experimentation(slotMachine, maxSteps, 0.2)]

    
    mean = np.mean(exp, axis = 0)
    # https://fr.wikipedia.org/wiki/Intervalle_de_confiance#cite_note-8
    confidenceInterval = 1.96 * (np.std(exp, axis = 0) / np.sqrt(nbexp)) 
    
    x = range(0, maxSteps)
    y = mean
    e = confidenceInterval
    l = r"UCB $C = 0.2$"

    plt.errorbar(x, 
            y,
            e, 
            linestyle=next(linecycler), 
            marker=next(markercycler), 
            label=l, 
            linewidth=1, 
            markersize=2, 
            markeredgewidth=1,
            color=next(colorcycler))
    
    size = 10
    plt.ylabel("Proportion of the best slot machine used", fontsize=size)
    plt.xlabel("Steps", fontsize=size)
    plt.grid(True)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("UCB-twoSlotMachines.pdf", bbox_inches='tight')
    plt.savefig("UCB-twoSlotMachines.svg", bbox_inches='tight')
    