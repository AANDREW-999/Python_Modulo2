"""
Pruebas unitarios para el Ejercicio 2:
Interprete de Comandos Sencillos.

Verifica que la función procesar_comando maneje correctamente los comandos válidos y no válidos.
"""
import pytest
from bloque1_logica_condicional_avanzada_y_bucles.ejercicio2 import procesar_comandos

def test_comando_guardar_valido():
    """Prueba que el comando 'guardar' retorne True."""
    assert procesar_comandos("guardar") is True

def test_comando_cargar_valido():
    """Prueba que el comando 'cargar' retorne True."""
    assert procesar_comandos("cargar") is True

def test_comando_salir_valido():
    """Prueba que el comando 'salir' retorne False para terminar el bucle."""
    assert procesar_comandos("salir") is False

# --- Pruebas de sensibilidad a mayúsculas/minúsculas ---

def test_comandos_con_mayusculas_funcionan():
    """Prueba que los comandos funcionen independientemente de las mayúsculas."""
    assert procesar_comandos("GUARDAR") is True
    assert procesar_comandos("Cargar") is True
    assert procesar_comandos("sAliR") is False

# --- Pruebas para entradas inválidas (deben lanzar excepciones) ---

def test_comando_no_reconocido_lanza_excepcion():
    """Prueba que un comando no válido lance un ValueError."""
    with pytest.raises(ValueError, match="El comando 'ayuda' no es reconocido."):
        procesar_comandos("ayuda")

def test_comando_vacio_lanza_excepcion():
    """Prueba que una cadena vacía lance un ValueError."""
    with pytest.raises(ValueError, match="No se puede dejar el comando vacío."):
        procesar_comandos("")

def test_comando_solo_espacios_lanza_excepcion():
    """Prueba que una cadena con solo espacios lance un ValueError."""
    with pytest.raises(ValueError, match="No se puede dejar el comando vacío."):
        procesar_comandos("   ")