import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    return (-2 - x, 1 - y)
def plot_vector_field(f,xmin,xmax,ymin,ymax,xstep=1,ystep=1):
    x_, y_ = np.meshgrid(np.arange(xmin, xmax, xstep), np.arange(ymin, ymax, ystep))
    u = np.vectorize(lambda x, y: f(x, y)[0])(x_, y_)
    v = np.vectorize(lambda x, y: f(x, y)[1])(x_, y_)
    plt.quiver(x_, y_, u, v, color='blue')
    fig = plt.gcf()
    fig.set_size_inches(7, 7)
plot_vector_field(f, -5,5,-5,5)
plt.show()
