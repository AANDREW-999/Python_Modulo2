"""
Ejercicio 12: Simulador de Lanzamiento de Dados

Este programa simula el lanzamiento de dos dados 10,000 veces para
determinar la frecuencia de cada posible suma (de 2 a 12).
"""
import random
from typing import Dict


def simular_lanzamientos(numero_lanzamientos: int) -> Dict[int, int]:
    """
    Simula el lanzamiento de dos dados y cuenta la frecuencia de cada suma.

    Args:
        numero_lanzamientos (int): La cantidad de veces que se simularán los lanzamientos.

    Returns:
        Dict[int, int]: Un diccionario con la suma como clave y la frecuencia como valor.
    """
    frecuencias = {}
    for _ in range(numero_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        # Usar el método get() para contar la frecuencia
        # get(key, default_value) devuelve el valor de la clave, o el valor por defecto si no existe.
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    return frecuencias


def principal():
    """
    Función principal que ejecuta la simulación de dados y muestra el reporte de
    frecuencias.
    """
    print("🎲 Simulador de Lanzamiento de Dados 🎲")

    NUMERO_LANZAMIENTOS = 10000

    # Llama a la función que realiza la simulación
    resultados = simular_lanzamientos(NUMERO_LANZAMIENTOS)

    print(f"\n✅ Resultados de la simulación de {NUMERO_LANZAMIENTOS} lanzamientos:")

    # Ordenar las claves del diccionario para una presentación más clara
    sumas_ordenadas = sorted(resultados.keys())

    # Itera sobre los resultados y muestra el reporte
    for suma in sumas_ordenadas:
        frecuencia = resultados[suma]
        print(f"La suma {suma} apareció {frecuencia} veces.")


if __name__ == "__main__":
    principal()