from typing import List
from numpy import array, random, cumsum
from scipy.ndimage.filters import gaussian_filter1d, maximum_filter1d, median_filter, minimum_filter, minimum_filter1d, uniform_filter, gaussian_filter, uniform_filter1d
import pylab


if __name__ == "__main__":
    size_of_dataset = 400
    t = cumsum(random.randint(0, 10, size_of_dataset))
    dataset = cumsum(random.normal(0, 1, size_of_dataset))


    pylab.figure(figsize=(8, 8), dpi=80)
    pylab.scatter(x=t, y=dataset, c="black", s=2, label="dataset")

    pylab.plot(t, uniform_filter1d(dataset, size=20), label="Uniform size=20")
    pylab.plot(t, gaussian_filter1d(dataset, sigma=20), label="Gaussian $\sigma$=20")
    pylab.plot(t, minimum_filter1d(dataset, size=20), label="Minimum size=20")
    pylab.plot(t, maximum_filter1d(dataset, size=20), label="Maximum size=20")
    pylab.plot(t, median_filter(dataset, size=20), label="Median size=20")
    
    pylab.legend(loc='best')
    pylab.xlabel("Time")
    pylab.ylabel("Value")
    pylab.savefig("filter-application.pdf")
    pylab.savefig("filter-application.svg")
    pass
