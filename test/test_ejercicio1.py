"""
Pruebas unitarias para el Ejercicio 1: Sistema de Precios de Entradas de Cine.

Verifica la lógica de la función calcular_precio_entrada con diferentes casos
de edad y estado de estudiante.
"""
import pytest
from bloque1_logica_condicional_avanzada_y_bucles.ejercicio1 import calcular_precio_entrada

def test_nino_no_estudiante():
    """Prueba el precio para un niño no estudiante."""
    # Menor de 12 años, no estudiante
    assert calcular_precio_entrada("10", "no") == 10000.0
    assert calcular_precio_entrada("11", "no") == 10000.0

def test_nino_estudiante():
    """Prueba el precio para un niño estudiante con descuento."""
    # Menor de 12 años, estudiante (10000 * 0.9 = 9000)
    assert calcular_precio_entrada("8", "si") == 9000.0

def test_joven_no_estudiante():
    """Prueba el precio para un joven no estudiante."""
    # Entre 12 y 17 años, no estudiante
    assert calcular_precio_entrada("15", "no") == 15000.0
    assert calcular_precio_entrada("12", "no") == 15000.0
    assert calcular_precio_entrada("17", "no") == 15000.0

def test_joven_estudiante():
    """Prueba el precio para un joven estudiante con descuento."""
    # Entre 12 y 17 años, estudiante (15000 * 0.9 = 13500)
    assert calcular_precio_entrada("16", "si") == 13500.0

def test_adulto_no_estudiante():
    """Prueba el precio para un adulto no estudiante."""
    # 18 años o más, no estudiante
    assert calcular_precio_entrada("25", "no") == 20000.0
    assert calcular_precio_entrada("18", "no") == 20000.0
    assert calcular_precio_entrada("60", "no") == 20000.0

def test_adulto_estudiante():
    """Prueba el precio para un adulto estudiante con descuento."""
    # 18 años o más, estudiante (20000 * 0.9 = 18000)
    assert calcular_precio_entrada("30", "si") == 18000.0

# --- Pruebas para los casos de error (lanzando excepciones) ---

def test_edad_vacia_lanza_excepcion():
    """Verifica que un campo de edad vacío lance ValueError."""
    with pytest.raises(ValueError, match="edad no puede estar vacío"):
        calcular_precio_entrada("", "si")

def test_estudiante_vacio_lanza_excepcion():
    """Verifica que un campo de estudiante vacío lance ValueError."""
    with pytest.raises(ValueError, match="estudiante no puede estar vacío"):
        calcular_precio_entrada("25", "")

def test_edad_no_numerica_lanza_excepcion():
    """Verifica que una edad no numérica lance ValueError."""
    with pytest.raises(ValueError, match="edad debe ser un número entero"):
        calcular_precio_entrada("veinte", "no")

def test_edad_fuera_de_rango_lanza_excepcion():
    """Verifica que una edad fuera del rango lance ValueError."""
    with pytest.raises(ValueError, match="debe estar entre 0 y 110"):
        calcular_precio_entrada("-5", "no")
    with pytest.raises(ValueError, match="debe estar entre 0 y 110"):
        calcular_precio_entrada("150", "si")

def test_respuesta_estudiante_invalida_lanza_excepcion():
    """Verifica que una respuesta de estudiante no válida lance ValueError."""
    with pytest.raises(ValueError, match="debe ser 'si' o 'no'"):
        calcular_precio_entrada("25", "tal vez")