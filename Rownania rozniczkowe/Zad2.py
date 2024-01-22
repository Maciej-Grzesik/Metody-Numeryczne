import numpy as np
import matplotlib.pyplot as plt

# Parametry modelu SIR
beta = 0.35  # Współczynnik zaraźliwości
gamma = 0.035  # Współczynnik zdrowienia
N = 4.0e6  # Całkowita populacja

# Warunki początkowe
S0 = N - 100  # Ilość podatnych
I0 = 100  # Ilość zarażonych
R0 = 0  # Ilość ozdrowiałych

# Krok czasowy
h = 0.1

# Funkcja opisująca układ równań różniczkowych SIR
def sir_model(S, I, R, beta, gamma, N):
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS, dI, dR

# Metoda Eulera do rozwiązania układu równań różniczkowych
def euler_method(S0, I0, R0, beta, gamma, N, h, num_steps):
    S, I, R = S0, I0, R0
    S_values, I_values, R_values = [S], [I], [R]

    for _ in range(num_steps):
        dS, dI, dR = sir_model(S, I, R, beta, gamma, N)
        S += h * dS
        I += h * dI
        R += h * dR
        S_values.append(S)
        I_values.append(I)
        R_values.append(R)

    return S_values, I_values, R_values

# Symulacja przy użyciu metody Eulera
num_steps = 500
S_values, I_values, R_values = euler_method(S0, I0, R0, beta, gamma, N, h, num_steps)

# Wykres wyników
t_values = np.arange(0, (num_steps + 1) * h, h)
plt.plot(t_values, S_values, label='Podatni (S)')
plt.plot(t_values, I_values, label='Zarażeni (I)')
plt.plot(t_values, R_values, label='Ozdrowiali (R)')
plt.xlabel('Czas')
plt.ylabel('Liczba osobników')
plt.legend()
plt.show()
