"""
Pruebas unitarias para el Ejercicio 3: Validador de Contraseñas.

Verifica la lógica de la función validar_contrasena con diferentes casos.
"""

from bloque1_logica_condicional_avanzada_y_bucles.ejercicio3 import validar_contrasena

def test_contrasena_valida():
    """Prueba una contraseña que cumple todos los criterios."""
    resultado = validar_contrasena("Contrasena123")
    assert resultado["valida"] is True
    assert not resultado["mensajes"]

def test_contrasena_corta():
    """Prueba una contraseña que no cumple el criterio de longitud."""
    resultado = validar_contrasena("Corta1")
    assert resultado["valida"] is False
    assert "8 caracteres" in resultado["mensajes"][0]


def test_sin_mayusculas():
    """Prueba una contraseña sin letras mayúsculas."""
    resultado = validar_contrasena("contrasena123")
    assert resultado["valida"] is False
    assert "letra mayúscula" in resultado["mensajes"][0]

def test_sin_numero():
    """Prueba una contraseña sin números."""
    resultado = validar_contrasena("ContrasenaSegura")
    assert resultado["valida"] is False
    assert "un número" in resultado["mensajes"][0]

def test_contrasena_vacia():
    """Prueba una cadena de texto vacía."""
    resultado = validar_contrasena("")
    assert resultado["valida"] is False
    assert "8 caracteres" in resultado["mensajes"][0]
    assert "letra mayúscula" in resultado["mensajes"][1]
    assert "un número" in resultado["mensajes"][2]