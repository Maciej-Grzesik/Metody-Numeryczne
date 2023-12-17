import numpy as np
import matplotlib.pyplot as plt

class LinearLeastSquares:
    def __init__(self, x, y):
        self.N = len(x)
        self.p = np.sum(x)
        self.q = np.sum(y)
        self.r = np.sum(np.multiply(x, y))
        self.s = np.sum(np.square(x))
        self.D = self.N * self.s - self.p ** 2
        self.a = (self.N * self.r - self.p * self.q) / self.D
        self.b = (self.s * self.q - self.p * self.r) / self.D
    
    def fit(self, xx):
        yy = self.a * xx + self.b
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
