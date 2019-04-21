#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-04
# @Version: 1
# @Purpose: 
#           https://en.wikipedia.org/wiki/Hamming_distance
#           see https://packages.debian.org/jessie/wordlist
#           see /usr/share/dict/
#

import numpy as np
import json
import sys
import collections
from itertools import cycle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json

lines = ["-"]#,"--","-.",":"]
markers = ["o", "v", "^", "^", ">", "1", "2", "3", "4", "8", "s", "p", "*", "h", "H", "+", "<", "D"]
colors = ["black", "blue", "green", "red", "brown", "magenta", "silver", "pink"]
linecycler = cycle(lines)
markercycler = cycle(markers)
colorcycler = cycle(colors)

def distanceHamming(s1, s2):
    #s1 = _s1.decode("utf-8", "strict")
    #s2 = _s2.decode("utf-8", "strict")
    
    distance = 0
    jobs = []
    retInfo = []
    
    if len(s1) == len(s2):
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                distance +=1
        return distance

    elif len(s1) < len(s2):
        distance = [len(s2) - len(s1)] * ((len(s2) - len(s1)) + 1)

        for n in  range(0, len(s2) - len(s1) + 1):
            for i in range(0, len(s1)):
                if s1[i] != s2[i + n]:
                    distance[n] +=1

        return distance[np.argmin(distance)]
    else:
        distance = [len(s1) - len(s2)] * ((len(s1) - len(s2)) + 1)

        for n in  range(0, len(s1) - len(s2) + 1):
            for i in range(0, len(s2)):
                if s2[i] != s1[i + n]:
                    distance[n] +=1

        return distance[np.argmin(distance)]

def loadwordlist(language):
    filepath = '/usr/share/dict/' + language
    #filepath = "C:\\Dev\\dict\\" + language

    word = []

    with open(filepath) as fp:  
        line = fp.readline()
        while line:
            word.append(line.strip())
            line = fp.readline()

    return word

def computeStatistics(language, numLine):    
    languages = ["french", "american-english", "british-english", "italian", "ngerman", "spanish"]
    words = loadwordlist(languages[language])
    #print("[+] Loading word list finish")

    file = open('./'+languages[language]+'/distanceHamming_'+languages[language]+'-'+str(numLine)+'.data',"w") 

    #count = 0
    #dHamming = []
    #for i in range(0, 1):
    i = numLine
    for j in range(i + 1, len(words)):
    #x =[i, j,distanceHamming(words[i], words[j])]
        file.write(str(i) + " " + str(j) + " " + str(distanceHamming(words[i], words[j])) +"\n")
    file.close()

def dataProcessing(language):
    frequancy = dict()

    languages = ["french", "american-english", "british-english", "italian", "ngerman", "spanish"]
    numLine = 2077

    count = 0
    for i in range(0, 139718):
        namefile = languages[language]+'/distanceHamming_'+languages[language]+'-'+str(numLine)+'.data'
        file = open(namefile, "r")
        for x in file:
            count += 1
            if int(x.strip().split(' ')[2]) in frequancy:
                frequancy[int(x.strip().split(' ')[2])] += 1
            else:
                frequancy[int(x.strip().split(' ')[2])] = 1
        file.close()

    x = []
    y = []
    l = languages[language]

    for i in frequancy:
        x += [i]
        y += [frequancy[i] / float(count)]

    return x, y, l

if __name__ == '__main__':
    with open('hamming-distance-french.json', 'w') as outfile:
        json.dump(dataProcessing(1), outfile)

    with open('hamming-distance-american-english.json', 'w') as outfile:
        json.dump(dataProcessing(1), outfile)


    with open('hamming-distance-french.json', 'r') as f:
        datastore = json.load(f)
    
    x1 = datastore[0]
    y1 = datastore[1]
    l1 = datastore[2]
    
    plt.plot(x1, 
            y1, 
            linestyle=next(linecycler), 
            marker=next(markercycler), 
            label=l1, 
            linewidth=1, 
            markersize=2, 
            markeredgewidth=1,
            color=next(colorcycler))

    with open('hamming-distance-american-english.json', 'r') as f:
        datastore = json.load(f)
    
    x2 = datastore[0]
    y2 = datastore[1]
    l2 = datastore[2]
    
    plt.plot(x2, 
            y2, 
            linestyle=next(linecycler), 
            marker=next(markercycler), 
            label=l2, 
            linewidth=1, 
            markersize=2, 
            markeredgewidth=1,
            color=next(colorcycler))
    
    size = 10
    plt.ylabel("Proportion of distance between two words", fontsize=size)
    plt.xlabel("Hamming distance", fontsize=size)
    plt.grid(True)
    plt.legend(loc=4, bbox_to_anchor=(1, 0.2),prop={'size':size}, fancybox=False) #(loc='upper center', ncol=3, fancybox=True)
    plt.savefig("hamming-distance.pdf", bbox_inches='tight')
    plt.savefig("hamming-distance.svg", bbox_inches='tight')