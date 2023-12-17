import math


def function1(x):
    return x ** (1/3) + 2

def function2(x):
    return (x - 2) ** 2

def function3(x):
    return 1 / math.sqrt(1+x)


class FixedPointMethod:
    def __init__(self, g_function):
        self.g_function = g_function

    def fixedPointIteration(self, initial_guess, max_iterations=100, tollerance=1e-5):
        for i in range(max_iterations):
            x_new = self.g_function(initial_guess)
            if abs(x_new - initial_guess) < tollerance:
                return x_new, i + 1
            initial_guess = x_new
        return x_new, max_iterations
    def setFunction(self, new_g_function):
        self.g_function = new_g_function


Function1_object = FixedPointMethod(function1)
Function2_object = FixedPointMethod(function2)
Function3_object = FixedPointMethod(function3)
print(Function1_object.fixedPointIteration(3.0))
print(Function2_object.fixedPointIteration(3.0))
print(Function3_object.fixedPointIteration(2))