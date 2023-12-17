import numpy as np
import matplotlib.pyplot as plt

class LinearApproximation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def uniform_approximation(self):
        N = len(self.x)
        p = np.sum(self.x)
        q = np.sum(self.y)
        
        a = (N * np.sum(np.multiply(self.x, self.y)) - p * q) / (N * np.sum(np.square(self.x)) - p**2)
        b = (q - a * p) / N
        
        return a, b
    
    def least_squares_approximation(self):
        N = len(self.x)
        p = np.sum(self.x)
        q = np.sum(self.y)
        r = np.sum(np.multiply(self.x, self.y))
        s = np.sum(np.square(self.x))
        
        a = (N * r - p * q) / (N * s - p**2)
        b = (s * q - p * r) / (N * s - p**2)
        
        return a, b

    def fit_uniform(self, xx):
        a, b = self.uniform_approximation()
        yy = a * xx + b
        return yy
    
    def fit_least_squares(self, xx):
        a, b = self.least_squares_approximation()
        yy = a * xx + b
        return yy


x = np.linspace(-1, 2, 10)
y = 2.0 * x + 1.0 + np.random.rand(10)

model = LinearApproximation(x, y)

xx = np.linspace(-1, 2, 100)
yy_uniform = model.fit_uniform(xx)
yy_least_squares = model.fit_least_squares(xx)

print(yy_uniform)
print('#####')
print(yy_least_squares)


plt.figure(figsize=(8, 6))
plt.plot(xx, yy_uniform, label='Aproksymacja jednostajna')
plt.plot(xx, yy_least_squares, label='Aproksymacja sredniokwadratowa')
plt.plot(x, y, 'o')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.title('Porownanie aproksymacji')
plt.show()
