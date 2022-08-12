from teapot import load_triangles
from draw_model import draw_model
from transforms import *


def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function
draw_model(polygon_map(scale_by(2), load_triangles()))