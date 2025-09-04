"""
Pruebas unitarias para el Ejercicio 6: Analizador de Posiciones de Letras.

Verifica la lógica de la función encontrar_indices en diferentes escenarios,
incluyendo casos con múltiples coincidencias, sin coincidencias y mayúsculas/minúsculas.
"""

import pytest
from .main import encontrar_indices

def test_letra_encontrada_una_vez():
    """Prueba cuando la letra aparece una sola vez."""
    frase = "Python"
    letra = "o"
    assert encontrar_indices(frase, letra) == [5]

def test_letra_encontrada_multiples_veces():
    """Prueba cuando la letra aparece varias veces."""
    frase = "banana"
    letra = "a"
    assert encontrar_indices(frase, letra) == [2, 4, 6]

def test_letra_no_encontrada():
    """Prueba cuando la letra no está en la frase."""
    frase = "programacion"
    letra = "z"
    assert encontrar_indices(frase, letra) == []

def test_mayusculas_y_minusculas():
    """Prueba que la función no distinga entre mayúsculas y minúsculas."""
    frase = "Hola SENA"
    letra = "a"
    assert encontrar_indices(frase, letra) == [4, 8]

def test_frase_vacia():
    """Prueba con una frase vacía."""
    frase = ""
    letra = "a"
    assert encontrar_indices(frase, letra) == []

def test_caracter_especial():
    """Prueba la búsqueda de un carácter especial."""
    frase = "esto-es-una-prueba"
    letra = "-"
    assert encontrar_indices(frase, letra) == [5, 8, 12]
