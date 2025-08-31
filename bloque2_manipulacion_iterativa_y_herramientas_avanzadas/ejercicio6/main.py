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
        list[int]: Una lista con los índices (posiciones) de la letra encontrada.
    """
    indices = []
    #Usames enumerate() para obtener tanto el índice (i) como el valor (c) en cada iteración.
    for i, c in enumerate(frase):
        if c.lower() == letra.lower():
            indices.append(i)
    return indices
def main():
    """
    Función main que solicita la frase y la letra al usuario,
    valida las entradas y muestra los resultados.
    """
    print("🔍 Analizador de Posiciones de Letras 🔍")

    # Solicita la frase al usuario
    frase = input("Por favor, ingrese una frase: ").strip()
    if frase == "":
        print("⚠️ Advertencia: La frase no puede estar vacía.")
        return

    # Solicita la letra al usuario y valida que sea un solo carácter
    letra = input("Por favor, ingrese una letra para buscar en la frase: ").strip()
    if len(letra) != 1 or not letra.isalpha():
        print("❌ Error: Debe ingresar una sola letra válida (a-z o A-Z).")
        return

    # Encuentra los índices de la letra en la frase
    indices_encontrados = encontrar_indices(frase, letra)

    # Muestra los resultados
    if indices_encontrados:
        print(f"\nLa letra '{letra}' se encontró en las posiciones: {indices_encontrados}")
    else:
        print(f"\nLa letra '{letra}' no se encontró en la frase.")


if __name__ == "__main__":
    main()
