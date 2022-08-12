from math import cos, sin, pi, sqrt

import numpy as np
from matplotlib import pyplot as plt, cm


def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    plt.show()


def trajectory(theta, speed=20, height=0, dt=0.01, g=-9.81):
    vx = speed * cos(pi * theta / 180)
    vz = speed * sin(pi * theta / 180)
    t, x, z = 0, 0, height
    ts, xs, zs = [t], [x], [z]
    while z >= 0:
        t += dt
        vz += g * dt
        x += vx * dt
        z += vz * dt
        ts.append(t)
        xs.append(x)
        zs.append(z)
    return ts, xs, zs


def flat_ground(x, y):
    return 0


def ridge(x, y):
    return (x ** 2 - 5 * y ** 2) / 2500


def trajectory3d(theta, phi, speed=20, height=0, dt=0.01, g=-9.81, elevation=flat_ground, drag=0.0):
    vx = speed * cos(pi * theta / 180) * cos(pi * phi / 180)
    vy = speed * cos(pi * theta / 180) * sin(pi * phi / 180)
    vz = speed * sin(pi * theta / 180)
    t, x, y, z = 0, 0, 0, height
    ts, xs, ys, zs = [t], [x], [y], [z]
    while z >= elevation(x, y):
        t += dt
        vx -= (drag * vx) * dt
        vy -= (drag * vy) * dt
        vz += (g - drag * vz) * dt
        x += vx * dt
        y += vy * dt
        z += vz * dt
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return ts, xs, ys, zs


def plot_trajectories_3d(*trajs, elevation=flat_ground, bounds=None, zbounds=None, shadows=False):
    fig, ax = plt.gcf(), plt.gca(projection='3d')
    fig.set_size_inches(7, 7)
    ax.view_init(0, 270)
    if not bounds:
        xmin = min([x for traj in trajs for x in traj[1]])
        xmax = max([x for traj in trajs for x in traj[1]])
        ymin = min([x for traj in trajs for x in traj[2]])
        ymax = max([x for traj in trajs for x in traj[2]])

        padding_x = 0.1 * (xmax - xmin)
        padding_y = 0.1 * (ymax - ymin)
        xmin -= padding_x
        xmax += padding_x
        ymin -= padding_y
        ymax += padding_x

    else:
        xmin, xmax, ymin, ymax = bounds

    plt.plot([xmin, xmax], [0, 0], [0, 0], c='k')
    plt.plot([0, 0], [ymin, ymax], [0, 0], c='k')

    g = np.vectorize(elevation)
    ground_x = np.linspace(xmin, xmax, 20)
    ground_y = np.linspace(ymin, ymax, 20)
    ground_x, ground_y = np.meshgrid(ground_x, ground_y)
    ground_z = g(ground_x, ground_y)
    ax.plot_surface(ground_x, ground_y, ground_z, cmap=cm.coolwarm, alpha=0.5,
                    linewidth=0, antialiased=True)
    for traj in trajs:
        ax.plot(traj[1], traj[2], traj[3])
        if shadows:
            ax.plot([traj[1][0], traj[1][-1]], [traj[2][0], traj[2][-1]], [0, 0], c='gray', linestyle='dashed')

    if zbounds:
        ax.set_zlim(*zbounds)
    plt.show()


def plot_trajectories(*trajs, show_seconds=False):
    for traj in trajs:
        xs, zs = traj[1], traj[2]
        plt.plot(xs, zs)
        if show_seconds:
            second_indices = []
            second = 0
            for i, t in enumerate(traj[0]):
                if t >= second:
                    second_indices.append(i)
                    second += 1
            plt.scatter([xs[i] for i in second_indices],
                        [zs[i] for i in second_indices])
    xl = plt.xlim()
    plt.plot(plt.xlim(), [0, 0], c='k')
    plt.xlim(*xl)

    width = 7
    coords_height = (plt.ylim()[1] - plt.ylim()[0])
    coords_width = (plt.xlim()[1] - plt.xlim()[0])
    plt.gcf().set_size_inches(width, width * coords_height / coords_width)
    plt.show()


def landing_pos(traj):
    return traj[1][-1]


def hang_time(traj):
    return traj[0][-1]


def max_height(traj):
    return max(traj[2])


def plot_trajectory_metric(metric, thetas, **settings):
    plt.scatter(thetas, [metric(trajectory(theta, **settings))
                         for theta in thetas])
    plt.show()


# plot_trajectories_3d(
#     trajectory3d(20,0,elevation=ridge),
#     trajectory3d(20,270,elevation=ridge),
#     bounds=[0,40,-40,0],
#     elevation=ridge)
B = 0.001  # <1>
C = 0.005
v = 20
g = -9.81


def velocity_component(speed, theta, phi):
    vx = speed * cos(pi * theta / 180) * cos(pi * phi / 180)
    vy = speed * cos(pi * theta / 180) * sin(pi * phi / 180)
    vz = speed * sin(pi * theta / 180)
    return vx, vy, vz


def landing_distance(theta, phi):
    vx, vy, vz = velocity_component(v, theta, phi)
    v_xy = sqrt(vx ** 2 + vy ** 2)
    a = (g / 2) - B * vx ** 2 + C * vy ** 2
    b = vz
    landing_time = -b / a
    landing_distance = v_xy * landing_time
    return landing_distance


# plot_trajectories_3d(
#     trajectory3d(20,-20,elevation=ridge),
#     trajectory3d(20,-20,elevation=ridge,drag=0.1),
#     bounds=[0,40,-40,0],
#     elevation=ridge)
def secant_slope(f, xmin, xmax):
    return (f(xmax) - f(xmin)) / (xmax - xmin)


def approx_derivative(f, x, dx=1e-6):
    return secant_slope(f, x - dx, x + dx)


def approx_gradient(f, x0, y0):
    patial_x = approx_derivative(lambda x: f(x, y0), x0)
    patial_y = approx_derivative(lambda y: f(x0, y), y0)
    return (patial_x, patial_y)


def landing_distance_gradient(theta, phi):
    return approx_gradient(landing_distance_gradient, theta, phi)


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def gradient_ascent(f, xstart, ystart, rate=1, tolerance=1e-6):
    x = xstart
    y = ystart
    xs, ys = [x], [y]
    grad = approx_gradient(f, x, y)
    while length(grad) > tolerance:
        x += rate * grad[0]
        y += rate * grad[1]
        grad = approx_gradient(f, x, y)
        xs.append(x)
        ys.append(y)
    return xs, ys


def count_ascent_steps(f, x, y, rate=1):
    gap = gradient_ascent(f, x, y, rate=rate)
    print(gap[0][-1], gap[1][-1])
    return len(gap[0])


# print(gradient_ascent(landing_distance, 0, 180))
# print(count_ascent_steps(landing_distance, 36, 83, rate=40))
# print(gradient_ascent(landing_distance, 36, 83))
# from random import uniform
# for x in range(0,20):
#     gap = gradient_ascent(landing_distance,
#     uniform(0,90),
#     uniform(0,360))
#     plt.plot(*gap,c='k')
# plt.show()
def simulated_distance_270(theta):
    ts, xs, ys, zs = trajectory3d(theta, 270)
    return sqrt(xs[-1] ** 2 + ys[-1] ** 2)


plot_function(simulated_distance_270, 35, 45)
plt.show()
