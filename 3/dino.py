from draw3d import *
from vec_draw import *
from matrix import *
from mini import *
dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                ]


# draw(
#     Points(*dino_vectors),
#     Polygon(*dino_vectors)
# )


def polygon_segments_3d(points, color='blue'):
    count = len(points)
    return [Segment3D(points[i], points[(i + 1) % count], color=color) for i in range(count)]


dino_3d = [(x, y, 1) for x, y in dino_vectors]

magic_matrix = (
    (1, 0, 3),
    (0, 1, 1),
    (0, 0, 1)
)
translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_3d]
rotate_and_translate = ((0, -1, 3), (1, 0, 1), (0, 0, 1))
rotated_translated_dino = [
    multiply_matrix_vector(rotate_and_translate, v)
    for v in dino_3d]
draw3d(
    Points3D(*dino_3d, color='blue'),
    *polygon_segments_3d(translated)

    # Points3D(*translated, color='red'),
    # Points3D(*rotated_translated_dino, color='green'),
    # *polygon_segments_3d(rotated_translated_dino),
    # *polygon_segments_3d(dino_3d),
)
back_2d = ((1, 0, 0), (0, 1, 0))
m = matrix_multiply(back_2d, magic_matrix)
m1 = matrix_multiply(back_2d, final_matrix)
vec = [multiply_matrix_vector(m, v) for v in dino_3d]
vec1 = [multiply_matrix_vector(m, v) for v in translated]
vec2 = [multiply_matrix_vector(m1, v) for v in dino_3d]
draw2d(Polygon2D(*vec, color="green"),
       Polygon2D(*vec2, color="purple"),
       )

