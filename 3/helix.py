from math import *
from vec import *
vs = [(sin(pi * t / 6), cos(pi * t / 6), 1 / 3) for t in range(24)]
running_sum = (0,0,0)
arrows = []
for v in vs:
    next_sum = add(running_sum, v)
    arrows.append(Arrow3D(next_sum, running_sum))
    running_sum = next_sum

print(running_sum)
draw3d(*arrows)