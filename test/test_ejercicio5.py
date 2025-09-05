"""
Pruebas unitarias para el Ejercicio 5: Clasificador de Números.

Verifica que la función clasificar_numero retorne correctamente 'Par' o 'Impar'.
"""

from bloque1_logica_condicional_avanzada_y_bucles.ejercicio5 import clasificar_numero

def test_numero_par():
    """Prueba que la función retorne 'Par' para un número par."""
    assert clasificar_numero(4) == "Par"

def test_numero_impar():
    """Prueba que la función retorne 'Impar' para un número impar."""
    assert clasificar_numero(7) == "Impar"

def test_numero_cero():
    """Prueba que el número cero sea clasificado como 'Par'."""
    assert clasificar_numero(0) == "Neutro"

def test_numero_negativo_par():
    """Prueba que un número par negativo sea clasificado como 'Par'."""
    assert clasificar_numero(-10) == "Par"

def test_numero_negativo_impar():
    """Prueba que un número impar negativo sea clasificado como 'Impar'."""
    assert clasificar_numero(-3) == "Impar"
