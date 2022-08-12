from PIL import Image
from vec import *


class ImageVector(Vector):
    size = (300, 300)

    def __init__(self, input):
        try:
            img = Image.open(input).resize(ImageVector.size)
            self.pixels = img.getdata()
        except:
            self.pixels = input

    def image(self):
        img = Image.new('RGB', ImageVector.size)
        img.putdata([(int(r), int(g), int(b)) for (r, g, b) in self.pixels])
        return img

    def add(self, other):
        return ImageVector([(r1 + r2, g1 + g2, b1 + b2)
                            for ((r1, g1, b1), (r2, g2, b2))
                            in zip(self.pixels, other.pixels)])

    def scale(self, scalar):
        return ImageVector([(scalar * r, scalar * g, scalar * b)
                            for (r, g, b) in self.pixels])

    @classmethod
    def zero(cls):
        total_pixels = cls.size[0] * cls.size[1]
        return ImageVector((0, 0, 0) for _ in range(total_pixels))

    def _repr_png_(self):
        return self.image()._repr_png_()()


def random_img():
    return ImageVector([(randint(0, 255), randint(0, 255), randint(0, 255))
                        for _ in range(3)])


class LinearFunction(Vector):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return LinearFunction(self.a + other.a, self.b + other.b)

    def scale(self, scalar):
        return LinearFunction(scalar * self.a, scalar * self.b)

    def __call__(self, x):
        return self.a * x + self.b

    @classmethod
    def zero(cls):
        return LinearFunction(0, 0)


class LF(Vec2):
    def __call__(self, input):
        return self.x * input + self.y


class QuadraticFunction(Vector):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self, other):
        return QuadraticFunction(self.a + other.a,
                                 self.b + other.b,
                                 self.c + other.c)

    def scale(self, scalar):
        return QuadraticFunction(scalar * self.a,
                                 scalar * self.b,
                                 scalar * self.c)

    def __call__(self, x):
        return self.a * x * x + self.b * x + self.c

    @classmethod
    def zero(cls):
        return QuadraticFunction(0, 0, 0)


class Polynomial(Vector):
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coefficient * x ** power
                   for (power, coefficient)
                   in enumerate(self.coefficients))

    def scale(self, scalar):
        return Polynomial([scalar * a for a in self.coefficients])

    def add(self, other):
        return Polynomial([a + b] for a, b in zip(self.coefficients, other.coefficients))

    def zero(cls):
        return Polynomial(0)


def solid_color(r, g, b):
    return ImageVector([(r, g, b) for _ in range(300 * 300)])
image_size = (300, 300)
total_pixels = image_size[0] * image_size[1]
square_count = 30
square_width = 10
def ij(n):
    return (n // image_size[0], n // image_size[1])
def to_lower(img):
    matrix = [
        [0 for i in range(square_count)]
        for j in range(square_count)
    ]
    for (n, p) in enumerate(img.pixels):
        i, j = ij(n)
        weight = 1 / (3 * square_width * square_width)
        matrix[i // square_width][j // square_width] += (sum(p) * weight)
    return matrix
def from_lower(matrix):
    def lower(pixels, i):
        i, j = ij
        return pixels[i // square_width][j // square_width]
    def make_highres(img):
        pixels = list(matrix)
        tri = lambda x: (x, x, x)
        return ImageVector([tri(lower(matrix, ij(n)) for n in range(total_pixels))])
    return make_highres(matrix)
# print(*enumerate([1, 2, 3]))
# gray = ImageVector([(1, 1, 1) for _ in range(3)])
# print(*gray.pixels)
# a, b = random_img(), random_img()
# print(a.pixels)
# print(b.pixels)
# for p1, p2 in zip(a.pixels, b.pixels):
#     print(p1, p2)
#     print(*zip(p1, p2))
