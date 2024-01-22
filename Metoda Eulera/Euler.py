import numpy as np
import matplotlib.pyplot as plt


class EulerMethod:
    def __init__(self, t, f, y0):
        self.t = t
        self.f = f
        self.y0 = y0

    def classified_method(self):
        n = len(self.t)
        y = np.zeros(n)
        h = self.t[1] - self.t[0]
        y[0] = self.y0
        for i in range(n - 1):
            y[i + 1] = self.f(self.t[i], y[i]) / (1 - h)
        return y

    def unclassified_method(self):
        n = len(self.t)
        y = np.zeros(n)
        h = self.t[1] - self.t[0]
        y[0] = self.y0
        for i in range(n - 1):
            y[i + 1] = y[i] + h * self.f(self.t[i], y[i])
        return y


def func(t, y):
    return -10 * y


a = 0.0
b = 2.0
N = 100
t = np.linspace(a, b, N + 1)
print(f'h = {(b - a) / N}')
y0 = 1.0  # Initial condition
euler = EulerMethod(t, func, y0)
y2 = euler.unclassified_method()
print("   jawna = ", y2)
y1 = euler.classified_method()
print("niejawna = ", y1)

# Plot the results
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(t, y1, '-o', label="Niejawna")
axes.plot(t, y2, '-o', label="Jawna")

# axes.plot(t, np.exp(-10 * t), '-d', label="Dokładne rozwiązanie")
axes.set_xlabel("t")
axes.set_ylabel("y")
axes.legend(loc=2)
plt.show()
