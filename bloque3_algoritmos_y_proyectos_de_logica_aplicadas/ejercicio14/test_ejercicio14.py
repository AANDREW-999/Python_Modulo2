"""
Pruebas unitarias para el Ejercicio 14: Juego del Ahorcado (Hangman).

Verifica la lógica de las funciones de validación de entrada y selección de palabra.
"""
import pytest
import random
from .main import seleccionar_palabra, validar_entrada, PALABRAS_SECRETAS

def test_seleccionar_palabra():
    """Prueba que la palabra seleccionada sea de la lista predefinida."""
    # Para asegurar la aleatoriedad, se prueba múltiples veces
    for _ in range(20):
        palabra = seleccionar_palabra()
        assert palabra in PALABRAS_SECRETAS

def test_validar_entrada_letra_unica_valida():
    """Prueba una entrada de una sola letra que no ha sido adivinada."""
    letras_adivinadas = {"a", "b", "c"}
    assert validar_entrada("d", letras_adivinadas) is True

def test_validar_entrada_letra_ya_adivinada():
    """Prueba una letra que ya ha sido adivinada."""
    letras_adivinadas = {"a", "b", "c"}
    # La validación debe fallar aunque la letra sea válida
    assert validar_entrada("a", letras_adivinadas) is False

def test_validar_entrada_no_letra():
    """Prueba una entrada que no es una letra (un número)."""
    letras_adivinadas = set()
    assert validar_entrada("1", letras_adivinadas) is False
    assert validar_entrada("!", letras_adivinadas) is False

def test_validar_entrada_mas_de_una_letra():
    """Prueba una entrada con más de un carácter."""
    letras_adivinadas = set()
    assert validar_entrada("abc", letras_adivinadas) is False

def test_validar_entrada_vacia():
    """Prueba una entrada vacía."""
    letras_adivinadas = set()
    assert validar_entrada("", letras_adivinadas) is False