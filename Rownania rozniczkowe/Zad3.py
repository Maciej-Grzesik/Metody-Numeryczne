import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametry oscylatora
omega_0 = 1.0  # Częstość kołowa nietłumiona
t = np.linspace(0, 10, 1000)

# Funkcja opisująca układ równań różniczkowych dla oscylatora tłumionego
def damped_oscillator(y, t, beta, omega_0):
    x, v = y
    dxdt = v
    dvdt = -2 * beta * v - omega_0**2 * x
    return [dxdt, dvdt]

# Rozwiązanie dla różnych przypadków tłumienia
betas = [0.2, 1.0, 2.0]  # Różne wartości współczynnika tłumienia

plt.figure(figsize=(12, 8))

for beta in betas:
    # Warunki początkowe
    initial_conditions = [1.0, 0.0]

    # Rozwiązanie równania różniczkowego przy użyciu odeint
    solution = odeint(damped_oscillator, initial_conditions, t, args=(beta, omega_0))

    # Wykres wyników
    plt.plot(t, solution[:, 0], label=f'Beta = {beta}')

plt.title('Rozwiązania tłumionego oscylatora harmonicznego')
plt.xlabel('Czas')
plt.ylabel('Położenie')
plt.legend()
plt.show()
