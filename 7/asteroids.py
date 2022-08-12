from math import pi
from random import randint, uniform
from vectors import *
import pygame
import numpy as np
from linear_solver import *

class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0
    def transformed(self):
        rotated = [rotate2d(self.rotation_angle, v) for v in self.points]
        return [add((self.x, self.y), v) for v in rotated]

    def does_intersect(self, laser):
        for segment in self.segments():
            if do_segments_intersect(laser, segment):
                return True
        return False
    def segments(self):
        point_count = len(self.points)
        points = self.transformed()
        return [(points[i], points[(i + 1) % point_count])
                for i in range(point_count)]
    def does_collide(self, other):
        for s in self.segments():
            if other.does_intersect(s):
                return True
        return False
class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (0.25, 0.6), (-0.8, 0.2)])


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        vs = [to_cartesian((uniform(0.5, 1), 2 * pi * i / sides))
              for i in range(sides)]
        super().__init__(vs)


ship = Ship()
asteroid_count = 10
asteroids = [Asteroid() for _ in range(asteroid_count)]
for a in asteroids:
    a.x = randint(-9, 9)
    a.y = randint(-9, 9)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

width, height = 400, 400


def to_pixel(x, y):
    return (width / 2 + width * x / 20, height / 2 - height * y / 20)


def draw_poly(screen, polygon_model, color=GREEN):
    pixel_points = [to_pixel(x, y) for x, y in polygon_model.transformed]
    pygame.draw.aaline(screen, color, True, pixel_points, 10)
def main():
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Asteroids!")
    done = False
    clock = pygame.time.Clock()
    p_pressed = False
    while not done:
        clock.tick()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

asteroid = PolygonModel([(2,7), (1,5), (2,3), (4,2), (6,2), (7,4), (6,6), (4,6)])
print(asteroid.does_intersect([(0, 0), (0, 7)]))
