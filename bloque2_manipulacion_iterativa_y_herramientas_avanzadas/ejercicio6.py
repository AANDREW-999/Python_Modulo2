"""
Ejercicio 6: Analizador de Posiciones de Letras con enumerate

Este programa encuentra y devuelve todos los índices de una letra
especifica dentro de una frase, utilizando la función enumerate().
"""

def encontrar_indices(frase: str, letra: str) -> list[int]:
    """
    Encuentra todas las posiciones de una letra en una frase dada.

    Args:
        frase (str): La frase en la que se buscara la letra.
        letra (str): La letra a buscar. Debe ser un solo carácter.

    Returns:
        list[int]: Una lista con los índices (posiciones + 1) de la letra.
    """
    indices = []
    #Usames enumerate() para obtener tanto el índice (i) como el valor (c) en cada iteración.
    for i, c in enumerate(frase.replace(" ", "")):
        if c.lower() == letra.lower():
            indices.append(i + 1)
    return indices

def main():
    """
    Función main que solicita la frase y la letra al usuario,
    valida las entradas y muestra los resultados.
    """
    print("🔍 Analizador de Posiciones de Letras 🔍")

    # --- Validación de la Frase ---
    # El bucle se repetirá hasta que el usuario ingrese una frase no vacía.
    while True:
        frase = input("\nPor favor, ingrese una frase: ").strip().replace(" ", "").lower()
        if frase.isalpha():  # Si la frase no está vacía (es decir, no es "")
            break  # Salimos del bucle
        print("⚠️ Advertencia: La frase no puede estar vacía o no puede contener numeros. Inténtelo de nuevo.")

    # --- Validación de la Letra ---
    # El bucle se repetirá hasta que se ingrese un único carácter alfabético.
    while True:
        letra = input("Por favor, ingrese una letra para buscar en la frase: ").strip().replace(" ", "").lower()
        if len(letra) == 1 and letra.isalpha():
            break  # Salimos del bucle si es una sola letra
        print("❌ Error: Debe ingresar una sola letra válida (de la a-z). Inténtelo de nuevo.")

    # Encuentra los índices de la letra en la frase
    indices_encontrados = encontrar_indices(frase, letra)

    # Muestra los resultados
    if indices_encontrados:
        # Convertimos la lista de números a una lista de strings para unirlos con comas
        posiciones_str = ", ".join(map(str, indices_encontrados))
        print(f"\n✅ ¡Encontrada! La letra '{letra}' aparece en la(s) posición(es): {posiciones_str}.")
    else:
        print(f"\n❌ Lo siento, la letra '{letra}' no se encontró en la frase.")


if __name__ == "__main__":
    main()
