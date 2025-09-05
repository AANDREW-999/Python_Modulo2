"""
Ejercicio 2: Interprete de Comandos Sencillos

Este programa simula un menu de consola que procesa comandos como 'guardar', 'cargar' y 'salir' usando la
estructura match-case.
El programa continuará pidiendo comandos hasta que el usuario ingrese 'salir'
"""


def main():
    """
    Función Principal que ejecuta el bucle del intérprete de comandos.
    """
    print("\n🚀 Intérprete de Comandos Sencillos!")
    print("Comandos disponibles: guardar, cargar, salir!")

    ejecutar_programa = True

    while ejecutar_programa:

        comando_usuario = input("\nIngrese un comando que quiere: ").strip().lower()

        # Validación de entrada vacía
        if comando_usuario == "":
            print("⚠️ Advertencia: No ingresó ningún comando. Intente de nuevo.")
            continue

        ejecutar_programa = procesar_comandos(comando_usuario)


def procesar_comandos(comando: str) -> bool:
    """
    Procesa un comando de la consola y ejecuta la acción correspondiente.
    Args:
        comando (str): comando ingresado por el usuario.
    Returns:
        bool: Retorna False si el comando es 'salir',
        de lo contrario, True.
    """
    comando = comando.lower()  # Convertir a minúscula para una validación consistente

    match comando:
        case "guardar":
            print("💾 Guardando archivo...")
        case "cargar":
            print("📁 Cargando archivo...")
        case "salir":
            print("✌️ Saliendo del intérprete. ¡Hasta la proxima!...")
            return False
        case _:
            print(f"❌ Error: Comando {comando} no es reconocido. "
                  f"Comandos validos: guardar, cargar, salir!")
    return True


if __name__ == "__main__":
    main()
