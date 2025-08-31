"""
Pruebas unitarias para el Ejercicio 8: Filtrado de Datos con List Comprehensions.

Verifica que la función procesar_numeros genere las tres listas de salida
correctamente para diferentes conjuntos de datos.
"""

import pytest
from .main import procesar_numeros


def test_procesamiento_basico():
    """Prueba el caso de uso principal con números positivos y negativos."""
    numeros = [-5, 10, -15, 20, -25, 30]

    numeros_positivos_esperado = [10, 20, 30]
    cuadrados_esperado = [25, 100, 225, 400, 625, 900]
    clasificacion_esperado = ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]

    positivos_obtenido, cuadrados_obtenido, clasificacion_obtenido = procesar_numeros(numeros)

    assert positivos_obtenido == numeros_positivos_esperado
    assert cuadrados_obtenido == cuadrados_esperado
    assert clasificacion_obtenido == clasificacion_esperado


def test_lista_vacia():
    """Prueba con una lista de números vacía."""
    numeros = []
    positivos, cuadrados, clasificacion = procesar_numeros(numeros)

    assert positivos == []
    assert cuadrados == []
    assert clasificacion == []


def test_solo_numeros_negativos():
    """Prueba con una lista que solo contiene números negativos."""
    numeros = [-1, -2, -3]

    positivos_obtenido, cuadrados_obtenido, clasificacion_obtenido = procesar_numeros(numeros)

    assert positivos_obtenido == []
    assert cuadrados_obtenido == [1, 4, 9]
    assert clasificacion_obtenido == ["negativo", "negativo", "negativo"]


def test_solo_numeros_positivos():
    """Prueba con una lista que solo contiene números positivos."""
    numeros = [1, 2, 3]

    positivos_obtenido, cuadrados_obtenido, clasificacion_obtenido = procesar_numeros(numeros)

    assert positivos_obtenido == [1, 2, 3]
    assert cuadrados_obtenido == [1, 4, 9]
    assert clasificacion_obtenido == ["positivo", "positivo", "positivo"]


def test_con_cero():
    """Prueba un caso que incluye el número cero."""
    numeros = [0, 5, -5]

    positivos_obtenido, cuadrados_obtenido, clasificacion_obtenido = procesar_numeros(numeros)

    assert positivos_obtenido == [5]
    assert cuadrados_obtenido == [0, 25, 25]
    assert clasificacion_obtenido == ["positivo", "positivo", "negativo"]
