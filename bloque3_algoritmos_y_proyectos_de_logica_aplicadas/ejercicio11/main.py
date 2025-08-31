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
    # 1. Validación de la entrada: asegurarse de que solo contenga dígitos.
    if not cedula.isdigit():
        print("⚠️ Error: La cédula debe contener solo números.")
        return False

    # 2. Calcular la suma de los dígitos
    suma_digitos = 0
    for digito in cedula:
        suma_digitos += int(digito)

    # 3. Comprobar si la suma es par
    if suma_digitos % 2 == 0:
        return True
    else:
        return False


def principal():
    """
    Función principal que solicita y valida la cédula del usuario en un bucle.
    """
    print("🛂 Validador de Cédula 🛂")
    print("La cédula es válida si la suma de sus dígitos es par.")

    while True:
        cedula_usuario = input("\nIngrese su número de cédula (solo números): ")

        # Validar si la entrada está vacía
        if not cedula_usuario.strip():
            print("⚠️ Error: No se puede dejar el campo de la cédula vacío.")
            continue

        # Llamar a la función de validación
        es_valida = validar_cedula(cedula_usuario)

        if es_valida:
            print(f"\n✅ ¡Cédula válida! La suma de sus dígitos ({sum(int(d) for d in cedula_usuario)}) es par.")
            break
        else:
            # El mensaje de error específico ya lo muestra la función validar_cedula
            print("❌ La cédula no es válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    principal()