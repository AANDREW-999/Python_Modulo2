"""
Ejercicio 13: Aventura de Texto Simple

Este programa simula un pequeño juego de aventura basado en texto, con la lógica
separada en funciones para facilitar la modularidad y las pruebas.
"""
from typing import Dict, Optional, Tuple


def get_habitacion_info(habitacion: str) -> Optional[Tuple[str, Dict[str, str]]]:
    """
    Devuelve la descripción y los posibles movimientos para una habitación.

    Args:
        habitacion (str): El nombre de la habitación.

    Returns:
        Optional[Tuple[str, Dict[str, str]]]: Una tupla con la descripción y un
        diccionario de movimientos, o None si la habitación no existe.
    """
    habitaciones = {
        "entrada": {
            "descripcion": "Estás en una mazmorra oscura. Ves una puerta al norte y un pasillo al sur.",
            "movimientos": {"norte": "sala_tesoro", "sur": "pasillo_sur"}
        },
        "pasillo_sur": {
            "descripcion": "Es un pasillo largo y oscuro. Hay una puerta al este y una al oeste.",
            "movimientos": {"este": "sala_trampa", "oeste": "sala_tesoro"}
        },
        "sala_tesoro": {
            "descripcion": "¡Llegaste! Encontraste el cofre del tesoro. Lo abres y... ¡Ganaste el juego! 💎",
            "movimientos": {}  # Estado final
        },
        "sala_trampa": {
            "descripcion": "Entras a una habitación con una trampa en el piso. ¡El techo comienza a caer! Perdiste el juego. 💀",
            "movimientos": {}  # Estado final
        }
    }

    info = habitaciones.get(habitacion)
    if info:
        return info["descripcion"], info["movimientos"]
    return None


def manejar_decision(habitacion_actual: str, comando: str) -> str:
    """
    Procesa el comando del jugador y determina la siguiente habitación.

    Args:
        habitacion_actual (str): El nombre de la habitación actual del jugador.
        comando (str): El comando ingresado por el jugador.

    Returns:
        str: El nombre de la siguiente habitación o la misma si el movimiento es inválido.
    """
    partes_comando = comando.split()
    if len(partes_comando) != 2 or partes_comando[0] != "ir":
        return habitacion_actual

    direccion = partes_comando[1]

    info_habitacion = get_habitacion_info(habitacion_actual)
    if not info_habitacion:
        return habitacion_actual

    _, movimientos_posibles = info_habitacion

    return movimientos_posibles.get(direccion, habitacion_actual)


def principal():
    """
    Función principal que ejecuta el bucle del juego.
    """
    print("🏰 Bienvenido a la Aventura de la Mazmorra Perdida 🏰")
    print("Comandos disponibles: 'ir [dirección]', 'ayuda', 'salir'")

    habitacion_actual = "entrada"

    while True:
        info_habitacion = get_habitacion_info(habitacion_actual)
        if not info_habitacion:
            print("Error: Habitación desconocida.")
            break

        descripcion, movimientos_posibles = info_habitacion

        print(f"\n--- Estás en la habitación: {habitacion_actual.upper()} ---")
        print(descripcion)

        # Validar estado final del juego
        if habitacion_actual in ["sala_tesoro", "sala_trampa"]:
            break

        comando = input("¿Qué decides hacer?: ").lower()

        if comando == "ayuda":
            print("Comandos disponibles: 'ir [dirección]', 'ayuda', 'salir'")
        elif comando == "salir":
            print("Saliendo del juego. ¡Hasta luego!")
            break
        else:
            proxima_habitacion = manejar_decision(habitacion_actual, comando)
            if proxima_habitacion == habitacion_actual:
                print("❌ No puedes ir en esa dirección o el comando no es válido.")
            else:
                habitacion_actual = proxima_habitacion

    print("\n¡Fin del juego!")


if __name__ == "__main__":
    principal()