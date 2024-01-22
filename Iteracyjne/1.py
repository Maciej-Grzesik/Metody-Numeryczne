import numpy as np
import numpy.linalg as npl


def Gauss_Seidel(A, b, x0=None, max_it=100, tol=1e-5):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    sum1 = 0
    sum2 = 0

    for iters in range(max_it):
        x = x0.copy()

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = x0[i] + (b[i] - sum1 - sum2) / A[i, i]

            if np.max(np.abs(x - x0)) < tol:
                print('Ilość iteracji: ', iters + 1)
                return x

        x0 = x.copy()

    print("Metoda nie zbiega się w danej liczbie iteracji.")


A = np.array([[2.0, -1.0, 0.0],
              [-1.0, 3.0, -1.0],
              [0.0, -1.0, 2.0]])
b = np.array([1.0, 8.0, -5.0])

max_it = 100

print(Gauss_Seidel(A, b))


def richardson_iteration(A, b, x0=None, omega=0.1, max_it=100, tol=1e-5):
    n = len(b)

    if x0 is None:
        x0 = np.zeros(n)

    for iters in range(max_it):
        x = x0 + omega * (b - np.dot(A, x0))

        if np.max(np.abs(x - x0)) < tol:
            print('Ilość iteracji: ' + str(iters+1) + " dla omega = " + str(omega))
            return x

        x0 = x

    print("Metoda nie zbiega się w danej liczbie iteracji (" + str(max_it) + ") dla omega = ", omega)
    return x


A = np.array([[2.0, -1.0, 0.0],
              [-1.0, 3.0, -1.0],
              [0.0, -1.0, 2.0]])
b = np.array([1.0, 8.0, -5.0])

max_it = 100

x0 = np.zeros_like(b)

solution = richardson_iteration(A, b, x0, omega=0.38, max_it=max_it)
print("Rozwiązanie:", solution)


def SOR(A, b, omega=0.1, x0=None, max_it=100, tol=1e-5):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)

    for iters in range(max_it):
        x = x0.copy()

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i:], x[i:])
            x[i] = x0[i] + omega * ((b[i] - sum1 - sum2) / A[i, i])

        if np.max(np.abs(x - x0)) < tol:
            print('Ilość iteracji: ', iters + 1)
            return x

        x0 = x.copy()

    print("Metoda nie zbiega się w danej liczbie iteracji.")

A = np.array([[2.0, -1.0, 0.0],
              [-1.0, 3.0, -1.0],
              [0.0, -1.0, 2.0]])
b = np.array([1.0, 8.0, -5.0])

print(SOR(A, b, omega=1.1, max_it=1000))
