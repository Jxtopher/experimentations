#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-05
# @Version: 1
# @Purpose: Sationnary reward solt machine.
#           Q-learning was introduced by Watkins in 1989 
#           see page 97 : Watkins - 1989 - Learning from Delayed Reward
#           see : https://en.wikipedia.org/wiki/Q-learning
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

class Qlearning:
    def __init__(self, nbMachine, alpha):
            self.alpha = alpha
            self.Q = [0.0] * nbMachine
    
    def update(self, machine, reward):
        self.Q[machine] = (1 - self.alpha) * self.Q[machine] + self.alpha * reward

    def SelectBestMachine(self):
        return np.argmax(self.Q)

def experimentation(slotMachine, maxRounds, alpha):
    parameterSelect = []

    qlearning = Qlearning(len(slotMachine), alpha)

    i = 0
    while i < maxRounds:

        for m in range(0, len(slotMachine)):
            qlearning.update(m, np.random.normal(slotMachine[m][0],slotMachine[m][1]))
        

        parameterSelect += [qlearning.SelectBestMachine()]
        i+=1
    return parameterSelect

if __name__ == '__main__':
    np.random.seed(seed=None)
    slotMachine = [[], []]
    slotMachine[0] = [0, 1] # mean (mu) and standard deviation (sigma)
    slotMachine[1] = [1, 1] # mean (mu) and standard deviation (sigma)


    for alpha in [0.1, 0.2, 0.5, 0.9, 1]:
        exp = []
        nbexp = 5000
        maxSteps = 50
        #alpha = 0.2
        for i in range(0, nbexp):
            exp += [experimentation(slotMachine, maxSteps, alpha)]

        
        mean = np.mean(exp, axis = 0)
        # https://fr.wikipedia.org/wiki/Intervalle_de_confiance#cite_note-8
        confidenceInterval = 1.96 * (np.std(exp, axis = 0) / np.sqrt(nbexp)) 
        
        x = range(0, maxSteps)
        y = mean
        e = confidenceInterval
        l = r"Q-learning $\alpha = "+str(alpha)+"$"

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
    plt.savefig("qlearning-twoSlotMachines.pdf", bbox_inches='tight')
    plt.savefig("qlearning-twoSlotMachines.svg", bbox_inches='tight')