"""
Ejercicio 10: Transposición de una Matriz

Este programa crea una función que recibe una matriz (lista de listas)
y devuelve su transpuesta, con validaciones robustas y lógicas separadas.
El usuario puede ingresar la matriz desde la consola.
"""
from typing import List

# Tipo de dato para una matriz (lista de listas de enteros)
Matriz = List[List[int]]


def validar_matriz(matriz: Matriz) -> None:
    """
    Valida si la entrada es una matriz válida (lista de listas no vacía
    con todas las filas de la misma longitud).

    Args:
        matriz (Matriz): La matriz a validar.

    Raises:
        ValueError: Si la matriz está vacía, o si sus filas tienen
                    longitudes diferentes.
        TypeError: Si la entrada no es una lista de listas.
    """
    if not isinstance(matriz, list):
        raise TypeError("La entrada debe ser una lista.")

    if not matriz or not all(isinstance(fila, list) for fila in matriz):
        raise ValueError("La matriz no puede estar vacía y debe contener listas.")

    # Comprobar que todas las filas tienen la misma longitud
    longitud_fila_base = len(matriz[0])
    if not all(len(fila) == longitud_fila_base for fila in matriz):
        raise ValueError("Todas las filas de la matriz deben tener la misma longitud.")


def transponer_con_bucles(matriz: Matriz) -> Matriz:
    """
    Transpone una matriz (lista de listas) utilizando bucles for anidados.
    Esta función asume que la matriz de entrada ya ha sido validada.
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    matriz_transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz[i][j]

    return matriz_transpuesta


def transponer_con_comprension(matriz: Matriz) -> Matriz:
    """
    Transpone una matriz (lista de listas) utilizando una comprensión de
    lista anidada.
    Esta función asume que la matriz de entrada ya ha sido validada.
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]


def obtener_matriz_del_usuario() -> Matriz:
    """
    Función que solicita al usuario los datos para crear una matriz.

    Returns:
        Matriz: La matriz creada a partir de la entrada del usuario.

    Raises:
        ValueError: Si el usuario ingresa un valor no numérico.
    """
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            if filas <= 0 or columnas <= 0:
                print("❌ Error: Las dimensiones deben ser números positivos.")
                continue
            break
        except ValueError:
            print("❌ Error: Por favor, ingrese números enteros válidos.")

    matriz = []
    for i in range(filas):
        while True:
            try:
                fila_str = input(f"Ingrese los {columnas} elementos de la fila {i + 1} separados por espacios: ")
                elementos = [int(x) for x in fila_str.split()]
                if len(elementos) != columnas:
                    print(f"❌ Error: Debe ingresar exactamente {columnas} elementos.")
                    continue
                matriz.append(elementos)
                break
            except ValueError:
                print("❌ Error: Los elementos de la fila deben ser números enteros.")
    return matriz


def main():
    """
    Función principal que demuestra la transposición de una matriz,
    gestionando la validación y la interacción con el usuario.
    """
    print("🔄 Transposición de una Matriz 🔄")

    try:
        matriz_original = obtener_matriz_del_usuario()
        validar_matriz(matriz_original)

        print(f"\nMatriz original: {matriz_original}")

        matriz_transpuesta_bucles = transponer_con_bucles(matriz_original)
        print("\n✅ Transpuesta (con bucles):")
        print(matriz_transpuesta_bucles)

        matriz_transpuesta_comprension = transponer_con_comprension(matriz_original)
        print("\n✅ Transpuesta (con compresión):")
        print(matriz_transpuesta_comprension)

    except (ValueError, TypeError) as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()