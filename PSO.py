import numpy as np
import math
import matplotlib.pyplot as plt

def funcionObjetivo(x):
    return 81*x**8 + 29*x**7 + 3*x**6 + 27*x**5 + 9*x**4 + 3*x**3 + 9*x**2 + 3*x + 1	

# Algoritmo PSO
def optimizacionEnjambreParticulas(numParticulas, numIteraciones):
    # Inicialización de partículas y velocidades
    particulas = np.random.uniform(-10, 10, size = numParticulas)
    velocidades = np.random.uniform(-1, 1, size = numParticulas)

    # Mejor posición personal y global para cada partícula
    mejoresPosicionesPersonales = particulas.copy()
    mejorPosicionGlobal = particulas[np.argmin(funcionObjetivo(particulas))]
    
    print("Mejor posición inicial: {:.2f}\n".format(mejorPosicionGlobal))

    for _ in range(numIteraciones):
        for i in range(numParticulas):
            # Actualización de velocidad y posición
            actualizacionCognitiva = np.random.random() * (mejoresPosicionesPersonales[i] - particulas[i])
            actualizacionSocial = np.random.random() * (mejorPosicionGlobal - particulas[i])
            velocidades[i] = 0.5 * velocidades[i] + 1.5 * actualizacionCognitiva + 1.5 * actualizacionSocial
            particulas[i] = particulas[i] + velocidades[i]

            # Actualización de la mejor posición personal y global
            if funcionObjetivo(particulas[i]) < funcionObjetivo(mejoresPosicionesPersonales[i]):
                mejoresPosicionesPersonales[i] = particulas[i]
                if funcionObjetivo(particulas[i]) < funcionObjetivo(mejorPosicionGlobal):
                    mejorPosicionGlobal = particulas[i]

    return mejorPosicionGlobal

# Parámetros de entrada
numParticulas = 10
numIteraciones = 100

# Ejecución del algoritmo PSO
mejorPosicionGlobal = optimizacionEnjambreParticulas(numParticulas, numIteraciones)

## escribe la funcion objetivo en un print

print("Mejor posición encontrada: {:.2f}\n".format(mejorPosicionGlobal))
print("Valor mínimo de la función: {:.2f}\n".format(funcionObjetivo(mejorPosicionGlobal)))
print("Coordenadas del valor mínimo de la función: ({:.2f}, {:.2f})\n".format(mejorPosicionGlobal, funcionObjetivo(mejorPosicionGlobal)))

