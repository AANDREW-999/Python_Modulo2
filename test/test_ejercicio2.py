"""
Pruebas unitarios para el Ejercicio 2:
Interprete de Comandos Sencillos.

Verifica que la función procesar_comando maneje correctamente los comandos válidos y no válidos.
"""

from bloque1_logica_condicional_avanzada_y_bucles.ejercicio2 import procesar_comandos

def test_comando_guardar_valido():
    """Prueba que el comando 'guardar' retorne True"""
    assert procesar_comandos("guardar") is True

def test_comando_cargar_invalido():
    """Prueba que el comando 'cargar' retorne True"""
    assert procesar_comandos("cargar") is True

def test_comando_salir_invalido():
    """Prueba que el comando 'salir' retorne True"""
    assert procesar_comandos("salir") is False

def test_comando_invalido():
    """Prueba que un comando no valido retorne True"""
    assert procesar_comandos('comando_invalido') is True

def test_comando_con_mayusculas():
    """Prueba que los comandos funcionen independiente de las mayúsculas"""
    assert procesar_comandos('GUARDAR') is True
    assert procesar_comandos('CARGAR') is True
    assert procesar_comandos('SALIR') is False