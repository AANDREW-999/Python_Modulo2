"""
Pruebas unitarias para el Ejercicio 11: Validador de Cédula.

Verifica la lógica de la función validar_cedula con diferentes entradas,
incluyendo casos válidos, inválidos y con caracteres no numéricos.
"""
import pytest
from .main import validar_cedula

def test_cedula_valida_par():
    """Prueba una cédula cuya suma de dígitos es par."""
    # 1+2+3+4+5+6 = 21 (impar)
    # 1+2+3+4+5+7 = 22 (par)
    assert validar_cedula("123457") is True

def test_cedula_invalida_impar():
    """Prueba una cédula cuya suma de dígitos es impar."""
    # 1+2+3+4+5+6 = 21 (impar)
    assert validar_cedula("123456") is False

def test_cedula_con_letras():
    """Prueba una cédula que contiene letras."""
    assert validar_cedula("123A45") is False

def test_cedula_con_caracteres_especiales():
    """Prueba una cédula que contiene caracteres especiales."""
    assert validar_cedula("123-456") is False

def test_cedula_vacia():
    """Prueba una cadena de cédula vacía."""
    assert validar_cedula("") is False

def test_cedula_con_un_solo_digito():
    """Prueba una cédula con un solo dígito."""
    assert validar_cedula("4") is True
    assert validar_cedula("5") is False

def test_suma_grande_par():
    """Prueba una cédula con una suma de dígitos grande y par."""
    # 9+9+9+9+9+9+9 = 63 (impar)
    # 9+9+9+9+9+9+8 = 62 (par)
    assert validar_cedula("9999998") is True