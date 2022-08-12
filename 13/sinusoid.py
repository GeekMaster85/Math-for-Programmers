from math import *
import matplotlib.pyplot as plt
import numpy as np
import pygame.sndarray


def make_sinusoid(freq, amp):
    def f(t):
        return amp * sin(2 * pi * freq * t)

    return f


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    plt.show()


def plot_sequence(points, max=100, line=False, **kwargs):
    if line:
        plt.plot(range(max), points[0:max], **kwargs)
    else:
        plt.scatter(range(max), points[0:max], **kwargs)
    plt.show()


def sample(f, start, end, count):
    mapf = np.vectorize(f)
    ts = np.arange(start, end, (end - start) / count)
    values = mapf(ts)
    return values.astype(np.int16)


def const(n):
    return 1 / sqrt(2)


def square(t):
    return 1 if (t % 1) < 0.5 else -1


def sawtooth(t):
    return t % 1


def fourier_series(a0, a, b):
    def res(t):
        cos_terms = [an * cos(2 * pi * (n + 1) * t)
                     for (n, an) in enumerate(a)]
        sin_terms = [bn * sin(2 * pi * (n + 1) * t)
                     for (n, bn) in enumerate(b)]
        return a0 * const(t) + sum(cos_terms) + sum(sin_terms)

    return res


def inner_product(f, g, n=1000):
    dt = 1 / n
    return 2 * sum([f(t) * g(t) * dt for t in np.arange(0, 1, dt)])


def s(n):  # <1>
    def f(t):
        return sin(2 * pi * n * t)

    return f


def c(n):  # <2>
    def f(t):
        return cos(2 * pi * n * t)

    return f


def fourier_coef(f, N):
    a0 = inner_product(f, const)
    an = [inner_product(f, c(n)) for n in range(1, N + 1)]
    bn = [inner_product(f, s(n)) for n in range(1, N + 1)]
    return a0, an, bn


if __name__ == '__main__':
    approx = fourier_series(*fourier_coef(sawtooth, 10))
    plot_function(sawtooth, 0, 5)
    plot_function(approx, 0, 5)
