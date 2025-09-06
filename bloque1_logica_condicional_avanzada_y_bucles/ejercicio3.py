"""
Ejercicio 3: Validador de Contraseñas

Este programa solicita una contraseña y la valida usando un conjunto de reglas.
Toda la lógica de validación está encapsulada en la función `validar_contrasena`
para facilitar las pruebas y la reutilización.
"""


def validar_contrasena(contrasena: str) -> bool:
    """
    Valida una contraseña según criterios de seguridad. Si es válida, retorna True.
    Si no cumple alguna regla, lanza un error ValueError con el motivo.

    Args:
        contrasena (str): La contraseña a validar.
    Returns:
        bool: True si la contraseña es válida.
    Raises:
        ValueError: Si la contraseña no cumple con alguna de las reglas.
    """
    # 1. Validación de entrada vacía o solo con espacios
    if not contrasena.strip():
        raise ValueError("la contraseña no puede estar vacía ni contener solo espacios")

    # 2. Criterio: Longitud mínima de 8 caracteres
    if len(contrasena) < 8:
        raise ValueError("la contraseña debe tener al menos 8 caracteres")

    # 3. Criterio: Al menos una letra mayúscula
    if not any(c.isupper() for c in contrasena):
        raise ValueError("la contraseña debe contener al menos una letra mayúscula")

    # 4. Criterio: Al menos un número
    if not any(c.isdigit() for c in contrasena):
        raise ValueError("la contraseña debe contener al menos un número")

    # Si todas las validaciones pasan, la contraseña es correcta
    return True


def principal():
    """
    Función principal que pide la contraseña y la valida en un bucle.
    """
    print("🔐 Creador de Contraseñas Seguras")
    print("   1. Mínimo 8 caracteres")
    print("   2. Al menos una letra mayúscula")
    print("   3. Al menos un número")

    while True:
        try:
            contrasena_usuario = input("\nIngrese una nueva contraseña: ")

            # Se llama a la función que contiene toda la lógica
            if validar_contrasena(contrasena_usuario):
                print("\n✅ ¡Contraseña válida y segura! Ha cumplido con todos los requisitos.")
                break  # Si es válida, salimos del bucle

        except ValueError as e:
            # Si validar_contrasena lanza un error, lo capturamos y mostramos aquí
            print(f"⛔ Error: {e}")


if __name__ == "__main__":
    principal()