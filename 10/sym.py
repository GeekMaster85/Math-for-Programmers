from sympy import *
x = Symbol('x')
print(type(x))
print((3 * x ** 2).integrate(x))