from math import e, pi, sin

import matplotlib.pyplot as plt
import numpy as np


def plot_function(f, xmin, xmax, color=None):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], c=color)
    plt.show()
plot_function(lambda x: e * sin(x), -pi, pi)
plot_function(lambda y: e ** y / 2, -3, 3)
