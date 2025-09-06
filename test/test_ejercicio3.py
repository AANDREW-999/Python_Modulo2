"""
Pruebas unitarias para el Ejercicio 3: Validador de Contraseñas.

Verifica la lógica de la función validar_contrasena con diferentes casos.
"""
import pytest
from bloque1_logica_condicional_avanzada_y_bucles.ejercicio3 import validar_contrasena

def test_contrasena_completamente_valida():
    """Prueba que una contraseña que cumple todas las reglas retorne True."""
    assert validar_contrasena("ContrasenaSegura123") is True

# --- Pruebas para cada regla de error (deben lanzar excepciones) ---

def test_contrasena_muy_corta_lanza_excepcion():
    """Prueba que una contraseña con menos de 8 caracteres lance ValueError."""
    with pytest.raises(ValueError, match="debe tener al menos 8 caracteres"):
        validar_contrasena("Clave1")

def test_contrasena_sin_mayuscula_lanza_excepcion():
    """Prueba que una contraseña sin mayúsculas lance ValueError."""
    with pytest.raises(ValueError, match="debe contener al menos una letra mayúscula"):
        validar_contrasena("clavesegura123")

def test_contrasena_sin_numero_lanza_excepcion():
    """Prueba que una contraseña sin números lance ValueError."""
    with pytest.raises(ValueError, match="debe contener al menos un número"):
        validar_contrasena("ClaveSeguraTotal")

def test_contrasena_vacia_lanza_excepcion():
    """Prueba que una contraseña vacía lance ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacía"):
        validar_contrasena("")

def test_contrasena_solo_espacios_lanza_excepcion():
    """Prueba que una contraseña con solo espacios lance ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacía"):
        validar_contrasena("        ")