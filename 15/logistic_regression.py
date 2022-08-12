from math import exp, log

import matplotlib.pyplot as plt
import numpy as np
from gradient_descent import *
from car_data import *


def bmw_finder(mileage, price):
    if price > 17500:
        return 1
    else:
        return 0


all_car_data = []
for bmw in bmws:
    all_car_data.append((bmw.mileage, bmw.price, 1))
for prius in priuses:
    all_car_data.append((prius.mileage, prius.price, 0))


def plot_data(ds):
    plt.scatter([d[0] for d in ds if d[2] == 0], [d[1] for d in ds if d[2] == 0], c='C1')
    plt.scatter([d[0] for d in ds if d[2] == 1], [d[1] for d in ds if d[2] == 1], c='C0', marker='x')
    plt.ylabel("Price ($)", fontsize=16)
    plt.xlabel("Odometer (mi)", fontsize=16)


def test_classifier(classifier, data, verbose=False):
    true_positives = 0  # 2
    true_negatives = 0
    false_positives = 0
    false_negatives = 0
    for mileage, price, is_bmw in data:
        pred = classifier(mileage, price)
        if pred and is_bmw:
            true_positives += 1
        elif pred:
            false_positives += 1
        elif is_bmw:
            false_negatives += 1
        else:
            true_negatives += 1
    if verbose:
        print('true_positives %f' % true_positives)
        print("true negatives %f" % true_negatives)
        print("false positives %f" % false_positives)
        print("false negatives %f" % false_negatives)
    total = true_positives + true_negatives
    return total / len(data)


def partial_derivative(f, i, v, **kwargs):
    def cross_section(x):
        arg = [(vj if j != i else x) for j, vj in enumerate(v)]
        return f(*arg)

    return approx_derivative(cross_section, v[i], **kwargs)


def approx_gradient(f, v):
    return [partial_derivative(f, i, v) for i in range(len(v))]


def gradient_descent(f, vstart, tolerance=1e-6, max_steps=1000):
    v = vstart
    grad = approx_gradient(f, v)
    steps = 0
    while length(grad) > tolerance and steps < max_steps:
        v = [(vi - 0.01 * dvi) for vi, dvi in zip(v, grad)]
        grad = approx_gradient(f, v)
        steps += 1
    return v


def sum_squares(*v):
    return sum([(x - 1) ** 2 for x in v])


v = [2, 2, 2, 2, 2]
print(gradient_descent(sum_squares, v))


def decision_boundary_classify(mileage, price):
    if price > 21000 - 0.07 * mileage:
        return 1
    else:
        return 0


# print(test_classifier(decision_boundary_classify, all_car_data, True))


# plot_data(all_car_data)
def constant_price_classifier(cutoff_price):
    def c(x, p):
        if p > cutoff_price:
            return 1
        else:
            return 0

    return c


def cutoff_accuracy(cutoff_price):
    c = constant_price_classifier(cutoff_price)
    return test_classifier(c, all_car_data)


# all_prices = [price for (mileage, price, is_bmw) in all_car_data]
# m = max(all_prices, key=cutoff_accuracy)
# print(test_classifier(constant_price_classifier(m), all_car_data, verbose=True))

def make_scale(data):
    min_val = min(data)
    max_val = max(data)

    def scale(x):
        return (x - min_val) / (max_val - min_val)

    def unscale(y):
        return y * (max_val - min_val) + min_val

    return scale, unscale


price_scale, price_unscale = make_scale([x[1] for x in all_car_data])
mileage_scale, mileage_unscale = make_scale([x[0] for x in all_car_data])
scaled_car_data = [(mileage_scale(mileage), price_scale(price), is_bmw)
                   for mileage, price, is_bmw in all_car_data]


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    plt.show()


# plot_data(scaled_car_data)
# plot_function(lambda x: 0.56 - 0.35 * x, 0, 1, c='k')
# plt.show()
def linear_classifier(mileage, price):
    if price > 0.56 - 0.35 * mileage:
        return 1
    else:
        return 0


# print(test_classifier(linear_classifier, scaled_car_data, verbose=True))


def sigmoid(x):
    return 1 / (1 + exp(-x))


def h(x):
    return sigmoid(3 - x)


# plot_function(h, -5, 11)
def make_logistic(a, b, c):
    def l(x, p):
        return sigmoid(a * x + b * p - c)

    return l


def simple_logistic_cost(a, b, c):
    l = make_logistic(a, b, c)
    errors = [abs(is_bmw - l(x, p)) for x, p, is_bmw in scaled_car_data]
    return sum(errors)




def point_cost(l, x, p, is_bmw):
    wrong = 1 - is_bmw
    return -log(abs(wrong - l(x, p)))


def logistic_cost(a, b, c):
    l = make_logistic(a, b, c)
    errors = [point_cost(l, x, p, is_bmw) for x, p, is_bmw in scaled_car_data]
    return sum(errors)


def plot_line(a, b, c, **kwargs):
    if 'c' not in kwargs:
        kwargs['c'] = 'k'
    if b == 0:
        plt.plot([c / a, c / a], [0, 1])
    else:
        def y(x):
            return (c - a * x) / b

        plt.plot([0, 1], [y(0), y(1)], **kwargs)


# print(logistic_cost(0.35, 1, 0.56))
# print(logistic_cost(1, 1, 1))
# plot_data(scaled_car_data)
# for i in range(0, 1000, 100):
#     a, b, c = gradient_descent(logistic_cost, 1, 1, 1, max_steps=i)
#     plot_line(a, b, c, alpha=i / 1000)
# plt.show()
def best_logistic_classifier(x, p):
    l = make_logistic(3.716700279792025, 11.422062341821322, 5.596878330572123)
    if l(x, p) > 0.5:
        return 1
    else:
        return 0


print(test_classifier(best_logistic_classifier, scaled_car_data))
