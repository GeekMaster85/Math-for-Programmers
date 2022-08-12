import numpy as np
import matplotlib.pyplot as plt
from math import sin


def plot(fs, xmin, xmax):
    xs = np.linspace(xmin, xmax, 100)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    for f in fs:
        ys = [f(x) for x in xs]
        plt.plot(xs, ys)
    plt.show()


def f(x):
    return 0.5 * x + 3


def g(x):
    return sin(x)

def add_functions(f, g):
    def new(x):
        return f(x) + g(x)
    return new
if __name__ == '__main__':
    plot([f, g, add_functions(f, g)], -10, 10)
