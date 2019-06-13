
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: *
# @License: *
# @Date: *
# @Version: 1
# @Purpose: https://en.wikipedia.org/wiki/Component_(graph_theory)
#           pip install networkx
#

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
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


# nbVertex : number of vertex
# p : probability for create a link
def nombreComposanteConnexe(nbVertex = 100, p = 1):
    #random.seed(246) 
    G = nx.Graph()
       
    # Graphe de 30 sommets
    G.add_nodes_from(range(0, nbVertex))

    # Create link
    for i in range (0, nbVertex):
        for j in range(i + 1, nbVertex):
            if random.uniform(0, 1) < p:
                G.add_edge(i, j)

    l = [-1] * nbVertex
    tabu = []
    explorer = [0]
    color = 1

    while (len(explorer) > 0):
        while(len(explorer) > 0):
            node = explorer.pop()
            neighbors = [n for n in G.neighbors(node)]
            for i in neighbors:
                if not(i in tabu):
                    explorer.append(i)
            tabu.append(node)
            l[node] = color
        try:
            explorer.append(l.index(-1))
            color = color + 1
        except ValueError:
            pass

    return color
    
    # plt.figure(figsize=(15, 15))
    # nx.draw(G, with_labels = True)
    # plt.savefig("graph.pdf", bbox_inches='tight')


def statistics(simple, nbVertex):
    mean = [None] * len(simple)
    std = [None] * len(simple)
    confidenceInterval = [None] * len(simple)

    for i in range(0, len(mean)):
        mean[i] = 1 - (np.mean(simple[i]) / nbVertex)
        std[i] = np.std(simple[i]) / nbVertex

    for i in range(0, len(std)):
        confidenceInterval[i] = 1.96 * (std[i]) / np.sqrt(len(simple[i]))
    
    return mean, confidenceInterval

if __name__ == '__main__':
    nbExperience = 100
    p = [0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
    
    #nbVertex = [10, 100, 200, 300 , 400]
    nbVertex = [100, 200, 300 , 400, 500]

    for v in nbVertex:
        print(v)
        nbComposanteConnexe = []
        for j in range(0, len(p)):
            nbComposanteConnexe.append([])
            for i in range(0, nbExperience):
                nbComposanteConnexe[j] += [nombreComposanteConnexe(v, p[j])]
                #print(nbComposanteConnexe)
            
        y, e = statistics(nbComposanteConnexe, v)
        x = p
        label = "#v = " + str(v)

        plt.errorbar(x, 
                y,
                e,
                linestyle=next(linecycler), 
                marker=next(markercycler), 
                label=label, 
                linewidth=1, 
                markersize=2, 
                markeredgewidth=1,
                color=next(colorcycler))
    
    size = 10
    #plt.xticks(np.arange(0, np.max(maxXlabel), step=3))
    plt.ylabel("Ratio of connected component", fontsize=size)
    plt.xlabel("Probability to link between of two nodes", fontsize=size)
    plt.grid(True)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("connected-component.pdf", bbox_inches='tight')
    plt.savefig("connected-component.svg", bbox_inches='tight')

    