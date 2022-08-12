import numpy as np

a = (x * x for x in range(10))
print(list(a))
b = 1, 2, 3, 4, 5
print(b)
dog = {
    "name": "Melba",
    "age": 2
}
c = dog.items()
print(list(dog.items()))
q = [1, 2]
print(list(reversed(c)))


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# print(add(2, 3))
# print(add(*q))
def birthday(**kwargs):
    s = '"Happy birthday, %s ' % kwargs['name']
    if kwargs['age']:
        s += ", you're %d years old" % kwargs['age']
    return s + '!'


print(birthday(**dog))


def make_power_function(p):
    return lambda x: x ** p


print(make_power_function(2)(3))
print([x + 2 for x in range(10)])
def my_fun(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 0

my_numpy_fun = np.vectorize(my_fun)
print(my_numpy_fun(np.arange(0, 10)))
print(my_numpy_fun(6))
