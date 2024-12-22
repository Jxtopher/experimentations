
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: *
# @Date: 2019-06
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
def createRandomGraph(nbVertex = 100, p = 1):
    G = nx.Graph()
       
    # Graphe de 30 sommets
    G.add_nodes_from(range(0, nbVertex))

    # Create link
    for i in range (0, nbVertex):
        for j in range(i + 1, nbVertex):
            if random.uniform(0, 1) < p:
                G.add_edge(i, j)
    return G

def createLineGraph(nbVertex = 100):
    G = nx.Graph()
       
    # Graphe de 30 sommets
    G.add_nodes_from(range(0, nbVertex))

    # Create link
    for i in range (1, nbVertex):
        G.add_edge(i - 1, i)
    return G

def nombreComposanteConnexe(graph):
    l = [-1] * len(graph)
    tabu = []
    explorer = [0]
    color = 1

    while (len(explorer) > 0):
        while(len(explorer) > 0):
            node = explorer.pop()
            neighbors = [n for n in graph.neighbors(node)]
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

def experience(nombreOfVertex, p):
    g = createRandomGraph(nombreOfVertex, p)
    d = degree(g)
    x = np.unique(d)
    
    y = [0] *len(x)
    for i in range(0, len(d)):
        for j in range(0, len(x)):
            if d[i] == x[j]:
                y[j] = y[j] + 1
    return x, y

def statistics(simple, nbVertex):
    mean = [None] * len(simple)
    std = [None] * len(simple)
    confidenceInterval = [None] * len(simple)

    for i in range(0, len(mean)):
        mean[i] = 1 - (np.mean(simple[i]) / nbVertex)
        std[i] = np.std(simple[i]) 

    for i in range(0, len(std)):
        confidenceInterval[i] = 1.96 * (std[i]) / np.sqrt(len(simple[i]))
    
    return mean, confidenceInterval

def degree(graph):
    l = []
    for i in range(0, len(graph)):
        l = l + [len([n for n in graph.neighbors(i)])]
    return l
if __name__ == '__main__':
    nbExperience = 1000
    p = 0.06
    numberOfNodes = 100

    for numberOfNodes in [100, 200, 300, 400, 500]:
        x_brut = []
        y_brut = []
        for i in range(0, nbExperience):
            sub_x_brut, sub_y_brut = experience(numberOfNodes, p)
            x_brut = x_brut + np.ndarray.tolist (sub_x_brut)
            y_brut = y_brut + list(sub_y_brut)
            
        # Agregation
        value_max = max(x_brut)
        value_min = min(x_brut)

        d_mean = {}
        d_brut = {}
        n = [0] * len(x_brut)

        for i in range(0, len(x_brut)):
            if x_brut[i] in d_mean:
                d_mean[x_brut[i]] =   (d_mean[x_brut[i]] * n[x_brut[i]] + y_brut[i]) / ( n[x_brut[i]] + 1)
                n[x_brut[i]] = n[x_brut[i]] + 1
            else:
                d_mean[x_brut[i]] = y_brut[i]
                n[x_brut[i]] = n[x_brut[i]] + 1


            if x_brut[i] in d_brut:
                d_brut[x_brut[i]] = d_brut[x_brut[i]] + [y_brut[i]]
            else:
                d_brut[x_brut[i]] = [y_brut[i]]


        print(d_brut)

        x = []
        y = []
        
        for key in d_mean:
            x = x + [key]
            y = y + [d_mean[key] / numberOfNodes]
        

        e = []
        d_confidenceInterval = {}
        for key in d_brut:
            d_confidenceInterval[key] = 1.96 * (np.std(d_brut[key])) / np.sqrt(len(d_brut[key]))
            e = e + [d_confidenceInterval[key] / numberOfNodes]
        
        label = "#v = "+ str(numberOfNodes) + ", p = " + str(p)

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
    plt.ylabel("Proportion of vertices", fontsize=size)
    plt.xlabel("Number of adjacent vertices", fontsize=size)
    plt.grid(True)
    plt.legend(loc=1, prop={'size':size}, fancybox=False)
    plt.savefig("connected-component.pdf", bbox_inches='tight')
    plt.savefig("connected-component.svg", bbox_inches='tight')

    
