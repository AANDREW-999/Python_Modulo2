"""
Pruebas unitarias para el Ejercicio 10: Transposición de una Matriz.

Verifica la lógica de las funciones de transposición y de validación
de la matriz.
"""
import pytest
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio10 import (
    validar_matriz,
    transponer_con_bucles,
    transponer_con_comprension
)

# --- Pruebas para la función de validación de la matriz ---
def test_matriz_valida():
    """Prueba que una matriz válida no lance excepción."""
    matriz = [[1, 2], [3, 4]]
    try:
        validar_matriz(matriz)
        assert True
    except:
        assert False, "Una matriz válida no debería lanzar una excepción."

def test_matriz_vacia_lanza_excepcion():
    """Prueba que una matriz vacía lance un ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacía"):
        validar_matriz([])

def test_entrada_no_lista_lanza_excepcion():
    """Prueba que una entrada que no es una lista lance un TypeError."""
    with pytest.raises(TypeError, match="La entrada debe ser una lista"):
        validar_matriz("no es una matriz")

def test_matriz_con_filas_de_diferente_longitud():
    """Prueba que una matriz con filas de diferente longitud lance un ValueError."""
    matriz = [[1, 2], [3, 4, 5]]
    with pytest.raises(ValueError, match="Todas las filas de la matriz deben tener la misma longitud"):
        validar_matriz(matriz)

# --- Pruebas para las funciones de transposición ---
def test_transponer_con_bucles_funciona_correctamente():
    """Prueba la transposición de una matriz con bucles."""
    matriz_original = [[1, 2, 3], [4, 5, 6]]
    matriz_transpuesta_esperada = [[1, 4], [2, 5], [3, 6]]

    validar_matriz(matriz_original)
    assert transponer_con_bucles(matriz_original) == matriz_transpuesta_esperada

def test_transponer_con_comprension_funciona_correctamente():
    """Prueba la transposición de una matriz con list comprehension."""
    matriz_original = [[1, 2], [3, 4], [5, 6]]
    matriz_transpuesta_esperada = [[1, 3, 5], [2, 4, 6]]

    validar_matriz(matriz_original)
    assert transponer_con_comprension(matriz_original) == matriz_transpuesta_esperada