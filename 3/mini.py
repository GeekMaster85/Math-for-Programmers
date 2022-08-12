from vectors import rotate2d
from transforms import *
from math import *

rotate_45 = curry2(rotate2d)(pi / 4)
rotation_matrix = infer_matrix(2, rotate_45)
print(rotation_matrix)
scale_matrix = ((0.5, 0), (0, 0.5))
rotate_and_scale = matrix_multiply(scale_matrix, rotation_matrix)
((a, b), (c, d)) = rotate_and_scale
final_matrix = ((a, b, 2), (c, d, 2), (0, 0, 1))
