"""
Pruebas unitarias para el Ejercicio 5: Clasificador de Números.
Se verifica que la función `analizar_numero` procese correctamente
las entradas válidas y lance excepciones para las inválidas.
"""
import pytest
from bloque1_logica_condicional_avanzada_y_bucles.ejercicio5 import analizar_numero


# --- Pruebas para entradas válidas ---

def test_numero_par_y_multiplo_de_5():
    """Prueba un número par que también es múltiplo de 5."""
    assert analizar_numero("10") == (10, "Par", True)


def test_numero_impar_y_no_multiplo_de_5():
    """Prueba un número impar que no es múltiplo de 5."""
    assert analizar_numero("7") == (7, "Impar", False)


def test_numero_impar_y_multiplo_de_5():
    """Prueba un número impar que es múltiplo de 5."""
    assert analizar_numero("-15") == (-15, "Impar", True)


def test_numero_cero():
    """Prueba el caso especial del número 0."""
    assert analizar_numero("0") == (0, "Neutro", True)


def test_numero_par_negativo():
    """Prueba un número par negativo."""
    assert analizar_numero("-2") == (-2, "Par", False)


# --- Pruebas para entradas inválidas (deben lanzar excepciones) ---

def test_entrada_vacia_lanza_excepcion():
    """Prueba que una cadena vacía o con espacios lance ValueError."""
    with pytest.raises(ValueError, match="la entrada no puede estar vacía"):
        analizar_numero("")
    with pytest.raises(ValueError, match="la entrada no puede estar vacía"):
        analizar_numero("   ")


def test_entrada_no_numerica_lanza_excepcion():
    """Prueba que una cadena no numérica lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un número entero válido"):
        analizar_numero("doce")


def test_entrada_decimal_lanza_excepcion():
    """Prueba que un número decimal lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un número entero válido"):
        analizar_numero("12.5")