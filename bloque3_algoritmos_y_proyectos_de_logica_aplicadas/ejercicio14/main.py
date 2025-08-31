"""
Ejercicio 14: Juego del Ahorcado (Hangman)

Este programa implementa una versión en consola del clásico juego del "Ahorcado".
El jugador tiene un número limitado de intentos para adivinar una palabra secreta,
letra por letra.
"""

import random
from typing import Set, List

# Lista de palabras secretas para el juego
PALABRAS_SECRETAS = ["python", "programacion", "computador", "algoritmo", "desarrollo"]
NUMERO_INTENTOS_MAXIMO = 6


def seleccionar_palabra() -> str:
    """
    Selecciona una palabra aleatoria de la lista predefinida.

    Returns:
        str: La palabra secreta para la partida.
    """
    return random.choice(PALABRAS_SECRETAS)


def mostrar_tablero(palabra_secreta: str, letras_adivinadas: Set[str], vidas: int) -> None:
    """
    Muestra el estado actual del juego al jugador.

    Args:
        palabra_secreta (str): La palabra que el jugador debe adivinar.
        letras_adivinadas (Set[str]): Conjunto de letras que el jugador ha adivinado.
        vidas (int): El número de intentos restantes.
    """
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "

    print("\n" + "---" * 10)
    print(f"Palabra: {tablero}")
    print(f"Vidas restantes: {vidas} ❤️")
    print(f"Letras intentadas: {sorted(list(letras_adivinadas))}")
    print("---" * 10)


def validar_entrada(letra_intento: str, letras_adivinadas: Set[str]) -> bool:
    """
    Valida la entrada del jugador: debe ser una sola letra y no haber sido adivinada antes.

    Args:
        letra_intento (str): La letra ingresada por el usuario.
        letras_adivinadas (Set[str]): Conjunto de letras ya intentadas.

    Returns:
        bool: True si la entrada es válida, False en caso contrario.
    """
    if len(letra_intento) != 1 or not letra_intento.isalpha():
        print("❌ Por favor, ingrese una sola letra válida.")
        return False

    if letra_intento in letras_adivinadas:
        print("❌ Ya intentaste esa letra. Elige una nueva.")
        return False

    return True


def principal():
    """
    Función principal que ejecuta la lógica del juego del Ahorcado.
    """
    print(" ahorcado Bienvenido al Juego del Ahorcado 🎯")
    palabra_secreta = seleccionar_palabra()

    # Estado del juego
    letras_adivinadas = set()
    vidas = NUMERO_INTENTOS_MAXIMO

    while vidas > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas, vidas)

        # Validación de entrada del usuario
        letra_intento = input("Ingresa una letra: ").lower()

        if not validar_entrada(letra_intento, letras_adivinadas):
            continue

        letras_adivinadas.add(letra_intento)

        # Lógica de juego: ¿acertó o falló?
        if letra_intento in palabra_secreta:
            print(f"🎉 ¡Bien hecho! La letra '{letra_intento}' está en la palabra.")
        else:
            print(f"😢 Lo siento, la letra '{letra_intento}' no está en la palabra.")
            vidas -= 1

        # Verificar si el jugador ha ganado
        palabra_revelada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_revelada += letra

        if palabra_revelada == palabra_secreta:
            print(f"\n🥳 ¡Felicidades! Adivinaste la palabra: '{palabra_secreta}'. ¡Ganaste!")
            break

    # Mensaje final del juego
    if vidas == 0:
        print("\n💀 ¡Oh no! Te has quedado sin vidas. Perdiste el juego.")
        print(f"La palabra secreta era: '{palabra_secreta}'")

    print("\n--- Fin del juego ---")


if __name__ == "__main__":
    principal()