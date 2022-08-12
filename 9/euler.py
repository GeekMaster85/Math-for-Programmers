from vectors import add, scale
from draw2d import *
from draw3d import *
from math import pi, sin, cos

t = 0
s = (0, 0)
v = (1, 0)
a = (0, 0.2)
dt = 0.1
steps = int(10 // dt)
positions = [s]
for _ in range(steps):
    t += dt
    s = add(s, scale(dt, v))
    v = add(v, scale(dt, a))
    positions.append(s)


# draw2d(Points2D(*positions))


def eulers_method(s0, v0, a, total_time, step_count):
    trajectory = [s0]
    s = s0
    v = v0
    dt = total_time / step_count
    for _ in range(step_count):
        s = add(s, scale(dt, v))
        v = add(v, scale(dt, a))
        trajectory.append(s)
    return trajectory


angle = 20 * pi / 180
s0 = (0, 1.5)
v0 = (30 * cos(angle), 30 * sin(angle))
a = (0, -9.81)
result = eulers_method(s0, v0, a, 3, 100)


# draw2d(Points2D(*result))
def baseball_trajectory(degrees):
    radians = degrees * pi / 180
    s0 = (0, 0)
    v0 = (30 * cos(radians), 30 * sin(radians))
    a = (0, -9.8)
    return [(x, y) for (x, y) in eulers_method(s0, v0, a, 10, 1000) if y > 0]


# draw2d(Points2D(*baseball_trajectory(20)), Points2D(*baseball_trajectory(45)), Points2D(*baseball_trajectory(70)))
traj3d = eulers_method((0, 0, 0), (1, 2, 0), (1, -1, 1), 10, 10)
draw3d(Points3D(*traj3d))
