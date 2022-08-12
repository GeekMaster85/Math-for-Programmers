import numpy as np
from vectors import *


def standard_form(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    a = y2 - y1
    b = x1 - x2
    c = x1 * y2 - y1 * x2
    return a, b, c
def intersection(u1, u2, v1, v2):
    a1, b1, c1 = standard_form(u1, u2)
    a2, b2, c2 = standard_form(v1, v2)
    m = np.array(((a1, b1), (a2, b2)))
    c = np.array((c1, c2))
    return np.linalg.solve(m, c)
def do_segments_intersect(s1,s2):
    u1, u2 = s1
    v1, v2 = s2
    d1, d2 = distance(*s1), distance(*s2)
    try:
        x, y = intersection(u1, u2, v1, v2)
        return (distance(u1, (x, y)) <= d1 and
                distance(u2, (x, y)) <= d1 and
                distance(v1, (x, y)) <= d2 and
                distance(v2, (x, y)) <= d2)
    except np.linalg.linalg.LinAlgError:
        return False
def plane_equation(p1, p2, p3):
    parallel1 = subtract(p1, p2)
    parallel2 = subtract(p1, p3)
    a, b, c = cross(parallel2, parallel1)
    d = dot((a, b, c), p1)
    return a, b, c, d
# matrix = np.array(((0,0,0,0,1),(0,1,0,0,0),(0,0,0,1,0),(1,0,0,0,0),(1,1,1,0,0)))
# vector = np.array((3,1,-1,0,-2))
# print(np.linalg.solve(matrix, vector))
# print(plane_equation((1, 1, 1), (3, 0, 0), (0, 3, 0)))
matrix = np.array(((1,1,-1),(0,0,-1),(0,1,1)))
vec = np.array((-1, 3, 2))
inverse = np.linalg.inv(matrix)
print(inverse)
print(np.matmul(inverse, matrix))
print(np.matmul(inverse, vec))
print(np.linalg.solve(matrix, vec))