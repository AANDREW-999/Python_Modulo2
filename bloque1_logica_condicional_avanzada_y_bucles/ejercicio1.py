"""
Ejercicio 1: Sistema de Precios de Entradas de Cine

Este programa calcula el precio de una entrada de cine. La función principal
incluye toda la lógica de validación, incluyendo la verificación de campos
vacíos, para asegurar que los datos de entrada sean correctos.
"""

def calcular_precio_entrada(edad_input: str, es_estudiante: str) -> float:
    """
    Valida las entradas y calcula el precio de la entrada de cine.

    Args:
        edad_input (str): La edad del usuario como cadena de texto.
        es_estudiante (str): La respuesta del usuario a si es estudiante.

    Returns:
        float: El precio final de la entrada.

    Raises:
        ValueError: Si alguna entrada está vacía, la edad no es un número,
                    está fuera de rango, o si la respuesta de estudiante es inválida.
    """
    # 1. Validación de Entradas Vacías
    if not edad_input.strip() or edad_input == "":
        raise ValueError("el campo de la edad no puede estar vacío")

    if not es_estudiante.strip() or es_estudiante == "":
        raise ValueError("el campo de estudiante no puede estar vacío")

    # 2. Conversión y Validación de la Edad
    try:
        edad = int(edad_input)
    except ValueError:
        raise ValueError("la edad debe ser un número entero (ej: 30)")

    if not 0 <= edad <= 110:
        raise ValueError("la edad debe estar entre 0 y 110 años")

    # 3. Validación del Estado de Estudiante
    respuesta_normalizada = es_estudiante.lower().strip()
    if respuesta_normalizada not in ['si', 'no']:
        raise ValueError("la respuesta de estudiante debe ser 'si' o 'no'")

    # 4. Cálculo del Precio
    precio_base = 0.0
    if edad < 12:
        precio_base = 10000.0
    elif edad < 18:
        precio_base = 15000.0
    else:  # edad >= 18
        precio_base = 20000.0

    # Aplica el descuento del 10% si es estudiante
    if respuesta_normalizada == 'si':
        return precio_base * 0.9

    return precio_base


def main():
    """
    Función principal que solicita datos y gestiona los errores de validación.
    """
    print("🎬 Sistema de Precios de Entradas de Cine 🎬")

    while True:
        try:
            edad_input = input("\nPor favor, ingrese su edad: ")
            es_estudiante_input = input("¿Es usted estudiante? (si/no): ")

            precio = calcular_precio_entrada(edad_input, es_estudiante_input)

            estado = "estudiante" if es_estudiante_input.lower().strip() == 'si' else "no estudiante"
            print(f"\n✅ El precio para una persona de {edad_input} años ({estado}) es de: ${precio:,.2f}")
            break

        except ValueError as e:
            print(f"⚠️ Error: {e}. Intente de nuevo.")


if __name__ == "__main__":
    main()