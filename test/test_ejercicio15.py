"""
Pruebas unitarias para el Ejercicio 15: Batalla Naval Simplificada.
...
Verifica la lógica de las funciones de inicialización, colocación del barco
y validación de coordenadas.
"""
import pytest
import random
from unittest.mock import patch
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio15 import (
    inicializar_tablero,
    colocar_barco,
    validar_coordenada_usuario,
    FILAS,
    COLUMNAS,
    LONGITUD_BARCO,
    SIMBOLO_VACIO,
    SIMBOLO_TOCADO
)


# --- Pruebas para la inicialización y validación del tablero ---

def test_inicializar_tablero():
    """Prueba que el tablero se inicialice con el tamaño correcto."""
    tablero = inicializar_tablero()
    assert len(tablero) == FILAS
    assert all(len(fila) == COLUMNAS for fila in tablero)
    assert all(all(cell == SIMBOLO_VACIO for cell in fila) for fila in tablero)


# --- Pruebas para la colocación del barco ---

@patch('random.randint')
def test_colocar_barco_horizontal(mock_randint):
    """Prueba que el barco se coloque horizontalmente como se espera."""
    # Simula la selección de orientación horizontal (0), fila 2, columna inicial 1
    mock_randint.side_effect = [0, 2, 1]

    barco_esperado = [(2, 1), (2, 2), (2, 3)]
    barco = colocar_barco()

    assert len(barco) == LONGITUD_BARCO
    assert sorted(barco) == sorted(barco_esperado)


@patch('random.randint')
def test_colocar_barco_vertical(mock_randint):
    """Prueba que el barco se coloque verticalmente como se espera."""
    # Simula la selección de orientación vertical (1), columna 3, fila inicial 0
    mock_randint.side_effect = [1, 3, 0]

    barco_esperado = [(0, 3), (1, 3), (2, 3)]
    barco = colocar_barco()

    assert len(barco) == LONGITUD_BARCO
    assert sorted(barco) == sorted(barco_esperado)


# --- Pruebas para la validación de coordenadas del usuario ---

def test_coordenada_valida():
    """Prueba que una coordenada válida sea procesada correctamente."""
    tablero = inicializar_tablero()
    coordenada = "B3"
    assert validar_coordenada_usuario(coordenada, tablero) == (1, 2)


def test_coordenada_con_minisculas_funciona():
    """Prueba que la validación sea insensible a mayúsculas/minúsculas."""
    tablero = inicializar_tablero()
    coordenada = "b3"
    assert validar_coordenada_usuario(coordenada, tablero) == (1, 2)


def test_coordenada_con_espacios_extra_funciona():
    """Prueba que los espacios extra no afecten la validación."""
    tablero = inicializar_tablero()
    coordenada = "  B3  "
    assert validar_coordenada_usuario(coordenada, tablero) == (1, 2)


def test_coordenada_invalida_larga_lanza_excepcion():
    """Prueba que una coordenada con longitud incorrecta lance ValueError."""
    tablero = inicializar_tablero()
    with pytest.raises(ValueError, match="inválida"):
        validar_coordenada_usuario("A12", tablero)
    with pytest.raises(ValueError, match="inválida"):
        validar_coordenada_usuario("A", tablero)


def test_coordenada_fila_fuera_de_rango():
    """Prueba que una fila fuera de rango (ej. F) lance ValueError."""
    tablero = inicializar_tablero()
    with pytest.raises(ValueError, match="fila 'F' está fuera de rango"):
        validar_coordenada_usuario("F1", tablero)


def test_coordenada_columna_fuera_de_rango():
    """Prueba que una columna fuera de rango (ej. 6) lance ValueError."""
    tablero = inicializar_tablero()
    with pytest.raises(ValueError, match="columna '6' está fuera de rango"):
        validar_coordenada_usuario("A6", tablero)


def test_coordenada_con_caracteres_especiales():
    """Prueba que una coordenada con caracteres especiales lance ValueError."""
    tablero = inicializar_tablero()
    with pytest.raises(ValueError, match="La columna debe ser un número"):
        validar_coordenada_usuario("A!", tablero)


def test_coordenada_ya_disparada_lanza_excepcion():
    """Prueba que disparar en una posición ya ocupada lance ValueError."""
    tablero = inicializar_tablero()
    fila, columna = 0, 0
    tablero[fila][columna] = SIMBOLO_TOCADO
    with pytest.raises(ValueError, match="Ya disparaste en esa posición"):
        validar_coordenada_usuario("A1", tablero)