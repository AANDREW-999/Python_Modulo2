"""
Pruebas unitarias para el Ejercicio 15: Batalla Naval Simplificada.

Verifica la lógica de las funciones de inicialización y conversión de coordenadas.
"""
import pytest
from .main import inicializar_tablero, convertir_coordenadas, FILAS, COLUMNAS

def test_inicializar_tablero():
    """Verifica que el tablero tenga las dimensiones correctas y esté vacío."""
    tablero = inicializar_tablero()
    assert len(tablero) == FILAS
    assert all(len(fila) == COLUMNAS for fila in tablero)
    assert all(all(casilla == "⬜" for casilla in fila) for fila in tablero)

def test_convertir_coordenadas_valida():
    """Prueba la conversión de una coordenada válida (ej. A3)."""
    assert convertir_coordenadas("A3") == (0, 2)
    assert convertir_coordenadas("C5") == (2, 4)
    assert convertir_coordenadas("e1") == (4, 0) # Prueba mayúsculas/minúsculas

def test_convertir_coordenadas_invalida_largo():
    """Prueba una coordenada con un formato de longitud incorrecta."""
    assert convertir_coordenadas("A12") is None
    assert convertir_coordenadas("A") is None

def test_convertir_coordenadas_invalida_rango():
    """Prueba una coordenada fuera de los límites del tablero."""
    assert convertir_coordenadas("A6") is None # Columna fuera de rango
    assert convertir_coordenadas("F1") is None # Fila fuera de rango

def test_convertir_coordenadas_invalida_caracteres():
    """Prueba una coordenada con caracteres no válidos."""
    assert convertir_coordenadas("!1") is None
    assert convertir_coordenadas("A?") is None