import math

def f(x):
    return x**5 + 2*x**4 - 7*x**3 + 3*x**2 - 5*x + 2

def f_prime(x):
    return 5*x**4 + 8*x**3 - 21*x**2 + 6*x - 5

def newton_raphson(func, func_prime, x0, tol, max_iterations):
    x = x0
    for i in range(max_iterations):
        fx = func(x)
        fpx = func_prime(x)
        x_next = x - fx / fpx
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return None  # No se alcanzó la convergencia en max_iterations

# Valores iniciales y parámetros
x_initial = 1.0
tolerance = 1e-6
max_iterations = 10

approx_root = newton_raphson(f, f_prime, x_initial, tolerance, max_iterations)
print("Aproximación de la raíz:", approx_root)
