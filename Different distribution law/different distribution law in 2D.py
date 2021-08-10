#!/usr/bin/env python
# -*- coding=utf-8 -*-

#
# @Author: Jxtopher
# @License: CC-BY-NC-SA
# @Date: 2019-05
# @Version: 1
# @Purpose: *

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def sub_plot(ax, data):

    x = np.linspace(data[0][np.argmin(data[0])], data[0][np.argmax(data[0])], 100)
    ax.plot(x, x * 0, color="red", zorder=1, linewidth=0.3)
    y = np.linspace(data[1][np.argmin(data[1])], data[1][np.argmax(data[1])], 100)
    ax.plot(y * 0, y, color="red", zorder=2, linewidth=0.3)
    ax.scatter(
        data[0],
        data[1],
        marker="o",
        s=2,
        c="black",
        alpha=0.8,
        edgecolors="none",
        zorder=3,
    )

    size = 5
    # plt.xticks(np.arange(0, np.max(maxXlabel), step=3))
    ax.tick_params(labelsize=size)
    ax.set_ylabel("y", fontsize=size)
    ax.set_xlabel("x", fontsize=size)
    ax.set_title(data[2], fontsize=size)


def data(chose):
    if chose == 0:
        x = np.random.rand(1000)
        y = np.random.rand(1000)
        label = "Uniform law"
    elif chose == 1:
        x = np.random.normal(1, 1, size=1000)
        y = np.random.normal(1, 1, size=1000)
        label = r"$\mathcal{N}(0, 1)$"
    elif chose == 2:
        x = np.random.beta(2, 5, size=1000)
        y = np.random.beta(2, 5, size=1000)
        label = r"$Beta(\alpha=2, \beta=5)$"
    elif chose == 3:
        x = np.random.exponential(size=1000)
        y = np.random.exponential(size=1000)
        label = "Exponential distribution"
    elif chose == 4:
        x = np.random.laplace(size=1000)
        y = np.random.laplace(size=1000)
        label = "Laplace distribution"
    elif chose == 5:
        x = np.random.logistic(size=1000)
        y = np.random.logistic(size=1000)
        label = "Logistic distribution"
    elif chose == 6:
        x = np.random.gamma(2, 2, size=1000)
        y = np.random.gamma(2, 2, size=1000)
        label = "Gamma distribution shape = 2, scale = 2"
    elif chose == 7:
        x = np.random.poisson(5, size=1000)
        y = np.random.poisson(5, size=1000)
        label = r"Poisson distribution $\lambda=5$"
    elif chose == 8:
        x = np.random.pareto(3, size=1000)
        y = np.random.pareto(3, size=1000)
        label = r"Pareto distribution $a=3$"
    else:
        x = []
        y = []
        label = ""
    return x, y, label


if __name__ == "__main__":
    np.random.seed(seed=None)

    fig, axs = plt.subplots(figsize=(5, 5), nrows=3, ncols=3, constrained_layout=True)

    i = 0
    for ax in axs.flatten():
        sub_plot(ax, data(i))
        i += 1

    plt.savefig("different-distribution-law-in-2D.pdf", bbox_inches="tight")
    plt.savefig("different-distribution-law-in-2D.svg", bbox_inches="tight")
