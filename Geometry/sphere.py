from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import quaternion
import math

# # Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, "gray")


def sphere() -> None:
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    xdata = []
    ydata = []
    zdata = []
    for i in np.arange(0, 2 * np.pi, 0.2):
        for j in np.arange(0, 2 * np.pi, 0.2):
            for k in np.arange(0, 2 * np.pi, 0.2):
                x = math.sin(j) * math.cos(i)
                y = math.sin(j) * math.sin(i)
                z = math.cos(j)
                xdata.append(x)
                ydata.append(y)
                zdata.append(z)

    ax.scatter3D(xdata, ydata, zdata, s=1)  # , c=zdata

    plt.savefig("sphere.svg")


if __name__ == "__main__":
    sphere()
