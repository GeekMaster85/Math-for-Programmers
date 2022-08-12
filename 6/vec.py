from math import sin, isclose
from random import uniform, randint

from plot import *
from vectors import add, scale

from abc import *


class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    def __truediv__(self, scalar):
        return self.scale(1 / scalar)

    def __sub__(self, other):
        return self.add(-1 * other)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)
    @classmethod
    def zero(cls):
        pass


class Vec0(Vector):
    def __init__(self):
        pass

    def add(self, other):
        return Vec0()

    def scale(self, scalar):
        return Vec0()

    @classmethod
    def zero(cls):
        return Vec0()

    def __eq__(self, other):
        return self.__class__ == other.__class__ == Vec0

    def __repr__(self):
        return "Vec0()"

    @classmethod
    @abstractproperty
    def zero(cls):
        pass

    def __neg__(self):
        return self.scale(-1)


class Vec2(Vector):
    @classmethod
    def zero(cls):
        pass

    def add(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self, scalar):
        return Vec2(scalar * self.x, scalar * self.y)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and \
               self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Vec2({}, {})".format(self.x, self.y)


class Vec3(Vector):
    @classmethod
    def zero(cls):
        return Vec3(0, 0, 0)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, scalar):
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)

    def __eq__(self, other):
        return (self.x == other.x
                and self.y == other.y
                and self.z == other.z)

    def __repr__(self):
        return 'Vec3({}, {}, {})'.format(self.x, self.y, self.z)


def avg(v1, v2):
    return 0.5 * (v1 + v2)


class CoordinateVector(Vector):
    @abstractproperty
    def dimension(self):
        pass

    def __init__(self, *coordinates):
        self.coordinates = tuple(x for x in coordinates)

    def add(self, other):
        return self.__class__(*add(self.coordinates, other.coordinates))

    def scale(self, scalar):
        return self.__class__(*scale(scalar, self.coordinates))

    def __repr__(self):
        return '{}{}'.format(self.__class__.__qualname__, self.coordinates)


class Vec6(CoordinateVector):
    def dimension(self):
        return 6


class Matrix5_by_3(Vector):
    rows = 5
    columns = 3

    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        return Matrix5_by_3(tuple(
            tuple(a + b for a, b in zip(row1, row2))
            for (row1, row2) in zip(self.matrix, other.matrix)
        ))

    def scale(self, scalar):
        return Matrix5_by_3(tuple(
            tuple(scalar * x for x in row)
            for row in self.matrix
        ))

    @classmethod
    def zero(cls):
        return Matrix5_by_3(tuple(
            tuple(0 for j in range(cls.columns))
            for i in range(cls.rows)
        ))


class Function(Vector):
    def __init__(self, f):
        self.function = f

    def add(self, other):
        return Function(lambda x: self.function(x) + other.function(x))

    def scale(self, scalar):
        return Function(lambda x: scalar * self.function(x))

    @classmethod
    def zero(cls):
        return Function(lambda x: 0)

    def __call__(self, arg):
        return self.function(arg)


def approx_equal_function(f, g):
    res = []
    for _ in range(10):
        x = uniform(-10, 10)
        res.append(isclose(f(x), g(x)))
    return all(res)


class Function2(Vector):
    def __init__(self, f):
        self.function = f

    def add(self, other):
        return Function2(lambda x, y: self.function(x, y) + other.function(x, y))

    def scale(self, scalar):
        return Function2(lambda x, y: scalar * self.function(x, y))

    @classmethod
    def zero(cls):
        return Function2(lambda x, y: 0)

    def __call__(self, *args):
        return self.function(*args)


class Matrix(Vector):
    @abstractproperty
    def rows(self):
        pass

    @abstractproperty
    def columns(self):
        pass

    def __init__(self, entries):
        self.entries = entries

    def add(self, other):
        return self.__class__(
            tuple(
                tuple(self.entries[i][j] + other.entries[i][j]
                      for j in range(self.columns()))
                for i in range(self.rows())
            )
        )

    def scale(self, scalar):
        return self.__class__(
            tuple(
                tuple(scalar * e for e in row)
                for row in self.entries
            )
        )

    def __repr__(self):
        return "%s%r" % (self.__class__.__qualname__, self.entries)

    def zero(self):
        return self.__class__(
            tuple(
                tuple(0 for i in range(self.columns()))
                for j in range(self.rows())
            )
        )


class Matrix2_by_2(Matrix):
    def rows(self):
        return 2

    def columns(self):
        return 2


if __name__ == '__main__':
    # f = Function(lambda x: 0.5 * x + 3)
    # g = Function(sin)
    # plot([f, g, 2 * f + 3 * g], -10, 10)
    # print(approx_equal_function(lambda x: (x * x) / x, lambda x: x))
    # print(*[uniform(-10, 10) for _ in range(5)])
    # f = Function2(lambda x, y: x + y)
    # g = Function2(lambda x, y: x - y + 1)
    # print((f + g)(3, 5))
    # print(2 * Matrix2_by_2(((1, 2), (3, 4))) + Matrix2_by_2(((2, 5), (1, 2))))
    print([(randint(0, 255), randint(0, 255), randint(0, 255))
           for i in range(0, 2)])
