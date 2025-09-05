"""
Pruebas unitarias para el Ejercicio 1: Sistema de Precios de Entradas de Cine.

Verifica la lógica de la función calcular_precio_entrada con diferentes casos
de edad y estado de estudiante.
"""
from bloque1_logica_condicional_avanzada_y_bucles.ejercicio1 import calcular_precio_entrada

def test_nino_no_estudiante():
    """Prueba el precio para un niño que no es estudiante."""
    assert calcular_precio_entrada(10,'no') == 10000.0

def test_nino_estudiante():
    """Prueba el precio para un niño que es estudiante (con descuento)."""
    assert calcular_precio_entrada(10, 'si') == 9000.0

def test_joven_no_estudiante():
    """Prueba el precio para un joven que no es estudiante."""
    assert calcular_precio_entrada(15, 'no') == 15000.0

def test_joven_estudiante():
    """Prueba el precio para un joven que es estudiante (con descuento)."""
    assert calcular_precio_entrada(15, 'si') == 13500.0

def test_adulto_no_estudiante():
    """Prueba el precio para un adulto que no es estudiante."""
    assert calcular_precio_entrada(30, 'no') == 20000.0

def test_adulto_estudiante():
    """Prueba el precio para un adulto que es estudiante (con descuento)."""
    assert calcular_precio_entrada(30, 'si') == 18000.0

def test_edad_limite_12():
    """Prueba el precio para la edad límite de 12 años."""
    assert calcular_precio_entrada(12, 'no') == 15000.0

def test_edad_limite_18():
    """Prueba el precio para la edad límite de 18 años."""
    assert calcular_precio_entrada(18, 'no') == 20000.0

def test_edad_cero():
    """Prueba el precio para la edad de 0 años."""
    assert calcular_precio_entrada(0, 'no') == 10000.0