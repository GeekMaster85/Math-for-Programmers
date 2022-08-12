from random import random

import matplotlib.cm

from draw2d import *
from draw3d import *
from math import *


# draw3d(Points3D((2, 2, 2), (1, -2, -2)),
#        Arrow3D((2, 2, 2)),
#        Arrow3D((1, -2, -2)),
#        Segment3D((2, 2, 2), (1, -2, -2)),
#        Box3D(2, 2, 2),
#        Box3D(1, -2, -2)
# )
# pm1 = [-1, 1]
# vertices = [(x, y, z) for x in pm1 for y in pm1 for z in pm1]
# edges = [((-1, y, z), (1, y, z)) for y in pm1 for z in pm1 ] + \
#         [((x, -1, z), (x, 1, z)) for x in pm1 for z in pm1] + \
#         [((x, y, -1), (x, y, 1)) for x in pm1 for y in pm1]
# draw3d(Points3D(*vertices), *[Segment3D(*edge) for edge in edges])
def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)
    # return tuple(map(sum, zip(*vectors)))


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def scale(scalar, v):
    return tuple(scalar * coord for coord in v)


def unit_vec(v):
    return scale(1 / length(v), v)


def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return length * cos(angle), length * sin(angle)


def angle_between(v1, v2):
    return acos(dot(v1, v2) / (length(v1) * length(v2)))


def random_vector_of_length(l):
    return to_cartesian((l, 2 * pi * random()))


pairs = [(random_vector_of_length(3), random_vector_of_length(7)) for i in range(3)]


# for u, v in pairs:
#     print("u = %s, v = %s" % (u, v))
#     print("length of u: %f, length of v: %f, dot product :%f" % (length(u), length(v), dot(u, v)))


def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)


octahedron = [
    [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
    [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
    [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, 0, 1), (0, 1, 0)],
    [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
    [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
]


def vertices(faces):
    return set([vertex for face in faces for vertex in face])


def component(v, direction):
    return dot(v, direction) / length(direction)


def vector_to_2d(v):
    return (component(v, (1, 0, 0)), component(v, (0, 1, 0)))


def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]


def subtract(v1, v2):
    return tuple(v1 - v2 for (v1, v2) in zip(v1, v2))


def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]
    return add(*scaled)


def normal(face):
    return cross(subtract(face[1], face[0]), subtract(face[2], face[1]))


blues = matplotlib.cm.get_cmap('Blues')


def render(faces, light=(1, 2, 3), color_map=blues, lines=None):
    polygons = []
    for face in faces:
        unit_normal = unit_vec(normal(face))
        if (unit_normal[2] > 0):
            c = color_map(1 - dot(unit_vec(normal(face)), unit_vec(light)))
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines)
            polygons.append(p)
    draw2d(*polygons, axes=False, origin=False, grid=None)


# render(octahedron, lines=black)
top = (0, 0, 1)
bottom = (0, 0, -1)
xy_plane = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
edges = [Segment3D(top, p) for p in xy_plane] + \
        [Segment3D(bottom, p) for p in xy_plane] + \
        [Segment3D(xy_plane[i], xy_plane[(i + 1) % 4]) for i in range(4)]
draw3d(*edges)
