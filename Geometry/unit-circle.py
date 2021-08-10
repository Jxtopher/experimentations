import pylab
import cmath
import numpy as np
import math


def unit_circle() -> None:
    center = complex(0, 0)

    data_x = []
    data_y = []
    for theta in np.arange(0, 2 * np.pi, 0.01):
        p = center + cmath.exp(complex(math.log10(1), theta))
        data_x.append(p.real)
        data_y.append(p.imag)

    # Plot
    out_file = "unit-circle.svg"
    pylab.figure(figsize=(5, 5))
    pylab.plot(data_x, data_y, label=r"$w = z + e^{ln(1) + \theta  i}$")
    pylab.grid()
    pylab.legend()
    pylab.savefig(out_file)
    pylab.close()


if __name__ == "__main__":
    unit_circle()
