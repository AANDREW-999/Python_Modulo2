"""
Ejercicio 9: Transformación de Datos con Dictionary Comprehensions

Este programa utiliza una comprensión de diccionario para transformar una lista
de productos (diccionarios) en un nuevo diccionario. Las claves serán los
nombres de los productos y los valores serán sus precios con el 19% de IVA.
"""
from typing import List, Dict

# Constante para la tasa de IVA
TASA_IVA = 0.19


def calcular_iva(precio: float) -> float:
    """
    Calcula el precio final de un producto incluyendo el 19% de IVA.

    Args:
        precio (float): El precio base del producto.

    Returns:
        float: El precio final con IVA.
    """
    return precio * (1 + TASA_IVA)


def transformar_productos_a_diccionario(productos: List[Dict]) -> Dict[str, float]:
    """
    Crea un diccionario de productos a partir de una lista de diccionarios,
    calculando el precio con IVA.

    Args:
        productos (List[Dict]): Una lista de diccionarios con 'nombre' y 'precio'.

    Returns:
        Dict[str, float]: Un diccionario con el nombre del producto como clave
                          y su precio con IVA como valor.
    """
    # La comprensión de diccionario itera sobre la lista y crea pares clave:valor
    # La expresión: {item['nombre']: calcular_iva(item['precio']) for item in productos}
    # - 'item' es cada diccionario en la lista de 'productos'
    # - 'item['nombre']' se convierte en la clave
    # - 'calcular_iva(item['precio'])' se convierte en el valor
    return {item['nombre']: calcular_iva(item['precio']) for item in productos}


def principal():
    """
    Función principal que demuestra la transformación de la lista de productos.
    """
    lista_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000}
    ]

    print("🛒 Transformador de Productos con IVA 🛒")
    print("Lista de productos original:")
    for producto in lista_productos:
        print(f" - {producto['nombre']}: ${producto['precio']:,.0f}")

    # Llama a la función que usa la comprensión de diccionario
    precios_con_iva = transformar_productos_a_diccionario(lista_productos)

    print("\n✅ Diccionario de precios con IVA (19%):")
    # Itera sobre el diccionario resultante y lo imprime de forma legible
    for nombre, precio_iva in precios_con_iva.items():
        print(f" - {nombre}: ${precio_iva:,.2f}")


if __name__ == "__main__":
    principal()