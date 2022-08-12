from vector_drawing import *

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                ]
# draw(
#     Points(*[(x, x ** 2) for x in range(-10, 11)]),
#     grid=(1, 10),
#     nice_aspect_ratio=False
# )


def add(*vectors):
    return sum([v[0] for v in vectors]), sum([v[1] for v in vectors])


dino_vectors2 = [add(vec, (1, 2)) for vec in dino_vectors]
# draw(Points(*dino_vectors, color=red), Polygon(*dino_vectors, color=red), Points(*dino_vectors2),
#      Polygon(*dino_vectors2))


def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


# print(add((1, 2), (1, 2), (1, 2)))


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]

def scale(scalar, vector):
    return scalar * vector[0], scalar * vector[1]
def hundred_dinos():
    translations = [(12 * x, 10 * y)
                    for x in range(-5, 5)
                    for y in range(-5, 5)]
    dinos = [Polygon(*translate(t, dino_vectors)) for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)
# hundred_dinos()
# print(translate((1,1), [(0,0), (0,1,), (-3,-3)]))
# print(max(dino_vectors, key=length))

