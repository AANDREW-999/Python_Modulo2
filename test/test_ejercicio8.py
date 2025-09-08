"""
Pruebas unitarias para el Ejercicio 8: Filtrado de Datos.
"""
import pytest
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio8 import analizar_lista_desde_texto


# ... (las pruebas anteriores como test_lista_mixta_valida, etc. siguen aquí)

def test_lista_mixta_valida():
    """Prueba una entrada estándar con números positivos, negativos y cero."""
    entrada = "-5, 10, 0, 20, -25"
    original, positivos, cuadrados, clasificacion = analizar_lista_desde_texto(entrada)

    assert original == [-5, 10, 0, 20, -25]
    assert positivos == [10, 20]
    assert cuadrados == [25, 100, 0, 400, 625]
    assert clasificacion == ["negativo", "positivo", "positivo", "positivo", "negativo"]


# --- Pruebas para entradas inválidas (deben lanzar excepciones) ---

def test_entrada_vacia_lanza_excepcion():
    """Prueba que una cadena vacía o con solo espacios lance ValueError."""
    with pytest.raises(ValueError, match="la entrada no puede estar vacía"):
        analizar_lista_desde_texto("   ")


def test_elemento_no_numerico_lanza_excepcion():
    """Prueba que un elemento no numérico en la lista lance ValueError."""
    with pytest.raises(ValueError, match="el elemento 'tres' no es un número entero válido"):
        analizar_lista_desde_texto("1, 2, tres, 4")


def test_lista_demasiado_larga_lanza_excepcion():
    """
    Prueba que una lista con más de 100 elementos lance ValueError.
    """
    # Creamos una cadena con 101 números (0,1,2,...,100)
    entrada_larga = ",".join(map(str, range(101)))

    with pytest.raises(ValueError, match="la lista excede el límite de 100 números"):
        analizar_lista_desde_texto(entrada_larga)


def test_lista_en_el_limite_es_valida():
    """Verifica que una lista con exactamente 100 elementos sea procesada correctamente."""
    # Creamos una cadena con 100 números (0,1,2,...,99)
    entrada_en_limite = ",".join(map(str, range(100)))

    # Esta llamada no debería lanzar una excepción
    original, _, _, _ = analizar_lista_desde_texto(entrada_en_limite)
    assert len(original) == 100

def test_elemento_con_espacios_extra_es_valido():
    """Prueba que los elementos con espacios extra se manejen correctamente."""
    entrada = "  -3 ,  4 ,  0 ,  15 , -8  "
    original, positivos, cuadrados, clasificacion = analizar_lista_desde_texto(entrada)

    assert original == [-3, 4, 0, 15, -8]
    assert positivos == [4, 15]
    assert cuadrados == [9, 16, 0, 225, 64]
    assert clasificacion == ["negativo", "positivo", "positivo", "positivo", "negativo"]