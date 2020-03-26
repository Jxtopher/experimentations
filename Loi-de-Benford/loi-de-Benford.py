#!/usr/bin/python3

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from pylab import savefig

# The prime numbers :https://oeis.org/A000040/a000040.txt
# Fibonacci numbers : https://oeis.org/A000045/b000045.txt
# Pascal's triangle read by rows :https://oeis.org/A007318/b007318.txt
# Powers of 2 : https://oeis.org/A000079/b000079.txt

def loadfile(pathfile : str) -> pd.DataFrame  :
    dataset = pd.read_csv(pathfile, sep=" ", names=["num","value"])
    # print(dataset)
    return dataset

def stat(dataset : pd.DataFrame) -> list:
    tab : list = [0,1,2,3,4,5,6,7,8]
    for index, row in dataset.iterrows():
        # for i in str(row["value"]):
        tab[int(str(row["value"])[0])-1] = tab[int(str(row["value"])[0])-1] + 1

    sum = np.sum(tab)
    return (tab /sum)*100

def plot(tab : list, title :str):
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.bar(range(1, 10), tab)
    plt.xticks(range(1, 10))
    plt.xlabel("Pourcentage")
    plt.ylabel("Premier chiffre des nombres")
    plt.title(title)
    plt.savefig(title+".svg")

if __name__ == "__main__":
    dataset = loadfile("a000040.txt")
    tab = stat(dataset)
    plot(tab, "The prime numbers")

    dataset = loadfile("b000045.txt")
    tab = stat(dataset)
    plot(tab, "Fibonacci numbers")

    dataset = loadfile("b007318.txt")
    tab = stat(dataset)
    plot(tab, "Pascal's triangle read by rows")

    dataset = loadfile("b000079.txt")
    tab = stat(dataset)
    plot(tab, "Powers of 2")

    