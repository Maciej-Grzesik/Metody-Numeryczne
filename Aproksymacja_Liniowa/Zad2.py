import numpy as np
import matplotlib.pyplot as plt


class LinearLeastSquares:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def fit(xx):
        N = len(x)
        p = np.sum(x)
        q = np.sum(y)
        r = np.sum(np.multiply(x, y))
        s = np.sum(np.square(x))
        D = N * s - p ** 2
        a = (N * r - p * q) / D
        b = (s * q - p * r) / D
        yy = a * xx + b
        return yy


x = np.linspace(-1, 2, 10)
y = 2.0 * x + 1.0 + np.random.rand(10)
model = LinearLeastSquares(x, y)

xx = np.linspace(-1, 2, 20)
yy = model.fit(xx)

plt.plot(xx, yy, '-', x, y, 'o')
plt.xlabel('$x$')
plt.ylabel('$y$', rotation=0)
plt.show()
