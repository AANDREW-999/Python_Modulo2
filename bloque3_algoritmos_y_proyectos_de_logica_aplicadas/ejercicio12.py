"""
Ejercicio 12: Simulador de Lanzamiento de Dados

Este programa simula el lanzamiento de dos dados y reporta la frecuencia de cada suma.
La lógica está separada en funciones de validación y simulación para mayor claridad.
"""
import random
from typing import Dict

# Constante de ejemplo para la simulación
NUMERO_LANZAMIENTOS_POR_DEFECTO = 10000


def validar_numero_lanzamientos(num_lanzamientos: str) -> int:
    """
    Valida que la entrada sea un número entero y positivo.

    Args:
        num_lanzamientos (str): El número de lanzamientos como cadena de texto.

    Returns:
        int: El número de lanzamientos validado.

    Raises:
        ValueError: Si la entrada no es un número entero o si es un número negativo.
    """
    try:
        lanzamientos = int(num_lanzamientos)
    except (ValueError, TypeError):
        raise ValueError("El número de lanzamientos debe ser un número entero.")

    if lanzamientos < 0:
        raise ValueError("El número de lanzamientos no puede ser negativo.")

    return lanzamientos


def simular_lanzamientos(numero_lanzamientos: int) -> Dict[int, int]:
    """
    Simula el lanzamiento de dos dados y cuenta la frecuencia de cada suma.

    Esta función asume que el `numero_lanzamientos` ya fue validado.

    Args:
        numero_lanzamientos (int): La cantidad de veces que se simularán los lanzamientos.

    Returns:
        Dict[int, int]: Un diccionario con la suma como clave y la frecuencia como valor.
    """
    frecuencias = {i: 0 for i in range(2, 13)}  # Inicializa el diccionario con todas las sumas posibles

    for _ in range(numero_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] += 1

    return frecuencias


def main():
    """
    Función principal que solicita el número de lanzamientos al usuario,
    ejecuta la simulación y muestra el reporte de frecuencias.
    """
    print("🎲 Simulador de Lanzamiento de Dados 🎲")

    while True:
        try:
            input_lanzamientos = input(f"\nIngrese el número de lanzamientos (ej: {NUMERO_LANZAMIENTOS_POR_DEFECTO}): ")
            num_lanzamientos = validar_numero_lanzamientos(input_lanzamientos)
            break
        except ValueError as e:
            print(f"❌ Error: {e}")

    # Llama a la función que realiza la simulación
    resultados = simular_lanzamientos(num_lanzamientos)

    print(f"\n✅ Resultados de la simulación de {num_lanzamientos} lanzamientos:")

    # Itera sobre los resultados y muestra el reporte
    for suma in sorted(resultados.keys()):
        frecuencia = resultados[suma]
        print(f"La suma {suma} apareció {frecuencia} veces.")


if __name__ == "__main__":
    main()