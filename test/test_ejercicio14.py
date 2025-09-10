"""
Pruebas unitarias para el Ejercicio 14: Juego del Ahorcado.

Verifica la lógica de las funciones de validación y de juego.
"""
import pytest
from unittest.mock import patch
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio14 import (
    seleccionar_palabra,
    validar_entrada,
    verificar_victoria,
    PALABRAS_SECRETAS
)


# --- Pruebas para la selección de palabras ---
@patch('random.choice', return_value='test')
def test_seleccionar_palabra(mock_random_choice):
    """
    Prueba que la función seleccione una palabra de la lista.
    Se usa mock para forzar la selección de una palabra específica.
    """
    palabra = seleccionar_palabra()
    assert palabra in PALABRAS_SECRETAS + ['test']  # 'test' es agregado por el mock
    mock_random_choice.assert_called_once_with(PALABRAS_SECRETAS)


# --- Pruebas para la validación de la entrada del usuario ---
def test_entrada_valida():
    """Prueba una letra válida que no se ha intentado."""
    letras_adivinadas = {'a', 'e'}
    assert validar_entrada('o', letras_adivinadas) == 'o'
    assert validar_entrada('O', letras_adivinadas) == 'o'  # Prueba minúscula


def test_entrada_no_letra():
    """Prueba que una entrada no alfabética lance ValueError."""
    with pytest.raises(ValueError, match="una sola letra"):
        validar_entrada('1', set())
    with pytest.raises(ValueError, match="una sola letra"):
        validar_entrada('!', set())


def test_entrada_con_multiples_caracteres():
    """Prueba que una entrada de más de un carácter lance ValueError."""
    with pytest.raises(ValueError, match="una sola letra"):
        validar_entrada('abc', set())


def test_letra_ya_intentada():
    """Prueba que una letra ya intentada lance ValueError."""
    letras_adivinadas = {'a', 'e', 'i'}
    with pytest.raises(ValueError, match="Ya intentaste esa letra"):
        validar_entrada('a', letras_adivinadas)


# --- Pruebas para la verificación de victoria ---
def test_jugador_ha_ganado():
    """Prueba si el jugador ha ganado adivinando todas las letras."""
    palabra_secreta = "juego"
    letras_adivinadas = {'j', 'u', 'e', 'g', 'o'}
    assert verificar_victoria(palabra_secreta, letras_adivinadas) is True


def test_jugador_no_ha_ganado():
    """Prueba si el jugador aún no ha adivinado la palabra completa."""
    palabra_secreta = "juego"
    letras_adivinadas = {'j', 'u', 'e'}
    assert verificar_victoria(palabra_secreta, letras_adivinadas) is False


def test_palabra_con_letras_repetidas():
    """Prueba la lógica con una palabra que tiene letras repetidas."""
    palabra_secreta = "dedo"
    letras_adivinadas = {'d', 'e', 'o'}
    assert verificar_victoria(palabra_secreta, letras_adivinadas) is True