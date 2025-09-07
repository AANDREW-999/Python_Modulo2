"""
Ejercicio 7: Combinador de Listas con zip

Este programa combina dos listas (nombres y notas de estudiantes) en un diccionario
y luego itera sobre este para imprimir un reporte detallado. La validación de la
longitud de las listas se realiza dentro de la función de combinación.
"""
from typing import Dict, List

def combinar_listas_a_diccionario(nombres: List[str], notas: List[float]) -> Dict[str, float]:
    """
    Combina dos listas en un diccionario, validando que tengan la misma longitud.

    Args:
        nombres (List[str]): Una lista de nombres de estudiantes.
        notas (List[float]): Una lista de notas de los estudiantes.

    Returns:
        Dict[str, float]: Un diccionario con la información combinada.

    Raises:
        ValueError: Si las listas no tienen la misma cantidad de elementos.
    """
    # Validación: verificar que las listas tengan la misma longitud
    if len(nombres) != len(notas):
        raise ValueError("Las listas de nombres y notas deben tener la misma cantidad de elementos.")

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

    try:
        # Combina las listas en un diccionario
        reporte_notas = combinar_listas_a_diccionario(nombres_estudiantes, notas_finales)

        print("\n✅ Reporte de Notas:")
        # Itera sobre los elementos del diccionario para imprimir el reporte
        for nombre, nota in reporte_notas.items():
            print(f"El estudiante {nombre} tiene una nota de {nota}.")

    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()