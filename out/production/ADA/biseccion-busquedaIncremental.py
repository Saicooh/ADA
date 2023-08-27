import math

def f(x):
    return x**10 + 2*x**9 - 3*x**8 + 4*x**7 - 5*x**6 + 6*x**5 - 7*x**4 + 8*x**3 - 9*x**2 + 10*x + 11

def search_intervals(a, b, paso):
    intervalos = []
    x = a
    while x <= b:
        funcion = f(x)
        funcionMasPaso = f(x + paso)
        if funcion * funcionMasPaso < 0:
            intervalos.append((x, x + paso))
        x += paso
    return intervalos

def bisection_method(intervalo, tolerance):
    a, b = intervalo
    while b - a >= tolerance:
        c = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fc = f(c)
        if fc == 0:
            return aproximarCero(c)
        if fa * fc < 0:
            b = c
        else:
            a = c
    return aproximarCero((a + b) / 2)

def find_roots(a, b, h, tolerance):
    intervals = search_intervals(a, b, h)
    roots = []
    for interval in intervals:
        root = bisection_method(interval, tolerance)
        roots.append(root)
    return roots

def aproximarCero(valor, tolerancia=1e-10):
    if abs(valor) < tolerancia:
        return 0
    return valor

# Parámetros iniciales
a = -5 # Límite inferior del rango
b = 5   # Límite superior del rango
h = 0.1 # Tamaño del paso en la búsqueda incremental
tolerancia = 1e-15 # Tolerancia para el método de bisección

roots = find_roots(a, b, h, tolerancia)
print("Raíces encontradas:", roots)
