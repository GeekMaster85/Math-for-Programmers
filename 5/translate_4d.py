from matrix import *


def translate_4d(translation):
    def new(target):
        a, b, c, d = translation
        x, y, z, w = target
        matrix = (
            (1, 0, 0, 0, a),
            (0, 1, 0, 0, b),
            (0, 0, 1, 0, c),
            (0, 0, 0, 1, d),
            (0, 0, 0, 0, 1))
        vectors = (x, y, z, w, 1)
        x_out, y_out, z_out, w_out, _ = multiply_matrix_vector(matrix, vectors)
        return (x_out, y_out, z_out, w_out)

    return new


print(translate_4d((1, 2, 3, 4))((10, 20, 30, 40)))
