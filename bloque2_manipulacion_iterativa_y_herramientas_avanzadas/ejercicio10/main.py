
"""
Ejercicio 10: Transposición de una Matriz

Este programa crea una función que recibe una matriz (lista de listas)
y devuelve su transpuesta. El problema se resuelve de dos maneras:
1. Usando bucles for anidados tradicionales.
2. Usando una comprensión de lista anidada para una solución más concisa.
"""
from typing import List

# Tipo de dato para una matriz (lista de listas de enteros)
Matriz = List[List[int]]


def transponer_con_bucles(matriz: Matriz) -> Matriz:
    """
    Transpone una matriz (lista de listas) utilizando bucles for anidados.

    Args:
        matriz (Matriz): La matriz original a transponer.

    Returns:
        Matriz: La matriz transpuesta.
    """
    if not matriz or not matriz[0]:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])

    # Crea una nueva matriz con las dimensiones intercambiadas (columnas x filas)
    matriz_transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz[i][j]

    return matriz_transpuesta


def transponer_con_comprension(matriz: Matriz) -> Matriz:
    """
    Transpone una matriz (lista de listas) utilizando una comprensión de
    lista anidada.

    Args:
        matriz (Matriz): La matriz original a transponer.

    Returns:
        Matriz: La matriz transpuesta.
    """
    if not matriz or not matriz[0]:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])

    # La magia de la comprensión de lista anidada:
    # 1. Bucle externo: for j in range(columnas) -> Crea las filas de la nueva matriz
    # 2. Bucle interno: for i in range(filas) -> Crea los elementos de la fila
    # 3. Acceso: matriz[i][j] -> Accede a los elementos de la matriz original,
    #    intercambiando las coordenadas (i,j) por (j,i)
    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]


def main():
    """
    Función principal que demuestra la transposición de una matriz
    utilizando dos métodos diferentes.
    """
    matriz_original = [[1, 2, 3], [4, 5, 6]]

    print("🔄 Transposición de una Matriz 🔄")
    print(f"Matriz original: {matriz_original}")
    print("-" * 30)

    # Solución 1: Con bucles for anidados
    matriz_transpuesta_bucles = transponer_con_bucles(matriz_original)
    print("Solución con bucles for anidados:")
    print(f"Matriz transpuesta: {matriz_transpuesta_bucles}")
    print("-" * 30)

    # Solución 2: Con list comprehension anidada
    matriz_transpuesta_comprension = transponer_con_comprension(matriz_original)
    print("Solución con list comprehension anidada:")
    print(f"Matriz transpuesta: {matriz_transpuesta_comprension}")


if __name__ == "__main__":
    main()