from vectors import *
from teapot import load_triangles
from draw_model import *
from math import pi


def rotate2d(angle, vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a + angle))


def rotate_z(angle, vector):
    x, y, z = vector
    new_x, new_y = rotate2d(angle, (x, y))
    return new_x, new_y, z


def rotate_z_by(angle):
    def new(v):
        return rotate_z(angle, v)

    return new


def cube_stretch_y(vector):
    x, y, z = vector
    return x, y ** 3, z


def slant_xy(vector):
    x, y, z = vector
    return (x + y, y, z)


def translate_by(translation):
    def new(v):
        return add(translation, v)

    return new


# draw_model(polygon_map(rotate_z_by(pi / 4), load_triangles()))
# draw_model(polygon_map(translate_by((0, 0, -20)), load_triangles()))
Ae1 = (1, 1, 1)
Ae2 = (1, 0, -1)
Ae3 = (0, 1, 1)


def apply_A(v):
    return add(scale(v[0], Ae1), scale(v[1], Ae2), scale(v[2], Ae3))


def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]
    return add(*scaled)


def transform_standard_basis(transform):
    return transform((1, 0, 0)), transform((0, 1, 0)), transform((0, 0, 1))


print(linear_combination([1, 2, 3], (1, 0, 0), (0, 1, 0), (0, 0, 1)))
print(transform_standard_basis(rotate_z_by(pi / 2)))
# draw_model(polygon_map(apply_A, load_triangles()))
