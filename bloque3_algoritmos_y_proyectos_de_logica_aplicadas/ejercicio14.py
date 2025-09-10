"""
Ejercicio 14: Juego del Ahorcado (Hangman).

Este programa implementa una versión en consola del clásico juego del "Ahorcado".
El código está refactorizado para separar la validación de la lógica.
"""

import random
from typing import Set, List

# Lista de palabras secretas para el juego
PALABRAS_SECRETAS = ["python", "programacion", "computador", "algoritmo", "desarrollo"]
NUMERO_INTENTOS_MAXIMO = 6


# --- Lógica del juego ---

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


def verificar_victoria(palabra_secreta: str, letras_adivinadas: Set[str]) -> bool:
    """
    Verifica si el jugador ha adivinado todas las letras de la palabra secreta.
    """
    return all(letra in letras_adivinadas for letra in palabra_secreta)


# --- Validación de la entrada del usuario ---

def validar_entrada(letra_intento: str, letras_adivinadas: Set[str]) -> str:
    """
    Valida la entrada del jugador, lanzando excepciones si es inválida.

    Args:
        letra_intento (str): La letra ingresada por el usuario.
        letras_adivinadas (Set[str]): Conjunto de letras ya intentadas.

    Returns:
        str: La letra validada, en minúscula.

    Raises:
        ValueError: Si la entrada no es una sola letra o si ya ha sido intentada.
    """
    if len(letra_intento) != 1 or not letra_intento.isalpha():
        raise ValueError("Por favor, ingrese una sola letra minuscula válida.")

    letra_normalizada = letra_intento.lower()

    if letra_normalizada in letras_adivinadas:
        raise ValueError("Ya intentaste esa letra. Elige una nueva.")

    return letra_normalizada


# --- Función principal del juego ---

def main():
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

        letra_input = input("Ingresa una letra: ")

        try:
            letra_intento = validar_entrada(letra_input, letras_adivinadas)
            letras_adivinadas.add(letra_intento)

            if letra_intento in palabra_secreta:
                print(f"🎉 ¡Bien hecho! La letra '{letra_intento}' está en la palabra.")
            else:
                print(f"😢 Lo siento, la letra '{letra_intento}' no está en la palabra.")
                vidas -= 1

            if verificar_victoria(palabra_secreta, letras_adivinadas):
                print(f"\n🥳 ¡Felicidades! Adivinaste la palabra: '{palabra_secreta}'. ¡Ganaste!")
                break

        except ValueError as e:
            print(f"❌ Error: {e}")
            continue

    if vidas == 0:
        print("\n💀 ¡Oh no! Te has quedado sin vidas. Perdiste el juego.")
        print(f"La palabra secreta era: '{palabra_secreta}'")

    print("\n--- Fin del juego ---")


if __name__ == "__main__":
    main()