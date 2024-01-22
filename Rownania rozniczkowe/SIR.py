import numpy as np
import matplotlib.pyplot as plt


def f(t, y, beta, N, gamma):
    S, I, R = y
    y0 = beta / N * S * I
    y1 = beta / N * S * I - gamma * I
    y2 = gamma * I
    return y0, y1, y2


def euler2(t, f, S0, I0, R0):
    n = len(t)
    S = np.zeros(n)
    I = np.zeros(n)
    R = np.zeros(n)
    h = t[1] - t[0]
    S[0] = S0
    I[0] = I0
    R[0] = R0
    for i in range(n - 1):
        S_, I_, R_ = f(t[i], (S[i], I[i], R[i]), 0.35, 4e6, 0.035)
        S[i + 1] = S[i] + h * S_
        I[i + 1] = I[i] + h * I_
        R[i + 1] = R[i] + h * R_
    return S, I, R


a = 0.0
b = 10.0
N = 20000 // 1  # test 1, 10, 100
t = np.linspace(a, b, N + 1)
S = 2000  # Initial condition
I = 600
R = 400
y1 = euler2(t, f, S, I, R)

# Plot the results
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(t, y1, label="Położenie - jawna")
axes.set_xlabel("t")
axes.set_ylabel("y")
axes.legend(loc=2)
plt.show()
