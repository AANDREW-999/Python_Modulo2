"""
Pruebas unitarias para el Ejercicio 4: Piedra, Papel o Tijeras.
Se prueban las funciones de validación de entrada y de determinación
del ganador de forma independiente.
"""
import pytest
from bloque1_logica_condicional_avanzada_y_bucles.ejercicio4 import validar_eleccion, determinar_ganador

# --- Pruebas para la función de validación ---

def test_elecciones_validas():
    """Prueba que las elecciones correctas se validen y normalicen."""
    assert validar_eleccion("piedra") == "piedra"
    assert validar_eleccion(" PAPEL ") == "papel" # Con espacios
    assert validar_eleccion("Tijeras") == "tijeras" # Con mayúsculas

def test_eleccion_invalida_lanza_excepcion():
    """Prueba que una elección no reconocida lance un ValueError."""
    with pytest.raises(ValueError, match="opción no válida"):
        validar_eleccion("Banano")

def test_eleccion_vacia_lanza_excepcion():
    """Prueba que una cadena vacía o con solo espacios lance un ValueError."""
    with pytest.raises(ValueError, match="opción no válida"):
        validar_eleccion("")
    with pytest.raises(ValueError, match="opción no válida"):
        validar_eleccion("   ")

# --- Pruebas para la lógica del juego ---

@pytest.mark.parametrize("jugador, computadora", [
    ("piedra", "tijeras"),
    ("papel", "piedra"),
    ("tijeras", "papel")
])
def test_jugador_gana(jugador, computadora):
    """Prueba todos los escenarios donde el jugador debe ganar."""
    assert determinar_ganador(jugador, computadora) == "jugador"

@pytest.mark.parametrize("jugador, computadora", [
    ("tijeras", "piedra"),
    ("piedra", "papel"),
    ("papel", "tijeras")
])
def test_computadora_gana(jugador, computadora):
    """Prueba todos los escenarios donde la computadora debe ganar."""
    assert determinar_ganador(jugador, computadora) == "computadora"

@pytest.mark.parametrize("eleccion", ["piedra", "papel", "tijeras"])
def test_empate(eleccion):
    """Prueba que elecciones idénticas resulten en empate."""
    assert determinar_ganador(eleccion, eleccion) == "empate"