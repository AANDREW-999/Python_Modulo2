"""
Ejercicio 15: Proyecto Final - Batalla Naval Simplificada...

Este programa simula un juego de Batalla Naval en una cuadrícula de 5x5,
con funciones separadas para la validación y la lógica principal.
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


# --- Lógica del tablero y juego ---

def inicializar_tablero() -> List[List[str]]:
    """Crea un tablero de juego de 5x5 lleno de espacios vacíos."""
    return [[SIMBOLO_VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]


def colocar_barco() -> List[Tuple[int, int]]:
    """
    Coloca un barco de 3 casillas en una fila o columna aleatoria.

    Esta función se basa en el módulo 'random' para la aleatoriedad.
    """
    barco = []
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
    """Imprime el tablero de juego para el usuario."""
    print("\n   " + " ".join([str(i + 1) for i in range(COLUMNAS)]))
    print("  " + "---" * COLUMNAS)
    for i in range(FILAS):
        fila_str = " ".join(tablero[i])
        print(f"{string.ascii_uppercase[i]} |{fila_str}|")
    print("-" * 20)


# --- Funciones de validación ---

def validar_coordenada_usuario(coordenada_str: str, tablero: List[List[str]]) -> Tuple[int, int]:
    """
    Valida y convierte la coordenada ingresada por el usuario.

    Args:
        coordenada_str (str): La coordenada ingresada por el usuario (ej. "A1").
        tablero (List[List[str]]): El estado actual del tablero.

    Returns:
        Tuple[int, int]: La tupla de índices (fila, columna) si es válida.

    Raises:
        ValueError: Si la coordenada es inválida o ya ha sido disparada.
    """
    coordenada = coordenada_str.strip().upper()

    if len(coordenada) != 2:
        raise ValueError("Coordenada inválida. Debe tener el formato 'LetraNúmero', ej. A1.")

    fila_char = coordenada[0]
    columna_char = coordenada[1]

    if fila_char not in string.ascii_uppercase[:FILAS]:
        raise ValueError(
            f"La fila '{fila_char}' está fuera de rango. Use una letra de A a {string.ascii_uppercase[FILAS - 1]}.")

    if not columna_char.isdigit():
        raise ValueError("La columna debe ser un número.")

    columna_num = int(columna_char)
    if not (1 <= columna_num <= COLUMNAS):
        raise ValueError(f"La columna '{columna_num}' está fuera de rango. Use un número de 1 a {COLUMNAS}.")

    fila = ord(fila_char) - ord('A')
    columna = columna_num - 1

    if tablero[fila][columna] != SIMBOLO_VACIO:
        raise ValueError("Ya disparaste en esa posición. Elige una nueva.")

    return (fila, columna)


# --- Función principal del juego ---

def main():
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

        try:
            coordenada_usuario = input("Ingresa una coordenada (ej. A1): ")
            fila, columna = validar_coordenada_usuario(coordenada_usuario, tablero)
        except ValueError as e:
            print(f"❌ Error: {e}. Pierdes un turno.")
            continue

        if (fila, columna) in barco_ubicacion:
            print("🔥 ¡Tocado! Has impactado una parte del barco.")
            tablero[fila][columna] = SIMBOLO_TOCADO
            casillas_acertadas += 1
        else:
            print("💧 ¡Agua! El disparo cayó al mar.")
            tablero[fila][columna] = SIMBOLO_AGUA

        if casillas_acertadas == LONGITUD_BARCO:
            print("\n🎉 ¡Felicidades! Has hundido el barco.")
            print("¡Ganaste el juego!")
            imprimir_tablero(tablero)
            break

    if casillas_acertadas < LONGITUD_BARCO:
        print("\n💀 ¡Oh no! Te quedaste sin turnos. El barco no ha sido hundido.")
        print("¡Perdiste el juego!")
        print("La ubicación del barco era:")
        for fila, columna in barco_ubicacion:
            tablero[fila][columna] = SIMBOLO_TOCADO
        imprimir_tablero(tablero)


if __name__ == "__main__":
    main()