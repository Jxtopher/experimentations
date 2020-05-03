#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2020-05
# @Version: 1
# @Purpose: Soit une liste de nombres à inconnue à Aladin. Aladin peut seulement la visiter de manière itérative. Il doit déterminer le plus grand nombre en un nombre de visites minimum.
#           see https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_secr%C3%A9taire
#

from itertools import cycle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
import numpy as np

# Aladin doit deviner le plus grand nombre en un minium d'itérations 
def aladin(number_list: list, exploration_section_size : int):
    my_max = np.amax(number_list[:exploration_section_size])
    for iteration in range(exploration_section_size, len(number_list) - 1):
        if my_max < number_list[iteration]:
            return number_list[iteration], iteration
    return my_max, len(number_list) - 1

# Oracle
def oracle(number_list: list) -> int:
    return np.amax(number_list)

if __name__ == '__main__':
    number_of_experiences = 500#1000
    sample_size = 2#100
    step = 0.1
    x = np.arange(step, 1 + step, step)
    y = []
    confidenceInterval = []

    for value in x:
        exploration_section_size  = int(round(number_of_experiences * value, 0))
        sample_successes : list = []
        for i in range(sample_size):
            number_of_successes = 0
            for i in range(0, number_of_experiences - 1):
                number_list = random.sample(range(0, 10000000), k=number_of_experiences)
                number_find, iterations = aladin(number_list, exploration_section_size)
                if oracle(number_list) == number_find:
                    number_of_successes += 1
            sample_successes +=[number_of_successes / number_of_experiences]
        y += [np.mean(sample_successes)]
        confidenceInterval += [1.96 * (np.std(sample_successes, axis = 0) / np.sqrt(sample_size))]

    print(y)
    print(confidenceInterval)


    lines = ["-"]#,"--","-.",":"]
    markers = ["o", "v", "^", "^", ">", "1", "2", "3", "4", "8", "s", "p", "*", "h", "H", "+", "<", "D"]
    colors = ["black", "blue", "green", "red", "brown", "magenta", "silver", "pink"]
    linecycler = cycle(lines)
    markercycler = cycle(markers)
    colorcycler = cycle(colors)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.margins(0.1)

    plt.errorbar(x, 
            y, 
            confidenceInterval,
            linestyle=next(linecycler), 
            marker=next(markercycler), 
            label="", 
            linewidth=1, 
            markersize=2, 
            markeredgewidth=1,
            color=next(colorcycler))
    
    size = 10
    plt.grid(True, linestyle='--', linewidth=0.1, alpha=0.7)
    plt.ylabel("Success rate", fontsize=size)
    plt.xlabel("Proportion of the exploration section", fontsize=size)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("optimal_stop.pdf", bbox_inches='tight')
    plt.savefig("optimal_stop.svg", bbox_inches='tight')





