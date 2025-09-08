"""
Ejercicio 2: Intérprete de Comandos Sencillos

Este programa simula un menú de consola que procesa comandos como 'guardar', 'cargar'
y 'salir'. La lógica de validación está encapsulada dentro de la función de procesamiento.
"""

def procesar_comandos(comando: str) -> bool:
    """
    Procesa un comando de la consola y ejecuta la acción correspondiente.

    Args:
        comando (str): Comando ingresado por el usuario.
    Returns:
        bool: Retorna False si el comando es 'salir', de lo contrario, True.
    Raises:
        ValueError: Si el comando está vacío o no es reconocido.
    """
    comando_normalizado = comando.strip().lower()

    # Validación de la entrada. Esto es lo nuevo que se añade a la función.
    if not comando_normalizado:
        raise ValueError("No se puede dejar el comando vacío.")

    if comando_normalizado not in ["guardar", "cargar", "salir"]:
        raise ValueError(f"El comando '{comando}' no es reconocido.")

    # Lógica de procesamiento con match-case
    match comando_normalizado:
        case "guardar":
            print("💾 Guardando archivo...")
            return True
        case "cargar":
            print("📁 Cargando archivo...")
            return True
        case "salir":
            print("✌️ Saliendo del intérprete. ¡Hasta la proxima!...")
            return False

def main():
    """
    Función principal que ejecuta el bucle del intérprete de comandos.
    """
    print("\n🚀 Intérprete de Comandos Sencillos!")
    print("Comandos disponibles: guardar, cargar, salir!")

    ejecutar_programa = True
    while ejecutar_programa:
        try:
            comando_usuario = input("\nIngrese un comando que quiere: ")
            ejecutar_programa = procesar_comandos(comando_usuario)
        except ValueError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()