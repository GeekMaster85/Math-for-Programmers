from vec import *


def multiply(matrix, vector):
    return linear_combination(vector, *zip(*matrix))


B = (
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)


def matrix_multiply(a, b):
    return tuple(
        tuple(dot(row, col) for col in zip(*b)) for row in a
    )


def multiply_matrix_vector(matrix, vector):
    return tuple(
        sum(vector_entry * matrix_entry
            for matrix_entry, vector_entry in zip(row, vector))
        for row in matrix
    )


def multiply_matrix_vector1(matrix, vector):
    return tuple(
        dot(row, vector)
        for row in matrix
    )


def transpose(matrix):
    return tuple(zip(*matrix))

# v = (3, -2, 5)
a = ((2, 1, 0), )
# print(transpose(a))
# b = ((1, 2, 1), )
#
# print(matrix_multiply(a, b))
# z = []
# for row in a:
#     z += zip(row, b)
# print(*z)
# print(sum(vector_entry * matrix_entry
#           for vector_entry, matrix_entry in z))
# print(multiply_matrix_vector1(a, b))
