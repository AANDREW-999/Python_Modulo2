"""
Pruebas unitarias para el Ejercicio 6: Analizador de Posiciones de Letras.
"""
import pytest
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio6 import analizar_frase_y_letra

# --- Pruebas para casos válidos ---

def test_encontrar_letra_multiples_veces():
    """Prueba un caso estándar donde la letra aparece varias veces."""
    assert analizar_frase_y_letra("Hola Sena sena", "a") == [4, 8, 12]

def test_busqueda_no_sensible_a_mayusculas():
    """Prueba que la búsqueda funcione con distintas combinaciones de mayúsculas."""
    assert analizar_frase_y_letra("HOLA SENA", "a") == [4, 8]
    assert analizar_frase_y_letra("hola sena", "A") == [4, 8]

def test_letra_no_encontrada():
    """Prueba que devuelva una lista vacía si la letra no está."""
    assert analizar_frase_y_letra("Probando el codigo", "z") == []

def test_frase_con_espacios_extra():
    """Prueba que los espacios extra al inicio/final se manejen bien."""
    assert analizar_frase_y_letra("  espacios extra  ", "e") == [1, 9]

# --- Pruebas para entradas inválidas (deben lanzar excepciones) ---

def test_frase_vacia_lanza_excepcion():
    """Prueba que una frase vacía o con solo espacios lance ValueError."""
    with pytest.raises(ValueError, match="la frase no puede estar vacía"):
        analizar_frase_y_letra("   ", "a")

def test_frase_con_numeros_lanza_excepcion():
    """Prueba que una frase con números lance ValueError."""
    with pytest.raises(ValueError, match="la frase no puede contener números"):
        analizar_frase_y_letra("Sena 123", "s")

def test_letra_vacia_lanza_excepcion():
    """Prueba que una letra vacía lance ValueError."""
    with pytest.raises(ValueError, match="la letra a buscar no puede estar vacía"):
        analizar_frase_y_letra("frase valida", " ")

def test_letra_con_multiples_caracteres_lanza_excepcion():
    """Prueba que una 'letra' con más de un carácter lance ValueError."""
    with pytest.raises(ValueError, match="debe ingresar una sola letra"):
        analizar_frase_y_letra("frase valida", "la")

def test_letra_no_alfabetica_lanza_excepcion():
    """Prueba que una 'letra' que no es del alfabeto (ej. un número) lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un carácter del alfabeto"):
        analizar_frase_y_letra("frase valida", "5")