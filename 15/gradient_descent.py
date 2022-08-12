from math import sqrt


def length(v):
    return sqrt(sum(vi * vi for vi in v))


def secant_slope(f, xmin, xmax):
    return (f(xmax) - f(xmin)) / (xmax - xmin)


def approx_derivative(f, x, dx=1e-6):
    return secant_slope(f, x - dx, x + dx)


def approx_gradient(f, x0, y0, z0):
    partial_x = approx_derivative(lambda x: f(x, y0, z0), x0)
    partial_y = approx_derivative(lambda y: f(x0, y, z0), y0)
    partial_z = approx_derivative(lambda z: f(x0, y0, z), z0)
    return partial_x, partial_y, partial_z


def gradient_descent(f, xstart, ystart, zstart, tolerance=1e-6, max_steps=1000):
    x = xstart
    y = ystart
    z = zstart
    grad = approx_gradient(f, x, y, z)
    steps = 0
    while length(grad) > tolerance and steps < max_steps:
        x -= 0.01 * grad[0]
        y -= 0.01 * grad[1]
        z -= 0.01 * grad[2]
        grad = approx_gradient(f, x, y, z)
        steps += 1
    return x, y, z



