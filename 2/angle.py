from math import *
from vec import *


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return length * cos(angle), length * sin(angle)


def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return length(vector), angle


# polar_coords = [(cos(pi * x / 100), pi * x / 500) for x in range(1000)]
# vectors = [to_cartesian(p) for p in polar_coords]
# draw(Polygon(*vectors, color=green))
def rotate(rotation_angle, vectors):
    dino_polar = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a + rotation_angle)) for l, a in dino_polar]
    # dino_rotated_polar = [(l, angle + rotation_angle) for l, angle in dino_polar]
    # dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
    # return dino_rotated


new_dino = translate((8, 8), rotate(5 * pi/3, dino_vectors))
new_dino1 = rotate(5 * pi/3, translate((8, 8), dino_vectors))
draw(Polygon(*new_dino), Polygon(*dino_vectors, color=red), Polygon(*new_dino1, color=green))
# def regular_polygon(n):
#     return [to_cartesian((1, 2 * pi * k / n)) for k in range(n)]
# draw(Polygon(*regular_polygon(7)))