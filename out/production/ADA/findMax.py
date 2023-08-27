def contarOcurrencias(lista, num):
    count = 0
    for elemento in lista:
        if elemento == num:
            count += 1
    return count

def encontrarElementoMayoritario(lista, izquierda, derecha):
    if izquierda == derecha: return lista[izquierda]
    
    medio = (izquierda + derecha) // 2
    
    elementoMayoritarioIzquierda = encontrarElementoMayoritario(lista, izquierda, medio)
    elementoMayoritarioDerecha = encontrarElementoMayoritario(lista, medio + 1, derecha)
    
    contadorIzquierda = contarOcurrencias(lista[izquierda:derecha + 1], elementoMayoritarioIzquierda)
    contadorDerecha = contarOcurrencias(lista[izquierda:derecha + 1], elementoMayoritarioDerecha)
    
    if contadorIzquierda > (derecha - izquierda + 1) // 2: return elementoMayoritarioIzquierda
    elif contadorDerecha > (derecha - izquierda + 1) // 2: return elementoMayoritarioDerecha
    else: return None

def elementoMayoritario(lista):
    return encontrarElementoMayoritario(lista, 0, len(lista) - 1)

# Ejemplo de uso
lista = [2, 2, 3, 3, 2, 3, 2, 2, 2]
mayoritario = elementoMayoritario(lista)

if mayoritario is not None: print("El elemento mayoritario es:", mayoritario)
else: print("No hay elemento mayoritario en la lista.")
