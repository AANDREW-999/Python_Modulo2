"""
Pruebas unitarias para el Ejercicio 9: Transformación de Datos con Dictionary Comprehensions.

Verifica que la función transforme correctamente la lista de diccionarios a un
nuevo diccionario con el IVA incluido.
"""
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio9 import transformar_productos_a_diccionario



def test_transformacion_basica_correcta():
    """
    Prueba que la función transforme la lista de productos correctamente,
    calculando el IVA.
    """
    lista_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    # Precios esperados con 19% de IVA
    # 50000 * 1.19 = 59500.0
    # 80000 * 1.19 = 95200.0
    diccionario_esperado = {
        "Camisa": 59500.0,
        "Pantalón": 95200.0
    }

    assert transformar_productos_a_diccionario(lista_productos) == diccionario_esperado


def test_lista_vacia():
    """Prueba que la función devuelva un diccionario vacío para una lista vacía."""
    assert transformar_productos_a_diccionario([]) == {}


def test_un_solo_producto():
    """Prueba la transformación con una lista que contiene un solo producto."""
    lista_productos = [{"nombre": "Zapatos", "precio": 100000}]
    diccionario_esperado = {"Zapatos": 119000.0}
    assert transformar_productos_a_diccionario(lista_productos) == diccionario_esperado
