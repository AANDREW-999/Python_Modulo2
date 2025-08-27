"""
Ejercicio 5: Clasificador de Números (Par/Impar con Ternario)

Este programa solicita un número al usuario y, utilizando el operador ternario,
determina si es par o impar. Adicionalmente, verifica si el número es múltiplo de 5.
"""


def clasificar_numero(numero: int) -> str:
    """
    Clasifica un número como 'Par' o 'Impar' usando el operador ternario.

    Args:
        numero (int): El número entero a clasificar.

    Returns:
        str: La cadena 'Par' si el número es par, 'Impar' si es impar.
    """
    # Operador ternario: (valor_si_verdadero) if (condicion) else (valor_si_falso)
    estado = "Par" if numero % 2 == 0 else "Impar"
    if numero == 0:
        estado = "Neutro"
    return estado


def main():
    """
    Función main que solicita el número, realiza las validaciones y
    muestra los resultados al usuario.
    """
    print("🔢 Clasificador de Números (Par/Impar) 🔢")

    # Bucle para validar que la entrada sea un número entero
    while True:
        try:
            entrada_usuario = input("Por favor, ingrese un número entero: ")
            if entrada_usuario == '':
                print("⚠️ Advertencia: La entrada no puede estar vacía. Intente de nuevo.")
                continue
            numero = int(entrada_usuario)
            break
        except ValueError:
            print("❌ Error: La entrada no es un número entero válido. Intente de nuevo.")

    # Usa la función para clasificar el número y muestra el resultado
    resultado_clasificacion = clasificar_numero(numero)
    print(f"\nEl número {numero} es: {resultado_clasificacion}")

    # Mensaje especial para el número cero
    if numero == 0:
        print("⚠️ Nota: El número cero es considerado 'Neutro' y es múltiplo de todos los números.")

    # Mensaje adicional si el número es múltiplo de 5
    if numero % 5 == 0:
        print("💡 ¡Dato extra! Este número también es un múltiplo de 5.")


if __name__ == "__main__":
    main()


