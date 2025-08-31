"""
Pruebas unitarias para el Ejercicio 10: Transposición de una Matriz.

Verifica que las funciones para transponer una matriz funcionen correctamente
con diferentes matrices de ejemplo.
"""
import pytest
from .main import transponer_con_bucles, transponer_con_comprension


def test_transponer_matriz_basica():
    """Prueba la transposición de una matriz 2x3 estándar."""
    matriz_original = [[1, 2, 3], [4, 5, 6]]
    matriz_transpuesta_esperada = [[1, 4], [2, 5], [3, 6]]

    assert transponer_con_bucles(matriz_original) == matriz_transpuesta_esperada
    assert transponer_con_comprension(matriz_original) == matriz_transpuesta_esperada


def test_transponer_matriz_cuadrada():
    """Prueba la transposición de una matriz cuadrada 3x3."""
    matriz_original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_transpuesta_esperada = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    assert transponer_con_bucles(matriz_original) == matriz_transpuesta_esperada
    assert transponer_con_comprension(matriz_original) == matriz_transpuesta_esperada


def test_matriz_vacia():
    """Prueba la transposición de una matriz vacía."""
    assert transponer_con_bucles([]) == []
    assert transponer_con_comprension([]) == []


def test_matriz_con_una_fila():
    """Prueba la transposición de una matriz con una sola fila."""
    matriz_original = [[1, 2, 3, 4]]
    matriz_transpuesta_esperada = [[1], [2], [3], [4]]

    assert transponer_con_bucles(matriz_original) == matriz_transpuesta_esperada
    assert transponer_con_comprension(matriz_original) == matriz_transpuesta_esperada