from math import exp

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

digits = datasets.load_digits()
a = digits.images
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)
# for i in range(8):
#     for j in range(8):
#         b =  plt.gca()
#         plt.gca().text(i - 0.15, j, int(digits.images[0][i][j]))
# plt.show()
c = digits.images[0].flatten() / 15


def random_classifier(input_vector):
    return np.random.rand(10)


res = random_classifier(c)


# print(list(res).index(max((res))))
# print(digits.target[0])
def test_digit_classify(classifier, start=0, test_count=1000):
    correct = 0
    end = start + test_count
    for img, target in zip(digits.images[start:end], digits.target[start:end]):
        v = np.matrix.flatten(img)

        output = classifier(v)
        answer = list(output).index(max(output))
        if answer == target:
            correct += 1
    return correct / test_count


# print(test_digit_classify(random_classifier))
def average_img(i):
    imgs = [img for img, target in zip(digits.images[:], digits.target[:]) if target == i]
    a = sum(imgs) / len(imgs)
    return sum(imgs) / len(imgs)


# plt.imshow(average_img(6), cmap=plt.cm.gray_r)
# plt.show()
avg_digits = [np.matrix.flatten(average_img(i)) for i in range(10)]


def compare_to_avg(v):
    return [np.dot(v, avg_digits[i]) for i in range(10)]


def sigmoid(x):
    return 1 / (1 + exp(-x))


# print(test_digit_classify(compare_to_avg))
class MLP():
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        a = layer_sizes[:-1]
        b = layer_sizes[1:]
        self.weights = [
            np.random.rand(n, m)
            for m, n in zip(layer_sizes[:-1], layer_sizes[1:])
        ]
        self.biases = [np.random.rand(n) for n in layer_sizes[1:]]

    def feedforward(self, v):
        activations = []
        a = v
        activations.append(a)
        for w, b in zip(self.weights, self.biases):
            z = w @ a + b
            a = [sigmoid(x) for x in z]
            activations.append(a)
        return activations

    def evaluate(self, v):
        return np.array(self.feedforward(v)[-1])



mlp = MLPClassifier(hidden_layer_sizes=(16,), activation='logistic', max_iter=100, verbose=True, random_state=1,
                    learning_rate_init=.1)
x = np.array([np.matrix.flatten(img) for img in digits.images[:1000]]) / 15
y = digits.target[:1000]
mlp.fit(x, y)

v = np.matrix.flatten(digits.images[0] / 15)
# print(nn.evaluate(v))
# print(test_digit_classify(nn.evaluate))
# nn = MLP([2, 4, 3])
# print(nn.weights)
# print(nn.biases)



def sklearn_trained_classify(v):
    return mlp.predict([v])[0]


# a = sklearn_trained_classify(v)
# x_ = np.array([np.matrix.flatten(img) for img in digits.images[:]]) / 15
# all = mlp.predict(x_)
# c = 0
# for (i, j) in zip(all, digits.target[:]):
#     if i == j:
#         c += 1
# print(c / len(all))
nn = MLP([64, 16, 10])
nn.weights = [w.T for w in mlp.coefs_]
nn.biases = mlp.intercepts_
print(test_digit_classify(nn.evaluate,start=1000,test_count=500))


def y_vec(digit):
    return np.array([1 if i == digit else 0] for i in range(10))


def cost_one(classifier, x, i):
    return sum((classifier(x)[j] - y_vec(i)[j]) ** 2 for j in range(10))


def avg_cost(classifier):
    return sum(cost_one(classifier, x[j], y[j]) for j in range(1000)) / 1000
from sympy import *
x = symbols('x')
print(diff(1 / (1 + exp(-x)), x))