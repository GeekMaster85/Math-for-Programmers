from transforms import *
from matrix import *
from random import randint


def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i == j else 0 for j in range(1, n + 1))

    standard_basis = [standard_basis_vector(i) for i in range(1, n + 1)]
    cols = [transformation(v) for v in standard_basis]
    return tuple(zip(*cols))


# print(infer_matrix(3, rotate_z_by(pi / 2)))
def random_matrix(rows, cols, min=-2, max=2):
    return tuple(
        tuple(
            randint(min, max) for i in range(cols))
        for j in range(rows)
    )
def project_xy(v):
    x, y, z = v
    return (x, y)


print(infer_matrix(3, project_xy))



a = ((1, 1, 0), (1, 0, 1), (1, -1, 1))
b = ((0, 2, 1), (0, 1, 0), (1, 0, -1))


def transform_a(v):
    return multiply_matrix_vector(a, v)


def transform_b(v):
    return multiply_matrix_vector(b, v)


compose_a_b = compose(transform_a, transform_b)


# print(infer_matrix(3, compose_a_b))
# print(matrix_multiply(a, b))
# print(random_matrix(3, 3, 0, 10))
def matrix_power(power, matrix):
    res = matrix
    for _ in range(1, power):
        res = matrix_multiply(matrix, res)
    return res


# print(matrix_power(3, ((1, 1, 0), (1, 0, 1), (1, -1, 1))))
