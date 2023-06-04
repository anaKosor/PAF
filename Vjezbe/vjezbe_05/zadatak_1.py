import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5*x**2 - 2*x

def df(x):
    return 10*(x) - 2

x, y = cal.derivacije(f, -3, 3, 0.1)
x1, y1 = cal.derivacije(f, -3, 3, 0.01)
x_list = [x for x in np.arange(-3, 3, 0.01)]
plt.scatter(y, x)
plt.scatter(y1, x1)
plt.plot(x_list, df(np.array(x_list)), c = 'r')
plt.show()
