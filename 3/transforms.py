from vectors import *


################################################################
# Vector transformation functions we'll introduce in Chapter 4 #
# (also used to render the teapot)                             #
################################################################

def compose1(f1, f2):
    def new_function(input):
        return f1(f2(input))

    return new_function


def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i == j else 0 for j in range(1, n + 1))

    standard_basis = [standard_basis_vector(i) for i in range(1, n + 1)]
    cols = [transformation(v) for v in standard_basis]
    return tuple(zip(*cols))


def compose2(f1, f2):
    return lambda x: f1(f2(x))


def matrix_multiply(a, b):
    return tuple(
        tuple(dot(row, col) for col in zip(*b)) for row in a
    )


def compose(*args):
    def new(input):
        state = input
        for f in reversed(args):
            state = f(state)
        return state

    return new


def prepend(string):
    def new(input):
        return string + input

    return new


f = compose(prepend('p'), prepend('y'), prepend('t'))
print(f('hon'))


def curry2(f):
    def g(x):
        def new(y):
            return f(x, y)

        return new

    return g


scale_by = curry2(scale)
print(scale_by(2)((1, 2, 3)))


def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]


def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)

    return new_function


def translate_by(translation):
    def new_function(v):
        return add(translation, v)

    return new_function


def rotate_z(angle, vector):
    x, y, z = vector
    new_x, new_y = rotate2d(angle, (x, y))
    return new_x, new_y, z


def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle, v)

    return new_function


def stretch_x(scalar, vector):
    x, y, z = vector
    return (scalar * x, y, z)


def stretch_x_by(scalar):
    def new(vector):
        return stretch_x(scalar, vector)

    return new


def rotate_x(angle, vector):
    x, y, z = vector
    new_y, new_z = rotate2d(angle, (y, z))
    return x, new_y, new_z


def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle, v)

    return new_function


def rotate_y(angle, vector):
    x, y, z = vector
    new_x, new_z = rotate2d(angle, (x, z))
    return new_x, y, new_z


def rotate_y_by(angle):
    def new_function(v):
        return rotate_y(angle, v)

    return new_function


def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))


B = (
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)

v = (1, -2, -2)


def transform_standard_basis(transform):
    return transform((1, 0, 0)), transform((0, 1, 0)), transform((0, 0, 1))
