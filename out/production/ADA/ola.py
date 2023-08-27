from collections import deque
from matplotlib.ticker import ScalarFormatter
import time
import matplotlib.pyplot as plt
import random

class Laberinto:
  def __init__(self, laberinto, coordenadaEntrada, coordenadaSalida):
    self.laberinto = laberinto
    self.entrada = coordenadaEntrada
    self.salida = coordenadaSalida
##

def generarLaberinto(filas, columnas):
  laberinto = [[0 for _ in range(columnas)] for _ in range(filas)]
  probabilidadInsercionPared = 0.2

  for fila in range(filas):
    for columna in range(columnas):
      if random.random() < probabilidadInsercionPared:
        laberinto[fila][columna] = 1

  return laberinto
##

def movimientoValido(laberinto, visitado, fila, columna):
    filas, columnas = len(laberinto), len(laberinto[0])
    return 0 <= fila < filas and 0 <= columna < columnas and laberinto[fila][columna] == 0 and not visitado[fila][columna]

##
def encontrarCaminoMasRapido(laberinto, filaInicial, columnaInicial, filaFinal, columnaFinal):
  filas, columnas = len(laberinto), len(laberinto[0])
  visitado = [[False for _ in range(columnas)] for _ in range(filas)]
  cola = deque([(filaInicial, columnaInicial, 0)])

  while cola:
    filaActual, columnaActual, distancia = cola.popleft()
    visitado[filaActual][columnaActual] = True

    if filaActual == filaFinal and columnaActual == columnaFinal:
      return distancia

    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for filaMov, columnaMov in movimientos:
      filaSig, columnaSig = filaActual + filaMov, columnaActual + columnaMov
      if movimientoValido(laberinto, visitado, filaSig, columnaSig):
        cola.append((filaSig, columnaSig, distancia + 1))

  return -1  # Se retorna -1 si es que no se consigue encontrar un camino válido para el laberinto.

##

def evaluarDesempeno(tamanosMatrices):
  listaTiempos = []
  listaLaberintosInfo = []

  for tamano in tamanosMatrices:
    sizeFilas, sizeColumnas = tamano, tamano

    laberinto = generarLaberinto(sizeFilas, sizeColumnas)

    entradaFila, entradaColumna = 0, 0  # Entrada en la esquina superior izquierda
    salidaFila, salidaColumna = sizeFilas - 1, sizeColumnas - 1  # Salida en la esquina inferior derecha

    if laberinto[entradaFila][entradaColumna] == 1:  # Si hay una pared en la entrada
        entradaColumna = 1  # Mover la entrada a la siguiente columna si hay una pared en (0, 0)

    salidaFila, salidaColumna = sizeFilas - 1, sizeColumnas - 1  # Salida en la esquina inferior derecha
    if laberinto[salidaFila][salidaColumna] == 1:  # Si hay una pared en la salida
        salidaColumna = sizeColumnas - 2  # Mover la salida a la columna anterior si hay una pared en (n-1, m-1)

    laberintoInfo = Laberinto(laberinto, (entradaFila, entradaColumna), (salidaFila, salidaColumna))
    listaLaberintosInfo.append(laberintoInfo)

    tiempoInicial = time.time()
    distanciaMinima = encontrarCaminoMasRapido(laberinto, entradaFila, entradaColumna, salidaFila, salidaColumna)
    tiempoFinal = time.time()

    tiempoEjecucion = (tiempoFinal - tiempoInicial) * 1000

    listaTiempos.append(tiempoEjecucion)

  plt.plot(tamanosMatrices, listaTiempos, marker='o')
  plt.xlabel('Tamaño de Matriz (N x N)')
  plt.ylabel('Tiempo de Ejecución (milisegundos)')
  plt.title('Desempeño del Algoritmo BFS')
  plt.yscale('log')

  formatter = ScalarFormatter()
  formatter.set_scientific(False)
  plt.gca().yaxis.set_major_formatter(formatter)
  plt.show()

  for i, laberinto_info in enumerate(listaLaberintosInfo):
    print(f"Laberinto {i + 1}:")
    print(f"Dimensiones: {len(laberinto_info.laberinto)} x {len(laberinto_info.laberinto[0])}")
    print("Laberinto:")

    for fila in laberinto_info.laberinto:
      print(fila)

    print(f"Coordenadas de entrada: Fila {laberinto_info.entrada[0] + 1}, Columna {laberinto_info.entrada[1] + 1} ")
    print(f"Coordenadas de salida: Fila {laberinto_info.salida[0] + 1}, Columna {laberinto_info.salida[1] + 1}")

    distanciaMinima = encontrarCaminoMasRapido(laberinto_info.laberinto, laberinto_info.entrada[0], laberinto_info.entrada[1], laberinto_info.salida[0], laberinto_info.salida[1])
    if distanciaMinima != -1:
      print(f"Distancia mínima: {distanciaMinima}")
    else:
      print("No hay un camino válido desde la entrada hasta la salida.")

    print("=" * 50)

  return listaLaberintosInfo
##

tamanosMatrices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
laberintos_info_generados = evaluarDesempeno(tamanosMatrices)