"""
Ejercicio 8: Filtrado de Datos con List Comprehensions

Este programa utiliza comprensiones de lista para generar nuevas listas
a partir de una lista de números dada, filtrando, transformando y
clasificando sus elementos de forma concisa y "Pythónica".
"""
from typing import List

def procesar_numeros(lista_numeros: List[int]) -> tuple[List[int], List[int], List[str]]:
    """
    Procesa una lista de números para generar tres listas nuevas usando
    comprensiones de lista.

    Args:
        lista_numeros (List[int]): Una lista de números enteros.

    Returns:
        tuple[List[int], List[int], List[str]]: Una tupla que contiene:
            - Una lista con solo los números positivos.
            - Una lista con los cuadrados de todos los números.
            - Una lista de strings que indica si cada número es "positivo" o "negativo".
    """
    # 1. Lista con solo los números positivos
    numeros_positivos = [num for num in lista_numeros if num > 0]

    # 2. Lista con los cuadrados de todos los números
    cuadrados = [num ** 2 for num in lista_numeros]

    # 3. Lista de strings 'positivo' o 'negativo' usando un ternario
    clasificacion_signo = ["positivo" if num >= 0 else "negativo" for num in lista_numeros]

    return (numeros_positivos, cuadrados, clasificacion_signo)


def main():
    """
    Función principal que ejecuta el procesamiento de la lista de números
    y muestra los resultados.
    """
    numeros = [-5, 10, -15, 20, -25, 30]

    print("📊 Procesador de Datos con List Comprehensions 📊")
    print(f"Lista de números original: {numeros}")

    # Llama a la función de procesamiento
    numeros_positivos, cuadrados, clasificacion_signo = procesar_numeros(numeros)

    # Imprime los resultados de forma descriptiva
    print(f"\n✅ Números positivos: {numeros_positivos}")
    print(f"✅ Cuadrados de los números: {cuadrados}")
    print(f"✅ Clasificación de signo: {clasificacion_signo}")

if __name__ == "__main__":
    main()
