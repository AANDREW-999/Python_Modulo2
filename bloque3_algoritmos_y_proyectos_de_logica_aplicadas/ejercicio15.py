"""
Ejercicio 15: Proyecto Final - Batalla Naval Simplificada

Este programa simula un juego de Batalla Naval en una cuadrícula de 5x5.
El objetivo es que el jugador adivine la ubicación de un barco escondido
en una fila o columna.
"""
import random
import string
from typing import List, Tuple

# Constantes del juego
FILAS = 5
COLUMNAS = 5
LONGITUD_BARCO = 3
NUMERO_TURNOS = 10
SIMBOLO_AGUA = "💧"
SIMBOLO_TOCADO = "🔥"
SIMBOLO_VACIO = "⬜"


def inicializar_tablero() -> List[List[str]]:
    """
    Crea un tablero de juego de 5x5 lleno de espacios vacíos.

    Returns:
        List[List[str]]: El tablero de juego como una lista de listas.
    """
    return [[SIMBOLO_VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]


def colocar_barco() -> List[Tuple[int, int]]:
    """
    Coloca un barco de 3 casillas en una fila o columna aleatoria.

    Returns:
        List[Tuple[int, int]]: Una lista de tuplas con las coordenadas del barco.
    """
    barco = []
    # Decide aleatoriamente si el barco será horizontal (0) o vertical (1)
    orientacion = random.randint(0, 1)

    if orientacion == 0:  # Horizontal
        fila = random.randint(0, FILAS - 1)
        columna_inicial = random.randint(0, COLUMNAS - LONGITUD_BARCO)
        for i in range(LONGITUD_BARCO):
            barco.append((fila, columna_inicial + i))
    else:  # Vertical
        columna = random.randint(0, COLUMNAS - 1)
        fila_inicial = random.randint(0, FILAS - LONGITUD_BARCO)
        for i in range(LONGITUD_BARCO):
            barco.append((fila_inicial + i, columna))

    return barco


def imprimir_tablero(tablero: List[List[str]]) -> None:
    """
    Imprime el tablero de juego para el usuario.

    Args:
        tablero (List[List[str]]): El tablero de juego.
    """
    print("\n   " + " ".join([str(i + 1) for i in range(COLUMNAS)]))
    print("  " + "---" * COLUMNAS)
    for i in range(FILAS):
        fila_str = " ".join(tablero[i])
        print(f"{string.ascii_uppercase[i]} |{fila_str}|")
    print("-" * 20)


def convertir_coordenadas(coordenada: str) -> Tuple[int, int] | None:
    """
    Convierte una coordenada de string (ej. "A3") a una tupla de índices (0, 2).

    Args:
        coordenada (str): La coordenada ingresada por el usuario.

    Returns:
        Tuple[int, int] | None: La tupla de índices (fila, columna) o None si es inválida.
    """
    if len(coordenada) != 2:
        return None

    fila_char = coordenada[0].upper()
    columna_str = coordenada[1]

    if fila_char not in string.ascii_uppercase[:FILAS] or not columna_str.isdigit():
        return None

    fila = ord(fila_char) - ord('A')
    columna = int(columna_str) - 1

    if not (0 <= fila < FILAS and 0 <= columna < COLUMNAS):
        return None

    return (fila, columna)


def principal():
    """
    Función principal que ejecuta el juego de Batalla Naval.
    """
    print("⚓️ ¡Bienvenido a Batalla Naval! ⚓️")
    print(f"El juego se juega en una cuadrícula de {FILAS}x{COLUMNAS}.")
    print(f"Tienes {NUMERO_TURNOS} turnos para encontrar y hundir un barco de {LONGITUD_BARCO} casillas.")

    tablero = inicializar_tablero()
    barco_ubicacion = colocar_barco()
    casillas_acertadas = 0

    for turno in range(1, NUMERO_TURNOS + 1):
        imprimir_tablero(tablero)
        print(f"--- Turno {turno} de {NUMERO_TURNOS} ---")

        while True:
            coordenada_usuario = input("Ingresa una coordenada (ej. A1): ").upper()
            coordenada_tuple = convertir_coordenadas(coordenada_usuario)

            if coordenada_tuple:
                fila, columna = coordenada_tuple
                if tablero[fila][columna] != SIMBOLO_VACIO:
                    print("❌ Ya disparaste en esa posición. Elige una nueva.")
                else:
                    break
            else:
                print("❌ Coordenada inválida. Intente de nuevo.")

        # Verificar si el disparo impactó al barco
        if coordenada_tuple in barco_ubicacion:
            print("🔥 ¡Tocado! Has impactado una parte del barco.")
            tablero[fila][columna] = SIMBOLO_TOCADO
            casillas_acertadas += 1
        else:
            print("💧 ¡Agua! El disparo cayó al mar.")
            tablero[fila][columna] = SIMBOLO_AGUA

        # Verificar si el barco ha sido hundido
        if casillas_acertadas == LONGITUD_BARCO:
            print("\n🎉 ¡Felicidades! Has hundido el barco.")
            print("¡Ganaste el juego!")
            imprimir_tablero(tablero)
            break

    # Mensaje de fin de juego si no se hundió el barco
    if casillas_acertadas < LONGITUD_BARCO:
        print("\n💀 ¡Oh no! Te quedaste sin turnos. El barco no ha sido hundido.")
        print("¡Perdiste el juego!")
        print("La ubicación del barco era:")
        for fila, columna in barco_ubicacion:
            tablero[fila][columna] = SIMBOLO_TOCADO
        imprimir_tablero(tablero)


if __name__ == "__main__":
    principal()