"""
Pruebas unitarias para el Ejercicio 11: Validador de Cédula.

Se verifica la lógica de la función validar_cedula con entradas
válidas e inválidas, esperando excepciones en los casos de error.
"""
import pytest
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio11 import validar_cedula

# --- Pruebas para la lógica de validación ---

def test_cedula_valida_par():
    """Prueba una cédula cuya suma de dígitos es par."""
    # Suma de dígitos: 1+2+3+4+5+0+1+2+3+4 = 25 (impar), 1+2+3+4+5+7+1+2+3+4 = 32 (par)
    assert validar_cedula("1234571234") is True

def test_cedula_invalida_impar():
    """Prueba una cédula cuya suma de dígitos es impar."""
    # Suma de dígitos: 1+2+3+4+5+6+1+2+3+4 = 31 (impar)
    assert validar_cedula("1234561234") is False

# --- Pruebas para las validaciones de entrada (errores) ---

def test_cedula_corta_lanza_excepcion():
    """Prueba que una cédula de menos de 10 dígitos lance un ValueError."""
    with pytest.raises(ValueError, match="exactamente 10 dígitos"):
        validar_cedula("123")

def test_cedula_larga_lanza_excepcion():
    """Prueba que una cédula de más de 10 dígitos lance un ValueError."""
    with pytest.raises(ValueError, match="exactamente 10 dígitos"):
        validar_cedula("12345678901")

def test_cedula_con_letras_lanza_excepcion():
    """Prueba que una cédula con letras lance un ValueError."""
    with pytest.raises(ValueError, match="solo números"):
        validar_cedula("123A456789")

def test_cedula_con_espacios_lanza_excepcion():
    """Prueba que una cadena de cédula con espacios lance un ValueError."""
    with pytest.raises(ValueError, match="solo números"):
        validar_cedula("123 456789")

def test_cedula_vacia_lanza_excepcion():
    """Prueba que una cadena de cédula vacía lance un ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacío"):
        validar_cedula("")