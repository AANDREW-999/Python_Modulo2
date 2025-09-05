"""
Pruebas unitarias para el Ejercicio 13: Aventura de Texto Simple.

Verifica la lógica de las funciones de habitaciones y decisiones, separándolas
de la interacción con el usuario.
"""
from bloque3_algoritmos_y_proyectos_de_logica_aplicadas.ejercicio13 import get_habitacion_info, manejar_decision

# --- Pruebas para la función get_habitacion_info ---

def test_get_habitacion_info_entrada():
    """Verifica la información de la habitación 'entrada'."""
    descripcion, movimientos = get_habitacion_info("entrada")
    assert "Estás en una mazmorra" in descripcion
    assert movimientos == {"norte": "sala_tesoro", "sur": "pasillo_sur"}

def test_get_habitacion_info_pasillo_sur():
    """Verifica la información del 'pasillo_sur'."""
    descripcion, movimientos = get_habitacion_info("pasillo_sur")
    assert "Es un pasillo largo" in descripcion
    assert movimientos == {"este": "sala_trampa", "oeste": "sala_tesoro"}

def test_get_habitacion_info_sala_tesoro():
    """Verifica la información de la 'sala_tesoro' (estado final)."""
    descripcion, movimientos = get_habitacion_info("sala_tesoro")
    assert "¡Ganaste el juego!" in descripcion
    assert movimientos == {}

def test_get_habitacion_info_habitacion_no_existente():
    """Verifica que devuelva None para una habitación no válida."""
    assert get_habitacion_info("sotano_secreto") is None

# --- Pruebas para la función manejar_decision ---

def test_manejar_decision_movimiento_valido():
    """Verifica que un movimiento válido cambie de habitación."""
    nueva_habitacion = manejar_decision("entrada", "ir norte")
    assert nueva_habitacion == "sala_tesoro"

def test_manejar_decision_movimiento_invalido():
    """Verifica que un movimiento inválido no cambie de habitación."""
    nueva_habitacion = manejar_decision("entrada", "ir este")
    assert nueva_habitacion == "entrada"

def test_manejar_decision_comando_invalido():
    """Verifica que un comando no reconocido no cambie de habitación."""
    nueva_habitacion = manejar_decision("entrada", "abrir puerta")
    assert nueva_habitacion == "entrada"

def test_manejar_decision_desde_estado_final():
    """Verifica que no haya movimientos desde un estado final."""
    nueva_habitacion = manejar_decision("sala_tesoro", "ir sur")
    assert nueva_habitacion == "sala_tesoro"