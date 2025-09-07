"""
Ejercicio 5: Clasificador de Números

El programa solicita un número y lo analiza. Toda la lógica de validación
y clasificación está encapsulada en la función `analizar_numero` para
facilitar pruebas exhaustivas.
"""

def analizar_numero(entrada_raw: str) -> tuple:
    """
    Valida y analiza una entrada para clasificarla como número.

    Args:
        entrada_raw (str): La entrada del usuario en formato de texto.
    Returns:
        tuple: (número_validado, clasificación, es_multiplo_de_5)
    Raises:
        ValueError: Si la entrada está vacía o no es un entero válido.
    """
    # 1. Validación de la entrada
    if not entrada_raw.strip():
        raise ValueError("la entrada no puede estar vacía")

    try:
        numero = int(entrada_raw)
    except ValueError:
        raise ValueError("la entrada debe ser un número entero válido")

    # 2. Análisis del número
    # Usamos un ternario anidado para la clasificación
    clasificacion = "Neutro" if numero == 0 else ("Par" if numero % 2 == 0 else "Impar")

    es_multiplo_de_5 = (numero % 5 == 0)

    return numero, clasificacion, es_multiplo_de_5

def principal():
    """
    Función principal que solicita el número y muestra el análisis.
    """
    print("🔢 Clasificador de Números 🔢")

    while True:
        try:
            entrada_usuario = input("\nPor favor, ingrese un número entero: ")

            # La función `analizar_numero` hace la validación y el análisis
            numero, clasificacion, es_multiplo = analizar_numero(entrada_usuario)

            # Si el análisis es exitoso, imprimimos los resultados
            print(f"\nEl número {numero} es: {clasificacion}")

            if es_multiplo:
                if numero == 0:
                    print("💡 ¡Dato extra! El cero es múltiplo de todos los números, incluido el 5.")
                else:
                    print("💡 ¡Dato extra! Este número también es múltiplo de 5.")

            break # Salimos del bucle si todo fue correcto

        except ValueError as e:
            print(f"❌ Error: {e}. Intente de nuevo.")

if __name__ == "__main__":
    principal()