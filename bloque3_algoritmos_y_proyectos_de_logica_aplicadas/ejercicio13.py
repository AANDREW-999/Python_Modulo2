"""
Ejercicio 13: Aventura de Texto Simple

Este programa simula un pequeño juego de aventura basado en texto, con la lógica
separada en funciones para facilitar la modularidad y las pruebas.
"""
from typing import Dict, Optional, Tuple, List

# Diccionario de habitaciones, fuera de la función para facilitar el acceso
HABITACIONES = {
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


def get_habitacion_info(habitacion: str) -> Optional[Tuple[str, Dict[str, str]]]:
    """
    Devuelve la descripción y los posibles movimientos para una habitación.

    Args:
        habitacion (str): El nombre de la habitación.

    Returns:
        Optional[Tuple[str, Dict[str, str]]]: Una tupla con la descripción y un
        diccionario de movimientos, o None si la habitación no existe.
    """
    info = HABITACIONES.get(habitacion)
    if info:
        return info["descripcion"], info["movimientos"]
    return None


def validar_comando(habitacion_actual: str, comando: str) -> str:
    """
    Valida el comando del jugador y determina si el movimiento es posible.

    Args:
        habitacion_actual (str): El nombre de la habitación actual del jugador.
        comando (str): El comando ingresado por el jugador.

    Returns:
        str: La siguiente habitación si el comando es válido, o un mensaje de error.

    Raises:
        ValueError: Si el comando no tiene el formato correcto.
    """
    partes_comando = comando.strip().split()


    if len(partes_comando) != 2 or partes_comando[0] != "ir":
        raise ValueError("Comando no válido. Usa el formato 'ir [dirección]'.")

    _, direccion = partes_comando
    direccion = direccion.lower()
    info_habitacion = get_habitacion_info(habitacion_actual)

    if not info_habitacion:
        raise ValueError("Error: Habitación desconocida.")

    _, movimientos_posibles = info_habitacion

    if direccion not in movimientos_posibles:
        raise ValueError(f"No puedes ir en esa dirección: '{direccion}'.")

    return movimientos_posibles[direccion]


def main():
    """
    Función principal que ejecuta el bucle del juego.
    """
    print("🏰 Bienvenido a la Aventura de la Mazmorra Perdida 🏰")
    print("Comandos disponibles: 'ir [dirección]', 'ayuda', 'salir'")

    habitacion_actual = "entrada"

    while True:
        info_habitacion = get_habitacion_info(habitacion_actual)
        if not info_habitacion:
            print("Error: Habitación desconocida. Saliendo del juego.")
            break

        descripcion, _ = info_habitacion

        print(f"\n--- Estás en la habitación: {habitacion_actual.upper()} ---")
        print(descripcion)

        if habitacion_actual in ["sala_tesoro", "sala_trampa"]:
            break

        comando = input("¿Qué decides hacer?: ")

        if comando == "ayuda":
            print("Comandos disponibles: 'ir [dirección]', 'ayuda', 'salir'")
            continue
        if comando == "salir":
            print("Saliendo del juego. ¡Hasta luego!")
            break

        try:
            proxima_habitacion = validar_comando(habitacion_actual, comando)
            habitacion_actual = proxima_habitacion
        except ValueError as e:
            print(f"❌ Error: {e}")

    print("\n¡Fin del juego!")


if __name__ == "__main__":
    main()