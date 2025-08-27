"""
Ejercicio 4: Juego de Piedra, Papel o Tijeras

Este programa implementa una versión simplificada del clásico juego. El jugador
compite contra la computadora, y el primero en llegar a 3 victorias gana la partida.
"""

import random


def determinar_ganador(eleccion_jugador: str, eleccion_computadora: str) -> str:
    """
    Determina el ganador de una ronda de Piedra, Papel o Tijeras.

    Args:
        eleccion_jugador (str): La elección del jugador ('piedra', 'papel' o 'tijeras').
        eleccion_computadora (str): La elección de la computadora.

    Returns:
        str: El resultado de la ronda: 'jugador', 'computadora' o 'empate'.
    """
    if eleccion_jugador == eleccion_computadora:
        return 'empate'
    elif (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijeras') or \
            (eleccion_jugador == 'tijeras' and eleccion_computadora == 'papel') or \
            (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra'):
        return 'jugador'
    else:
        return 'computadora'


def principal():
    """
    Función principal que ejecuta el bucle del juego de Piedra, Papel o Tijeras.
    """
    opciones = ['piedra', 'papel', 'tijeras']
    victorias_jugador = 0
    victorias_computadora = 0

    print("👊 JUEGO DE PIEDRA, PAPEL O TIJERAS 🖐️")
    print("¡El primero en llegar a 3 victorias gana!")

    while victorias_jugador < 3 and victorias_computadora < 3:
        print(f"\nMarcador: Jugador: {victorias_jugador} - Computadora: {victorias_computadora}")

        # Validar la elección del jugador
        while True:
            eleccion_jugador = input("Elige (piedra, papel o tijeras): ").lower()
            if eleccion_jugador in opciones:
                break
            else:
                print("⚠️ Error: Opción no válida. Por favor, elige entre 'piedra', 'papel' o 'tijeras'.")

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

    # Mensaje final del juego
    if victorias_jugador == 3:
        print("\n🥳 ¡Felicidades! ¡Has ganado el juego!")
    else:
        print("\n😔 La computadora ha ganado el juego. ¡Mejor suerte la próxima vez!")


if __name__ == "__main__":
    principal()