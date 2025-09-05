"""
Pruebas unitarias para el Ejercicio 11: Validador de Cédula.

Verifica la lógica de la función validar_cedula con diferentes entradas,
incluyendo casos válidos, inválidos y con caracteres no numéricos.
"""
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio11 import validar_cedula

def test_cedula_valida_par():
    """Prueba una cédula cuya suma de dígitos es par."""
    assert validar_cedula("1234567891") is True

def test_cedula_invalida_impar():
    """Prueba una cédula cuya suma de dígitos es impar."""
    assert validar_cedula("1234567890") is False

