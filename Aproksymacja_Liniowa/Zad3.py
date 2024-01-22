import numpy as np
import matplotlib.pyplot as plt

class LinearApproximation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def uniform_approximation(self):
        mean_x = np.mean(self.x)
        mean_y = np.mean(self.y)

        a = (mean_y - self.y[0]) / (mean_x - self.x[0])
        b = mean_y - a * mean_x

        return a, b

    def fit_uniform(self, xx):
        a, b = self.uniform_approximation()
        yy = a * xx + b
        return yy

    def fit_least_squares(self, xx):
        coefficients_ls = np.polyfit(self.x, self.y, 1)
        a, b = coefficients_ls
        yy = a * xx + b
        return yy

# Dane do aproksymacji
x = np.linspace(-1, 2, 10)
y = 2.0 * x + 1.0 + np.random.rand(10)

# Inicjalizacja modelu
model = LinearApproximation(x, y)

# Punkty dla wykresu
xx = np.linspace(-1, 2, 100)

# Aproksymacja jednostajna
yy_uniform = model.fit_uniform(xx)

# Aproksymacja średniokwadratowa
yy_least_squares = model.fit_least_squares(xx)

# Wykres
plt.figure(figsize=(8, 6))
plt.plot(xx, yy_uniform, label='Aproksymacja jednostajna')
plt.plot(xx, yy_least_squares, label='Aproksymacja średniokwadratowa')
plt.plot(x, y, 'o', label='Dane')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.title('Porównanie aproksymacji')
plt.show()

