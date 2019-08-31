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


# data
french_frequency_of_letters = {'a': 0.0911, 'à': 0.0, 'c': 0.0334, 'ô': 0.0003, 't': 0.0682, 'é': 0.0359, 's': 0.0997, 'o': 0.0586, 'u': 0.0354, 'p': 0.023, 'e': 0.1095, 'r': 0.0878, 'è': 0.0037, 'i': 0.0932, 'v': 0.0099, 'l': 0.0397, 'n': 0.0741, 'b': 0.0141, 'â': 0.0062, 'm': 0.0244, 'z': 0.011, 'g': 0.0159, 'j': 0.0019, 'd': 0.0238, 'q': 0.005, 'î': 0.0009, 'f': 0.0132, 'x': 0.0025, 'y': 0.0034, 'ê': 0.0007, 'h': 0.0112, 'û': 0.0004, 'ç': 0.0008, 'ï': 0.0003, 'k': 0.0005, 'ë': 0.0, "'": 0.0001, 'w': 0.0002, 'ü': 0.0, 'ú': 0.0, 'ö': 0.0, 'ù': 0.0}

american_english_frequency_of_letters = {'a': 0.0799, 's': 0.1126, 'm': 0.0277, 'd': 0.0349, 'o': 0.0603, 'l': 0.0505, 'w': 0.0093, 'c': 0.039, 'h': 0.0241, 'e': 0.1086, 'n': 0.0701, 'i': 0.0818, 'y': 0.0155, 'r': 0.0704, 'b': 0.0192, 't': 0.0645, 'u': 0.032, 'j': 0.0024, 'g': 0.0278, 'p': 0.0271, 'v': 0.0098, 'x': 0.0026, 'f': 0.013, 'k': 0.0106, 'z': 0.0041, 'q': 0.0019, 'ó': 0.0, 'ü': 0.0, 'á': 0.0, 'ö': 0.0, 'ñ': 0.0, 'é': 0.0002, 'ä': 0.0, 'è': 0.0, 'ç': 0.0, 'ô': 0.0, 'í':
0.0, 'â': 0.0, 'û': 0.0, 'ê': 0.0, 'å': 0.0}

british_english_frequency_of_letters = {'a': 0.0799, 's': 0.1142, 'm': 0.0277, 'd': 0.0348, 'o': 0.0603, 'l': 0.0503, 'w': 0.0093, 'c': 0.039, 'h': 0.0241, 'e': 0.1084, 'n': 0.0701, 'i': 0.0817, 'y': 0.0156, 'r': 0.0704, 'b': 0.0193, 't': 0.0646, 'u': 0.0324, 'j': 0.0024, 'g': 0.0277, 'p': 0.0271, 'v': 0.0097, 'x': 0.0026, 'f': 0.013, 'k': 0.0106, 'z': 0.0026, 'q': 0.0019, 'ó': 0.0, 'ü': 0.0, 'á': 0.0, 'ö': 0.0, 'ñ': 0.0, 'é': 0.0002, 'ä': 0.0, 'è': 0.0, 'ç': 0.0, 'ô': 0.0, 'í': 0.0, 'â': 0.0, 'û': 0.0, 'ê': 0.0, 'å': 0.0}


italian_frequency_of_letters = {'a': 0.1175, 'c': 0.0415, 'h': 0.0059, 'i': 0.1061, 'l': 0.0439, 'e': 0.1119, 'd': 0.0255, 'm': 0.0348, 'o': 0.0824, 'r': 0.086, 'n': 0.0606, 'f': 0.0125, 't': 0.0715, 'g': 0.0221, 's': 0.0693, 'b': 0.0181, 'p': 0.0253, 'z': 0.0125, 'u': 0.0223, 'v': 0.0228, 'y': 0.0, 'q': 0.0017, 'ì': 0.0002, 'ù': 0.0, 'è': 0.0, 'j': 0.0, 'k': 0.0, 'x': 0.0, 'w': 0.0, 'é': 0.0001, 'à': 0.0025, 'ò': 0.0032}

ngerman_frequency_of_letters = {'a': 0.0507, 'b': 0.0236, 'c': 0.0294, 'm': 0.0272, 'l': 0.0409, 's': 0.0748, 'p': 0.0138, 'i': 0.0617, 'd': 0.0296, 'e': 0.1762, 'g': 0.0361, 'x': 0.0008, 'k': 0.0185, 'w': 0.0098, 'n': 0.087, 'o': 0.0219, 'r': 0.0825, 't': 0.0737, 'h': 0.0418, 'u': 0.0359, 'f': 0.0202, 'ä': 0.0078, 'z': 0.0133, 'ö': 0.0027, 'y': 0.0009, 'v': 0.0094, 'j': 0.0008, 'ü': 0.0072, 'ß': 0.0016, 'q': 0.0005, 'é': 0.0, 'â': 0.0, 'ê': 0.0, 'ñ': 0.0, 'à': 0.0}

spanish_frequency_of_letters = {'a': 0.1529, 'r': 0.093, 'ó': 0.0075, 'n': 0.0623, 'i': 0.0761, 'c': 0.0549, 'o': 0.0847, 'b': 0.0185, 'l': 0.0473, 's': 0.0418, 'e': 0.096, 'á': 0.0038, 'í': 0.0061, 'd': 0.0423, 'j': 0.0064, 'g': 0.0172, 't': 0.0536, 'm': 0.031, 'ñ': 0.0027, 'u': 0.0305, 'z': 0.0077, 'q': 0.0037, 'h': 0.0094, 'y': 0.0015, 'v': 0.0101, 'é': 0.0023, 'p': 0.0231, 'f': 0.0109, 'x': 0.0016, 'ú': 0.0007, 'ü': 0.0002, 'k': 0.0001, 'w': 0.0}

def frequencyOfLetters(language):
    frequency_of_letters : dict = {}
    filepath = '/usr/share/dict/' + language
    with open(filepath) as fp:  
        line = fp.readline()

        while line:
            word = (line.strip()).lower()
            for l in word:
                if (l != " " and l != ","  and l != "." and l != "-" and l != "'"):
                    if l in frequency_of_letters:
                        frequency_of_letters[l] = frequency_of_letters[l]  + 1
                    else:
                        frequency_of_letters[l] = 0
            
            line = fp.readline()
    
    # sum
    total_of_letters = 0
    for key in frequency_of_letters:
        total_of_letters = total_of_letters + frequency_of_letters[key]

    # div bay total of letters 
    for key in frequency_of_letters:
        frequency_of_letters[key] = np.around(frequency_of_letters[key] / total_of_letters, 4)

    return frequency_of_letters
            

if __name__ == '__main__':
    languages = ["french", "american-english", "british-english", "italian", "ngerman", "spanish"]

    for l in languages:
        print(frequencyOfLetters(l))