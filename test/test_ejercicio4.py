"""
Pruebas unitarias para el Ejercicio 4: Juego de Piedra, Papel o Tijeras.

Verifica la lógica de la función determinar_ganador para todas las posibles
combinaciones de jugadas.
"""

from bloque1_logica_condicional_avanzada_y_bucles.ejercicio4 import determinar_ganador

def test_jugador_gana_con_piedra():
    """Prueba que el jugador gane con piedra contra tijeras."""
    assert determinar_ganador('piedra', 'tijeras') == 'jugador'

def test_jugador_gana_con_papel():
    """Prueba que el jugador gane con papel contra piedra."""
    assert determinar_ganador('papel', 'piedra') == 'jugador'

def test_jugador_gana_con_tijeras():
    """Prueba que el jugador gane con tijeras contra papel."""
    assert determinar_ganador('tijeras', 'papel') == 'jugador'

def test_computadora_gana_con_piedra():
    """Prueba que la computadora gane con piedra contra tijeras."""
    assert determinar_ganador('tijeras', 'piedra') == 'computadora'

def test_computadora_gana_con_papel():
    """Prueba que la computadora gane con papel contra piedra."""
    assert determinar_ganador('piedra', 'papel') == 'computadora'

def test_computadora_gana_con_tijeras():
    """Prueba que la computadora gane con tijeras contra papel."""
    assert determinar_ganador('papel', 'tijeras') == 'computadora'

def test_empate_piedra():
    """Prueba el caso de empate con piedra."""
    assert determinar_ganador('piedra', 'piedra') == 'empate'

def test_empate_papel():
    """Prueba el caso de empate con papel."""
    assert determinar_ganador('papel', 'papel') == 'empate'

def test_empate_tijeras():
    """Prueba el caso de empate con tijeras."""
    assert determinar_ganador('tijeras', 'tijeras') == 'empate'