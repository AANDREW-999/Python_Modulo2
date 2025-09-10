"""
Pruebas unitarias para el Ejercicio 12: Simulador de Lanzamiento de Dados.

Verifica las funciones de validación de entrada y la lógica de simulación.
"""
import pytest
import random
from unittest.mock import patch
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio12 import validar_numero_lanzamientos, simular_lanzamientos


# --- Pruebas para la función de validación ---

def test_lanzamientos_validos():
    """Prueba que la función valide correctamente números enteros positivos."""
    assert validar_numero_lanzamientos("100") == 100
    assert validar_numero_lanzamientos("5000") == 5000
    assert validar_numero_lanzamientos("0") == 0


def test_lanzamientos_negativos_lanza_excepcion():
    """Prueba que un número negativo lance una excepción."""
    with pytest.raises(ValueError, match="no puede ser negativo"):
        validar_numero_lanzamientos("-100")


def test_lanzamientos_no_enteros_lanza_excepcion():
    """Prueba que una entrada no numérica o decimal lance una excepción."""
    with pytest.raises(ValueError, match="debe ser un número entero"):
        validar_numero_lanzamientos("abc")
    with pytest.raises(ValueError, match="debe ser un número entero"):
        validar_numero_lanzamientos("100.5")
    with pytest.raises(ValueError, match="debe ser un número entero"):
        validar_numero_lanzamientos("  ")


# --- Pruebas para la función de simulación ---

def test_simular_lanzamientos_con_valores_fijos(monkeypatch):
    """
    Prueba la lógica de simulación con resultados predecibles.

    Se usa monkeypatch para falsificar el comportamiento de random.randint.
    Se simula que el dado1 siempre es 1 y el dado2 siempre es 1.
    """

    def mock_randint(a, b):
        return 1

    monkeypatch.setattr(random, "randint", mock_randint)

    num_lanzamientos = 5
    resultados = simular_lanzamientos(num_lanzamientos)

    # La suma de 1 + 1 es 2, y debe aparecer 5 veces.
    diccionario_esperado = {2: 5}

    assert resultados[2] == diccionario_esperado[2]
    # Se asegura de que no haya otras claves en el diccionario
    assert len(resultados.keys()) == 11
    assert resultados[3] == 0
    assert resultados[12] == 0


def test_simular_lanzamientos_con_multiples_valores_fijos(monkeypatch):
    """
    Prueba la lógica de simulación con una secuencia predecible de resultados.

    Se usa patch para simular una secuencia de llamadas a random.randint.
    """
    # Se simulan 5 lanzamientos:
    # 1. 1, 6 -> suma 7
    # 2. 3, 3 -> suma 6
    # 3. 2, 4 -> suma 6
    # 4. 5, 5 -> suma 10
    # 5. 6, 6 -> suma 12
    valores_simulados = [1, 6, 3, 3, 2, 4, 5, 5, 6, 6]

    with patch("random.randint", side_effect=valores_simulados):
        resultados = simular_lanzamientos(5)

    # Se verifica el resultado de las frecuencias
    assert resultados[7] == 1
    assert resultados[6] == 2
    assert resultados[10] == 1
    assert resultados[12] == 1
    assert resultados[2] == 0
    assert sum(resultados.values()) == 5