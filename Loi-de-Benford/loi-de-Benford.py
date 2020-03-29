#!/usr/bin/python3

from tempfile import NamedTemporaryFile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import urllib.request

from pylab import savefig



def dwfile(url : str, temporary_file : str) -> None:
    urllib.request.urlretrieve(url, temporary_file)

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

def plot(tab : list, title :str) -> None:
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.bar(range(1, 10), tab)
    plt.xticks(range(1, 10))
    plt.xlabel("Pourcentage", size="large")
    plt.ylabel("Premier chiffre des nombres", size="large")
    plt.title(title, size="x-large")
    plt.savefig(title+".svg")

if __name__ == "__main__":
    temporary_file = NamedTemporaryFile().name
    list_of_sequences = [
        ["Triangular numbers", "https://oeis.org/A000217/b000217.txt"],
        ["The nonnegative even numbers", "https://oeis.org/A005843/b005843.txt"],
        ["The prime numbers", "https://oeis.org/A000040/a000040.txt"],
        ["Fibonacci numbers", "https://oeis.org/A000045/b000045.txt"],
        ["Pascal's triangle read by rows", "https://oeis.org/A007318/b007318.txt"],
        ["Powers of 2", "https://oeis.org/A000079/b000079.txt"],
        ["The positive integers"," https://oeis.org/A000027/b000027.txt"]
    ]

    # for i in range(0, len(list_of_sequences)):
    i = 0
    dwfile(list_of_sequences[i][1], temporary_file)
    dataset = loadfile(temporary_file)
    tab = stat(dataset)
    plot(tab, list_of_sequences[i][0])