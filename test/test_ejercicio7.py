"""
Pruebas unitarias para el Ejercicio 7: Combinador de Listas con zip.

Verifica que la función combine correctamente las listas en un diccionario.
"""
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio7 import combinar_listas_a_diccionario

def test_combinacion_basica_correcta():
    """Prueba una combinación estándar de listas."""
    nombres = ["Ana", "Luis"]
    notas = [4.5, 3.8]
    diccionario_esperado = {"Ana": 4.5, "Luis": 3.8}
    assert combinar_listas_a_diccionario(nombres, notas) == diccionario_esperado

def test_listas_vacias():
    """Prueba la combinación de listas vacías."""
    nombres = []
    notas = []
    diccionario_esperado = {}
    assert combinar_listas_a_diccionario(nombres, notas) == diccionario_esperado

def test_listas_con_un_elemento():
    """Prueba la combinación de listas con un solo elemento."""
    nombres = ["Sofía"]
    notas = [5.0]
    diccionario_esperado = {"Sofía": 5.0}
    assert combinar_listas_a_diccionario(nombres, notas) == diccionario_esperado

# Nota: pytest no lanza una excepción si las listas tienen longitudes diferentes
# con la función zip, simplemente se detiene. Por lo tanto, no es necesario
# un test para ese caso, ya que la validación se maneja en la función principal.