"""
Ejercicio 8: Filtrado de Datos con List Comprehensions

Este programa interactivo pide al usuario una lista de números, la valida
y utiliza comprensiones de lista para generar y mostrar nuevos datos derivados.
"""
from typing import List


def analizar_lista_desde_texto(entrada_raw: str) -> tuple:
    """
    Convierte y valida una cadena de texto en una lista de números, y luego
    la procesa usando comprensiones de lista.

    Args:
        entrada_raw (str): Cadena con números separados por comas.
    Returns:
        tuple: (lista_original, positivos, cuadrados, clasificacion_signo)
    Raises:
        ValueError: Si la entrada está vacía o contiene elementos no válidos.
    """
    # Límite máximo de números permitidos en la lista
    limite_elementos = 100

    # 1. Validación y Conversión de la Entrada
    if not entrada_raw.strip():
        raise ValueError("la entrada no puede estar vacía")

    elementos = entrada_raw.split(',')
    lista_numeros = []
    for elemento in elementos:
        try:
            # Quitamos espacios y convertimos a entero
            lista_numeros.append(int(elemento.strip()))
        except ValueError:
            raise ValueError(f"el elemento '{elemento.strip()}' no es un número entero válido")

    # Límite de tamaño de la lista
    if len(lista_numeros) > limite_elementos:
        raise ValueError(f"la lista excede el límite de {limite_elementos} números")

    # 2. Lógica de Procesamiento con List Comprehensions
    numeros_positivos = [num for num in lista_numeros if num > 0]
    cuadrados = [num ** 2 for num in lista_numeros]
    clasificacion_signo = ["positivo" if num >= 0 else "negativo" for num in lista_numeros]

    return lista_numeros, numeros_positivos, cuadrados, clasificacion_signo


def main():
    """
    Función principal que solicita la lista al usuario y muestra los resultados.
    """
    print("📊 Procesador de Datos con List Comprehensions 📊")

    while True:
        try:
            entrada_usuario = input("\nIngrese números separados por comas (ej: -5, 10, -15, 20, -25, 30): ")

            # La función de análisis hace la validación y el procesamiento
            original, positivos, cuadrados, clasificacion = analizar_lista_desde_texto(entrada_usuario)

            # Si es correcto, mostramos los resultados
            print(f"\nLista original procesada: {original}")
            print(f"✅ Números positivos: {positivos}")
            print(f"✅ Cuadrados de los números: {cuadrados}")
            print(f"✅ Clasificación de signo: {clasificacion}")
            break

        except ValueError as e:
            print(f"❌ Error: {e}. Intente de nuevo.")


if __name__ == "__main__":
    main()