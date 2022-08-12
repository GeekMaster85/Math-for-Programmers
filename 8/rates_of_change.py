import matplotlib.pyplot as plt
import numpy as np


def plot_function(f, tmin, tmax, tlabel=None, xlabel=None, axes=False, **kwargs):
    ts = np.linspace(tmin, tmax, 1000)
    if tlabel:
        plt.xlabel(tlabel, fontsize=18)
    if xlabel:
        plt.ylabel(xlabel, fontsize=18)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    if axes:
        total_t = tmax - tmin
        plt.plot([tmin - total_t / 10, tmax + total_t / 10], [0, 0], c='k', linewidth=1)
        plt.xlim(tmin - total_t / 10, tmax + total_t / 10)
        xmin, xmax = plt.ylim()
        plt.plot([0, 0], [xmin, xmax], c='k', linewidth=1)
        plt.ylim(xmin, xmax)


def plot_volume(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="volume (bbl)", axes=axes, **kwargs)


def interval_flow_rate(v, t1, t2, dt):
    return [(t, average_flow_rate(v, t, t + dt)) for t in np.arange(t1, t2, dt)]


def plot_flow_rate(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)


def volume(t):
    return (t - 4) ** 3 / 64 + 3.3


def flow_rate(t):
    return 3 * (t - 4) ** 2 / 64


def average_flow_rate(v, t1, t2):
    return (v(t2) - v(t1)) / (t2 - t1)


def secant_line(f, x1, x2):
    def line(x):
        return f(x1) + (x - x1) * (f(x2) - f(x1)) / (x2 - x1)

    return line


def plot_secant(f, x1, x2, color='k'):
    line = secant_line(f, x1, x2)
    plot_function(line, x1, x2, c=color)
    plt.scatter([x1, x2], [f(x1), f(x2)], c=color)


# plot_volume(volume, 0, 10)
# plot_secant(volume, 4, 7)
# plt.show()
# plot_flow_rate(flow_rate, 0, 10)
# plt.show()
# print(interval_flow_rate(volume, 0, 10, 1))
def plot_interval_flow_rates(volume, t1, t2, dt):
    series = interval_flow_rate(volume, t1, t2, dt)
    times = [t for (t, _) in series]
    rates = [r for (_, r) in series]
    plt.scatter(times, rates)


def instantaneous_flow_rate(v, t, digits=6):
    tolerance = 10 ** (-digits)
    h = 1
    approx = average_flow_rate(v, t - h, t + h)
    for i in range(2 * digits):
        h /= 10
        next_approx = average_flow_rate(v, t - h, t + h)
        if abs(next_approx - approx) < tolerance:
            return round(next_approx, digits)
        else:
            approx = next_approx
    raise Exception('Derivative did not converge')


def get_flow_rate_function(v):
    def flow_rate_function(t):
        return instantaneous_flow_rate(v, t)

    return flow_rate_function


# print(instantaneous_flow_rate(volume, 1))
# plot_interval_flow_rates(volume, 0, 10, 0.2)
def small_volume_change(q, t, dt):
    return q(t) * dt


def volume_change(q, t1, t2, dt):
    return sum(small_volume_change(q, t, dt) for t in np.arange(t1, t2, dt))


# print(volume(1))
# print(secant_line(volume,0.999,1.001)(1))
# plot_function(flow_rate, 0, 10)
# plot_function(get_flow_rate_function(volume), 0, 10)
# print(volume_change(flow_rate, 0, 6, 0.01))
# print(volume_change(flow_rate, 6, 10, 0.01))
def approximate_volume(q, v0, dt, t):
    return v0 + volume_change(q, 0, t, dt)


def approximate_volume_function(q, v0, dt):
    def volume(t):
        return approximate_volume(q, v0, dt, t)

    return volume


# plot_function(approximate_volume_function(flow_rate, 2.3, 0.1), 0, 10)


# plot_function(volume, 0, 10)
def get_volume(q, v0, digits=6):
    def volume(t):
        tolerance = 10 ** -(digits)
        dt = 1
        approx = v0 + volume_change(q, 0, t, dt)
        for i in range(digits * 2):
            dt /= 10
            next_approx = v0 + volume_change(q, 0, t, dt)
            if abs(next_approx - approx) < tolerance:
                return round(next_approx, digits)
            else:
                approx = next_approx
        raise Exception('did not converge')

    return volume


print(get_volume(flow_rate, 2.3, 6)(1))

plot_function(lambda x: 5 * x ** 4, 0, 1)
plt.show()

# print(average_flow_rate(volume, 0, 10))
