import numpy as np
import matplotlib.pyplot as plt

# Funkcja reprezentująca równanie różniczkowe
def differential_equation(t, y):
    return y

# Metoda Eulera do rozwiązania równania różniczkowego
def euler_method(t_max, h):
    num_steps = int(t_max / h) + 1
    t_values = np.linspace(0, t_max, num_steps)
    y_values = np.zeros(num_steps)

    # Warunki początkowe
    t_values[0] = 0
    y_values[0] = 1

    # Iteracyjne obliczanie wartości y
    for i in range(1, num_steps):
        y_values[i] = y_values[i-1] + h * differential_equation(t_values[i-1], y_values[i-1])

    return t_values, y_values

# Parametry symulacji
t_max = 5
h = 0.1

# Wywołanie metody Eulera
t, y = euler_method(t_max, h)

# Rysowanie wykresu
plt.plot(t, y, label='Metoda Eulera')
plt.plot(t, np.exp(t), label='Dokładne rozwiązanie (e^t)', linestyle='dashed')
plt.xlabel('Czas (t)')
plt.ylabel('y(t)')
plt.legend()
plt.show()
