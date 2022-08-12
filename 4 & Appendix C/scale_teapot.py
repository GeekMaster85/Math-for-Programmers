from vectors import *
from teapot import load_triangles
from draw_model import draw_model

original_triangles = load_triangles()
scaled_triangles = [

    [add(scale(2, vertex), (-1, 0, 0)) for vertex in triangle]
    for triangle in original_triangles
]
draw_model(scaled_triangles)