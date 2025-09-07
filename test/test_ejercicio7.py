"""
Pruebas unitarias para el Ejercicio 7: Combinador de Listas con zip.

Verifica la lógica de la función combinar_listas_a_diccionario, incluyendo
la validación de la longitud de las listas.
"""
import pytest
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio7 import combinar_listas_a_diccionario

def test_combinar_listas_longitud_igual():
    """
    Prueba que la función combine correctamente dos listas de igual longitud.
    """
    nombres = ["Ana", "Luis", "Sofía"]
    notas = [4.5, 3.8, 5.0]
    diccionario_esperado = {"Ana": 4.5, "Luis": 3.8, "Sofía": 5.0}
    assert combinar_listas_a_diccionario(nombres, notas) == diccionario_esperado

def test_combinar_listas_vacias():
    """
    Prueba que la función combine correctamente dos listas vacías.
    """
    nombres = []
    notas = []
    diccionario_esperado = {}
    assert combinar_listas_a_diccionario(nombres, notas) == diccionario_esperado

def test_combinar_listas_longitud_diferente_lanza_excepcion():
    """
    Prueba que la función lance un ValueError si las listas tienen
    longitudes diferentes.
    """
    nombres = ["Ana", "Luis", "Sofía"]
    notas = [4.5, 3.8] # Falta un elemento
    with pytest.raises(ValueError, match="misma cantidad de elementos"):
        combinar_listas_a_diccionario(nombres, notas)