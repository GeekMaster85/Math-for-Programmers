# Suppose u = (-1, 1) and v = (1, 1), and suppose r and s are real numbers.
# Specifically, let’s assume -1< r < 1 and -3 < s < 3.
# Where are the possible points on the plane where the vector r ∙ u + s ∙ v could end up?
from random import uniform
from vec import *
u = (-1, 1)
v = (1, 1)
def random_r():
    return uniform(-3, 3)
def random_s():
    return uniform(-1, 1)
possibilities = [add(scale(random_r(), u), scale(random_s(), v))
                 for i in range(500)]
draw(Points(*possibilities))
