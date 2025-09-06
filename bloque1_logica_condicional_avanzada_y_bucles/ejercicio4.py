"""
Ejercicio 4: Juego de Piedra, Papel o Tijeras

El programa implementa el clásico juego, encapsulando la validación de la
entrada del jugador en una función dedicada para mejorar la robustez y
facilitar las pruebas.
"""

import random


def validar_eleccion(eleccion_raw: str) -> str:
    """
    Valida la elección del jugador. Si es válida, la devuelve normalizada.
    Si no, lanza un error ValueError.

    Args:
        eleccion_raw (str): La entrada del jugador.
    Returns:
        str: La elección validada y en minúsculas ('piedra', 'papel' o 'tijeras').
    Raises:
        ValueError: Si la elección no es una de las opciones válidas.
    """
    eleccion_normalizada = eleccion_raw.lower().strip()
    opciones = ['piedra', 'papel', 'tijeras']

    if eleccion_normalizada not in opciones:
        raise ValueError("opción no válida. Elige 'piedra', 'papel' o 'tijeras'")

    return eleccion_normalizada


def determinar_ganador(eleccion_jugador: str, eleccion_computadora: str) -> str:
    """
    Determina el ganador de una ronda. Asume que las entradas ya son válidas.

    Args:
        eleccion_jugador (str): La elección del jugador.
        eleccion_computadora (str): La elección de la computadora.
    Returns:
        str: 'jugador', 'computadora' o 'empate'.
    """
    if eleccion_jugador == eleccion_computadora:
        return 'empate'

    victorias_jugador = (
            (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijeras') or
            (eleccion_jugador == 'tijeras' and eleccion_computadora == 'papel') or
            (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra')
    )

    return 'jugador' if victorias_jugador else 'computadora'


def principal():
    """
    Función principal que ejecuta el bucle del juego.
    """
    opciones = ['piedra', 'papel', 'tijeras']
    victorias_jugador = 0
    victorias_computadora = 0

    print("👊 JUEGO DE PIEDRA, PAPEL O TIJERAS 🖐️")
    print("¡El primero en llegar a 3 victorias gana!")

    while victorias_jugador < 3 and victorias_computadora < 3:
        print(f"\nMarcador: Jugador: {victorias_jugador} - Computadora: {victorias_computadora}")

        try:
            eleccion_usuario_raw = input("Elige (piedra, papel o tijeras): ")
            eleccion_jugador = validar_eleccion(eleccion_usuario_raw)

            eleccion_computadora = random.choice(opciones)
            print(f"La computadora eligió: {eleccion_computadora}")

            resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)

            if resultado == 'jugador':
                print("🎉 ¡Ganaste esta ronda!")
                victorias_jugador += 1
            elif resultado == 'computadora':
                print("😢 Perdiste esta ronda.")
                victorias_computadora += 1
            else:
                print("🤝 ¡Es un empate!")

        except ValueError as e:
            print(f"⚠️ Error: {e}")
            continue  # Saltamos al siguiente intento sin sumar puntos

    # Mensaje final del juego
    if victorias_jugador == 3:
        print("\n🥳 ¡Felicidades! ¡Has ganado el juego!")
    else:
        print("\n😔 La computadora ha ganado el juego. ¡Mejor suerte la próxima vez!")


if __name__ == "__main__":
    principal()