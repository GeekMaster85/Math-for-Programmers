from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map
from draw_model import multiply_matrix_vector


def transform(v):
    m = ((1, 1, 1), (1, 1, 1), (1, 0, 1))
    return multiply_matrix_vector(m, v)

draw_model(polygon_map(transform, load_triangles()))