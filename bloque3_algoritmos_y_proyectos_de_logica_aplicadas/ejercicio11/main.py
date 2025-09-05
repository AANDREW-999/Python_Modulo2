"""
Ejercicio 11: Validador de Cédula (Algoritmo Simple)

Este programa valida un número de cédula según una regla simple: la suma
de sus dígitos debe ser un número par. El programa solicita la cédula
al usuario en un bucle hasta que ingrese una válida.
"""
from typing import List


def validar_cedula(cedula: str) -> bool:
    """
    Valida un número de cédula comprobando si la suma de sus dígitos es par.

    Args:
        cedula (str): El número de cédula como una cadena de texto.

    Returns:
        bool: True si la suma de los dígitos es par, False en caso contrario.
    """
    # 1. Calcular la suma de los dígitos
    # Se usa un generador para mayor eficiencia
    suma_digitos = sum(int(digito) for digito in cedula)

    # 2. Comprobar si la suma es par y devolver el resultado directamente
    return suma_digitos % 2 == 0


def main():
    """
    Función principal que solicita y valida la cédula del usuario en un bucle.
    """
    print("🛂 Validador de Cédula 🛂")
    print("La cédula debe tener 10 dígitos y la suma de estos debe ser par.")

    while True:
        cedula_usuario = input("\nIngrese su número de cédula (10 dígitos): ").strip()

        # --- Validaciones previas antes de la lógica principal ---

        # 1. Validar si contiene solo números
        if not cedula_usuario.isdigit():
            print("❌ Error: La cédula debe contener únicamente números.")
            continue  # Vuelve al inicio del bucle

        # 2. Validar la longitud exacta de 10 dígitos
        if len(cedula_usuario) != 10:
            print(f"❌ Error: La cédula debe tener 10 dígitos (usted ingresó {len(cedula_usuario)}).")
            continue  # Vuelve al inicio del bucle

        # --- Si las validaciones de formato son correctas, se aplica la regla ---
        if validar_cedula(cedula_usuario):
            print(f"✅ ¡Cédula válida! La suma de sus dígitos es par.")
            break  # Termina el programa
        else:
            print("❌ Cédula no válida. La suma de sus dígitos es impar. Intente de nuevo.")


if __name__ == "__main__":
    main()