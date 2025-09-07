"""
Ejercicio 6: Analizador de Posiciones de Letras

Este programa encuentra los índices de una letra en una frase.
La lógica de validación y búsqueda está encapsulada en una sola función
para máxima cohesión y facilidad de prueba.
"""


def analizar_frase_y_letra(frase_raw: str, letra_raw: str) -> list[int]:
    """
    Valida la frase y la letra, y luego busca las posiciones de la letra.
    Las posiciones se cuentan ignorando los espacios.

    Args:
        frase_raw (str): La frase ingresada por el usuario.
        letra_raw (str): La letra a buscar, ingresada por el usuario.
    Returns:
        list[int]: Una lista con las posiciones (basadas en 1) de la letra.
    Raises:
        ValueError: Si alguna de las entradas no cumple las reglas.
    """
    # --- 1. Validación de la Frase ---
    frase_validada = frase_raw.strip()
    if not frase_validada:
        raise ValueError("la frase no puede estar vacía")
    if any(c.isdigit() for c in frase_validada):
        raise ValueError("la frase no puede contener números")

    # --- 2. Validación de la Letra ---
    letra_validada = letra_raw.strip()
    if not letra_validada:
        raise ValueError("la letra a buscar no puede estar vacía")
    if len(letra_validada) != 1:
        raise ValueError("debe ingresar una sola letra para la búsqueda")
    if not letra_validada.isalpha():
        raise ValueError("la letra a buscar debe ser un carácter del alfabeto (a-z)")

    # --- 3. Lógica de Búsqueda ---
    indices = []
    frase_sin_espacios = frase_validada.replace(" ", "")

    # Usamos enumerate para obtener índice (i) y carácter (c)
    for i, c in enumerate(frase_sin_espacios):
        if c.lower() == letra_validada.lower():
            indices.append(i + 1)  # Se suma 1 para que sea más intuitivo

    return indices


def principal():
    """
    Función principal que gestiona la interacción con el usuario.
    """
    print("🔍 Analizador de Posiciones de Letras 🔍")
    print("(Nota: las posiciones se calculan sin contar los espacios)")

    while True:
        try:
            frase_usuario = input("\nPor favor, ingrese una frase: ")
            letra_usuario = input("Por favor, ingrese la letra a buscar: ")

            indices_encontrados = analizar_frase_y_letra(frase_usuario, letra_usuario)

            if indices_encontrados:
                posiciones_str = ", ".join(map(str, indices_encontrados))
                print(
                    f"\n✅ ¡Encontrada! La letra '{letra_usuario.strip()}' aparece en la(s) posición(es): {posiciones_str}.")
            else:
                print(f"\n❌ Lo siento, la letra '{letra_usuario.strip()}' no se encontró en la frase.")

            break  # Salimos del bucle si fue exitoso

        except ValueError as e:
            print(f"⚠️ Error: {e}. Inténtelo de nuevo.")


if __name__ == "__main__":
    principal()