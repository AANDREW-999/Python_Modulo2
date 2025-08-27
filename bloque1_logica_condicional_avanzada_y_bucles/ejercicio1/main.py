"""
Ejercicio 1: Sistema de Precios de Entradas de Cine

Este programa calcula el precio de una entrada de cine basándose en la edad del usuario
y si es estudiante, aplicando las reglas de descuento correspondientes.
"""


def calcular_precio_entrada(edad: int, es_estudiante: str) -> float:
    """
    Calcula el precio de la entrada de cine según la edad y el estado de estudiante.

    Args:
        edad (int): La edad del usuario.
        es_estudiante (str): Indica si el usuario es estudiante ('si' o 'no').

    Returns:
        float: El precio final de la entrada.
    """
    precio_base = 0.0

    if edad < 12:
        precio_base = 10000.0
    elif 12 <= edad < 18:
        precio_base = 15000.0
    elif edad >= 18:
        precio_base = 20000.0

    # Aplica el descuento del 10% si el usuario es estudiante
    if es_estudiante.lower() == 'si':
        precio_final = precio_base * 0.9
    else:
        precio_final = precio_base

    return precio_final


def main():
    """
    Función principal que solicita datos al usuario, los valida y muestra
    el precio de la entrada.
    """
    print("🎬 Sistema de Precios de Entradas de Cine 🎬")

    # Validación de la edad
    while True:
        try:
            edad_input = input("Por favor, ingrese su edad: ")
            edad = int(edad_input)

            if edad < 0:
                print("⚠️ Error: La edad no puede ser un número negativo. Intente de nuevo.")
            elif edad > 110:
                print("⚠️ Error: La edad máxima permitida es de 110 años. Intente de nuevo.")
            else:
                # La edad es un número válido y dentro del rango. Salir del bucle.
                break

        except ValueError:
            # Esto se ejecuta si la entrada no se puede convertir a un entero.
            print("⚠️ Error: Entrada no válida. Por favor, ingrese un número entero para la edad.")

    # Validación del estado de estudiante
    while True:
        es_estudiante_input = input("¿Es usted estudiante? (si/no): ").lower()
        if es_estudiante_input in ['si', 'no']:
            break
        else:
            print("⚠️ Error: Respuesta no válida. Por favor, escriba 'si' o 'no'.")

    # Llama a la función para calcular el precio y muestra el resultado
    precio = calcular_precio_entrada(edad, es_estudiante_input)

    estado_estudiante = "estudiante" if es_estudiante_input == 'si' else "no estudiante"

    print(f"\n✅ El precio de la entrada para una persona de {edad} años ({estado_estudiante}) es de: ${precio:,.2f}")


if __name__ == "__main__":
    main()