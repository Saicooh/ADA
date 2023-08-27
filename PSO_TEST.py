import numpy as np
import matplotlib.pyplot as plt

def funcionObjetivo(x):
    return x**2 -12*x + 35

valorMinimoConocido = 6

# Algoritmo PSO
def optimizacionEnjambreParticulas(numParticulas, numIteraciones):
    particulas = np.random.uniform(-100, 100, size=numParticulas)
    velocidades = np.random.uniform(-1, 1, size=numParticulas)

    # Mejor posición personal y global para cada partícula
    mejoresPosicionesPersonales = particulas.copy()
    mejorPosicionGlobal = particulas[np.argmin(funcionObjetivo(particulas))]

    # Listas para almacenar la evolución de las partículas en cada iteración
    evolucion_particulas = [particulas.copy()]
    
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
        evolucion_particulas.append(particulas.copy())

    return evolucion_particulas, mejorPosicionGlobal

# Parámetros de entrada
numParticulas = 5000
numIteraciones = 40

# Ejecución del algoritmo PSO y seguimiento de la evolución de las partículas
evolucion_particulas, mejorPosicionGlobal = optimizacionEnjambreParticulas(numParticulas, numIteraciones)

# Graficar la evolución de las partículas en cada iteración
plt.figure(figsize=(10, 6))
for i, particulas_iteracion in enumerate(evolucion_particulas):
    plt.scatter(particulas_iteracion, [i] * numParticulas, alpha = 0.5, label=f'Iteración {i}')
plt.xlabel('Valor de la partícula')
plt.ylabel('Iteración')
plt.title('Evolución de las partículas en cada iteración')
plt.legend()
plt.axvline(x=6, color='red', linestyle='--', label="Mínimo en x=6")
plt.text(6, -2.5, "x = 6", fontsize=12, color='black', ha='center', va='center')
plt.show()