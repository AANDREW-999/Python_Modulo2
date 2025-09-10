"""
Ejercicio 11: Validador de Cédula (Algoritmo Simple)

Este programa valida un número de cédula según una regla simple: la suma
de sus dígitos debe ser un número par. La lógica de validación está
encapsulada en una función que lanza excepciones para manejar los errores.
"""
from typing import List


def validar_cedula(cedula: str) -> bool:
    """
    Valida la entrada de cédula y luego comprueba si la suma de sus dígitos es par.

    Args:
        cedula (str): El número de cédula como una cadena de texto.

    Returns:
        bool: True si la suma de los dígitos es par.

    Raises:
        ValueError: Si la entrada está vacía, no contiene solo números o no tiene 10 dígitos.
    """
    if not cedula.strip():
        raise ValueError("El campo de la cédula no puede estar vacío.")

    if not cedula.isdigit():
        raise ValueError("La cédula debe contener solo números.")

    if len(cedula) != 10:
        raise ValueError("La cédula debe tener exactamente 10 dígitos.")

    suma_digitos = sum(int(digito) for digito in cedula)
    return suma_digitos % 2 == 0


def main():
    """
    Función principal que solicita y gestiona la validación de la cédula.
    """
    print("🛂 Validador de Cédula 🛂")
    print("La cédula es válida si la suma de sus dígitos es par.")

    while True:
        try:
            cedula_usuario = input("\nIngrese su número de cédula: ")

            es_valida = validar_cedula(cedula_usuario)

            if es_valida:
                print("✅ ¡Cédula válida!")
                break
            else:
                print("❌ Cédula no válida. La suma de sus dígitos es impar. Intente de nuevo.")

        except ValueError as e:
            print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()