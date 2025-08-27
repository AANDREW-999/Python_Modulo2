"""
Ejercicio 3: Validador de Contraseñas

Este programa solicita al usuario que cree una contraseña y la valida
basándose en un conjunto de reglas. El bucle continuará hasta que la
contraseña cumpla con todos los criterios de seguridad.
"""


def validar_contrasena(contrasena: str) -> dict:
    """
    Valida una contraseña según criterios de seguridad específicos.

    Args:
        contrasena (str): La contraseña a validar.

    Returns:
        dict: Un diccionario con los resultados de la validación.
              'valida': bool (True si es válida, False en caso contrario).
              'mensajes': list (Lista de strings con los errores encontrados).
    """
    mensajes_error = []
    es_valida = True

    # Criterio 1: Longitud mínima de 8 caracteres
    if len(contrasena) < 8:
        mensajes_error.append("❌ La contraseña debe tener al menos 8 caracteres.")
        es_valida = False

    # Criterio 2: Al menos una letra mayúscula
    if not any(c.isupper() for c in contrasena):
        mensajes_error.append("❌ La contraseña debe contener al menos una letra mayúscula.")
        es_valida = False

    # Criterio 3: Al menos un número
    if not any(c.isdigit() for c in contrasena):
        mensajes_error.append("❌ La contraseña debe contener al menos un número.")
        es_valida = False

    return {"valida": es_valida, "mensajes": mensajes_error}


def main():
    """
    Función main que pide la contraseña y la valida en un bucle.
    """
    print("🔐 Creador de Contraseñas Seguras")
    print("Criterios de validación:")
    print(" 1. Mínimo 8 caracteres")
    print(" 2. Al menos una letra mayúscula")
    print(" 3. Al menos un número")

    while True:
        contrasena = input("\nIngrese una nueva contraseña: ")

        # Validación de entrada vacía
        if contrasena == "":
            print("⚠️ Advertencia: No puede ingresar una contraseña vacía.")
            continue

        resultado_validacion = validar_contrasena(contrasena)

        if resultado_validacion["valida"]:
            print("\n✅ ¡Contraseña válida! Ha cumplido con todos los requisitos.")
            break
        else:
            print("\n⛔ La contraseña no es válida. Revise los siguientes errores:")
            for mensaje in resultado_validacion["mensajes"]:
                print(mensaje)


if __name__ == "__main__":
    main()