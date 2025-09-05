"""
Ejercicio 7: Combinador de Listas con zip

Este programa combina dos listas (nombres y notas de estudiantes) en un diccionario
y luego itera sobre este para imprimir un reporte detallado.
"""
from typing import Dict, List

def combinar_listas_a_diccionario(nombres: List[str], notas: List[float]) -> Dict[str, float]:
    """
    Combina dos listas de igual longitud en un diccionario,
    donde los nombres son las claves y las notas son los valores.

    Args:
        nombres (List[str]): Una lista de nombres de estudiantes.
        notas (List[float]): Una lista de notas de los estudiantes.

    Returns:
        Dict[str, float]: Un diccionario con la información combinada.
    """
    # zip() combina los elementos de las dos listas en tuplas.
    # dict() convierte esas tuplas en un diccionario.
    return dict(zip(nombres, notas))

def main():
    """
    Función principal que demuestra la combinación de listas y la impresión
    del reporte.
    """
    nombres_estudiantes = ["Ana", "Luis", "Sofía", "Carlos"]
    notas_finales = [4.5, 3.8, 5.0, 4.2]

    print("📚 Generador de Reporte de Notas 📚")

    # Validación: verificar que las listas tengan la misma longitud
    if len(nombres_estudiantes) != len(notas_finales):
        print("❌ Error: Las listas de nombres y notas deben tener la misma cantidad de elementos.")
        return

    # Combina las listas en un diccionario
    reporte_notas = combinar_listas_a_diccionario(nombres_estudiantes, notas_finales)

    print("\n✅ Reporte de Notas:")
    # Itera sobre los elementos del diccionario para imprimir el reporte
    for nombre, nota in reporte_notas.items():
        print(f"El estudiante {nombre} tiene una nota de {nota}.")

if __name__ == "__main__":
    main()
