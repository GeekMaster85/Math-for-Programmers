from math import exp

from car_data import priuses
from optmize import *

test_data = [
    (-1.0, -2.0137862606487387),
    (-0.9, -1.7730222478628337),
    (-0.8, -1.5510125944820812),
    (-0.7, -1.6071832453434687),
    (-0.6, -0.7530149734137868),
    (-0.5, -1.4185018340443283),
    (-0.4, -0.6055579756271128),
    (-0.3, -1.0067254915961406),
    (-0.2, -0.4382360549665138),
    (-0.1, -0.17621952751051906),
    (0.0, -0.12218090884626329),
    (0.1, 0.07428573423209717),
    (0.2, 0.4268795998864943),
    (0.3, 0.7254661223608084),
    (0.4, 0.04798697977420063),
    (0.5, 1.1578103735448106),
    (0.6, 1.5684111061340824),
    (0.7, 1.157745051031345),
    (0.8, 2.1744401978240675),
    (0.9, 1.6380001974121732),
    (1.0, 2.538951262545233)
]


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    plt.show()


def sum_error(f, data):
    errors = [abs(f(x) - y) for (x, y) in data]
    return sum(errors)


def sum_squared_error(f, data):
    squared_errors = [(f(x) - y) ** 2 for (x, y) in data]
    return sum(squared_errors)


def f(x):
    return 2 * x


def g(x):
    return 1 - x


# plt.scatter([t[0] for t in test_data], [t[1] for t in test_data])
# plot_function(lambda x: 2 * x, -1 ,1, c='k')
prius_mileage_price = [(p.mileage, p.price) for p in priuses]


def p1(x):
    return 25000 - 0.2 * x


def p2(x):
    return 25000 - 0.1 * x


def p3(x):
    return 22500 - 0.1 * x


def test_data_coefficient_cost(a):
    def f(x):
        return a * x

    return sum_squared_error(f, test_data)


def coefficient_cost(a, b):
    def p(x):
        return a * x + b

    return sum_squared_error(p, prius_mileage_price)


def scaled_cost_function(c, d):
    return coefficient_cost(0.5 * c, 50000 * d) / 1e13


def exp_coefficient_cost(q, r):
    def f(x):
        return q * exp(r * x)

    return sum_squared_error(f, prius_mileage_price)


# print(sum_squared_error(p1, prius_mileage_price))
def scaled_exp_coefficient_cost(s, t):
    return exp_coefficient_cost(30000 * s, 1e-4 * t) / 1e11


# c, d = gradient_descent(scaled_cost_function, 0, 0)
s, t = gradient_descent(scaled_exp_coefficient_cost, 0, 0)
print(s, t)
