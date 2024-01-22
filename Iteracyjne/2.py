import numpy as np
import scipy.optimize as scop
import matplotlib.pyplot as plt

class UniformApproximation:
    def __init__(self, x_points, y_points):
        self.x_points = np.array(x_points)
        self.y_points = np.array(y_points)

    def J(self, params):
        a, b = params
        return np.max(np.abs(a * self.x_points + b - self.y_points))

    def find_coefficients(self):
        initial_guess = [0, 0]
        result = scop.fmin_bfgs(self.J, initial_guess, disp=False)
        return result[0], result[1]

    def plot_approximation(self, a, b):
        plt.scatter(self.x_points, self.y_points, label='Original Points')
        x_range = np.linspace(np.min(self.x_points), np.max(self.x_points), 100)
        y_approx = a * x_range + b
        plt.plot(x_range, y_approx, color='red', label='Uniform Approximation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

# Przykładowe użycie
x_points = np.array([1, 2, 3, 4, 5])
y_points = np.array([2, 4, 1, 6, 5])

uniform_approximation = UniformApproximation(x_points, y_points)
a, b = uniform_approximation.find_coefficients()
print(f'Współczynniki funkcji liniowej: a = {a}, b = {b}')

uniform_approximation.plot_approximation(a, b)
