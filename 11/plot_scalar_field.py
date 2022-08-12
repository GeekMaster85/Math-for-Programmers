import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
def u(x,y):
    return 0.5 * (x**2 + y**2)

def plot_scalar_field(f, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap=cm.coolwarm, alpha=1,
                      antialiased=False):
    fig = plt.figure()
    fig.set_size_inches(7, 7)
    ax = fig.add_subplot(projection='3d')
    fv = np.vectorize(f)

    # Make data.
    X = np.arange(xmin, xmax, xstep)
    Y = np.arange(ymin, ymax, ystep)
    X, Y = np.meshgrid(X, Y)
    Z = fv(X, Y)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, color=c, alpha=alpha,
                           linewidth=0, antialiased=antialiased)
    plt.show()
plot_scalar_field(u, -5, 5, -5, 5)
