import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definicja równania różniczkowego dla oscylatora harmonicznego
def harmonic_oscillator(y, t, omega):
    """
    y: Wektor zmiennych stanu [x, v]
    t: Czas
    omega: Częstość kołowa (omega^2 to stała sprężystości/masa)
    """
    x, v = y
    dydt = [v, -omega**2 * x]
    return dydt

# Parametry oscylatora harmonicznego
omega = 1.0  # Częstość kołowa

# Warunki początkowe [położenie, prędkość]
initial_conditions = [1.0, 0.0]

# Czas symulacji
t = np.linspace(0, 10, 1000)

# Rozwiązanie równania różniczkowego przy użyciu odeint
solution = odeint(harmonic_oscillator, initial_conditions, t, args=(omega,))

# Wykres wyników
plt.plot(t, solution[:, 0], label='Położenie (x)')
plt.plot(t, solution[:, 1], label='Prędkość (v)')
plt.xlabel('Czas')
plt.ylabel('Wartość')
plt.legend()
plt.show()
