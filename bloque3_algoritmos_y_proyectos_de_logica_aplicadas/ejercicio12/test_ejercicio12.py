"""
Pruebas unitarias para el Ejercicio 12: Simulador de Lanzamiento de Dados.

Verifica que la función de simulación genere un diccionario con las sumas
correctas y el número total de lanzamientos esperado.
"""
import pytest
from .main import simular_lanzamientos

def test_claves_diccionario_correctas():
    """Prueba que el diccionario retornado contenga las claves esperadas (2 a 12)."""
    resultados = simular_lanzamientos(100)
    claves_esperadas = set(range(2, 13))
    assert set(resultados.keys()) == claves_esperadas

def test_numero_total_lanzamientos():
    """Prueba que la suma de las frecuencias sea igual al número de lanzamientos."""
    numero_lanzamientos = 500
    resultados = simular_lanzamientos(numero_lanzamientos)
    assert sum(resultados.values()) == numero_lanzamientos

def test_un_solo_lanzamiento():
    """Prueba un solo lanzamiento. El diccionario debe tener una sola entrada."""
    resultados = simular_lanzamientos(1)
    assert len(resultados) == 1
    assert sum(resultados.values()) == 1

def test_lanzamientos_extremos():
    """Prueba si las sumas más improbables (2 y 12) pueden aparecer."""
    # Aunque la probabilidad es baja, en un gran número de lanzamientos
    # deberían aparecer. Esta prueba es menos determinista.
    resultados = simular_lanzamientos(10000)
    assert 2 in resultados
    assert 12 in resultados