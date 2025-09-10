"""
Pruebas unitarias para el Ejercicio 13: Aventura de Texto Simple.

Verifica la lógica de las funciones de juego y la validación de comandos.
"""
import pytest
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio13 import (
    get_habitacion_info,
    validar_comando,
    HABITACIONES
)

# --- Pruebas para get_habitacion_info ---

def test_get_habitacion_info_existente():
    """Prueba que se obtenga la información correcta para una habitación existente."""
    descripcion, movimientos = get_habitacion_info("entrada")
    assert descripcion.startswith("Estás en una mazmorra")
    assert movimientos == {"norte": "sala_tesoro", "sur": "pasillo_sur"}

def test_get_habitacion_info_inexistente():
    """Prueba que se retorne None para una habitación que no existe."""
    info = get_habitacion_info("cuarto_secreto")
    assert info is None

# --- Pruebas para la función de validación de comandos ---

def test_comando_valido_avanza_correctamente():
    """Prueba que un comando válido devuelva la siguiente habitación."""
    proxima_habitacion = validar_comando("entrada", "ir NORTE")
    assert proxima_habitacion == "sala_tesoro"

def test_comando_con_mayusculas_funciona():
    """Prueba que el comando funcione independientemente de las mayúsculas."""
    proxima_habitacion = validar_comando("entrada", "ir NORTE")
    assert proxima_habitacion == "sala_tesoro"

def test_comando_con_espacios_extra_funciona():
    """Prueba que el comando funcione con espacios adicionales."""
    proxima_habitacion = validar_comando("entrada", "  ir   sur  ")
    assert proxima_habitacion == "pasillo_sur"

def test_comando_invalido_lanza_excepcion():
    """Prueba que un comando con formato incorrecto lance ValueError."""
    with pytest.raises(ValueError, match="Comando no válido"):
        validar_comando("entrada", "moverse norte")
    with pytest.raises(ValueError, match="Comando no válido"):
        validar_comando("entrada", "ir")
    with pytest.raises(ValueError, match="Comando no válido"):
        validar_comando("entrada", "ir_norte")

def test_direccion_invalida_lanza_excepcion():
    """Prueba que una dirección no válida lance ValueError."""
    with pytest.raises(ValueError, match="No puedes ir en esa dirección"):
        validar_comando("entrada", "ir este")

def test_comando_en_estado_final_lanza_excepcion():
    """
    Prueba que un comando en una habitación final lance una excepción.
    La validación de la lógica del juego ya se hace en el bucle principal.
    """
    with pytest.raises(ValueError, match="No puedes ir en esa dirección"):
        validar_comando("sala_tesoro", "ir norte")