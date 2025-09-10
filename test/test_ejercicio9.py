"""
Pruebas unitarias para el Ejercicio 9: Transformación de Datos.

Verifica la robustez de las funciones de validación para nombres y precios,
así como la función principal de procesamiento.
"""
import pytest
from bloque2_manipulacion_iterativa_y_herramientas_avanzadas.ejercicio9 import (
    validar_estructura_lista,
    validar_formato_del_nombre,
    validar_formato_del_precio,
    validar_contenido_productos,
    procesar_productos,
    LIMITE_PRODUCTOS
)

# --- Pruebas para validar_formato_del_nombre ---
def test_nombre_valido():
    """Prueba con nombres que solo contienen letras y espacios."""
    validar_formato_del_nombre("Teclado Inalámbrico")
    validar_formato_del_nombre("Laptop")
    assert True # La prueba pasa si no lanza excepción

def test_nombre_vacio():
    """Prueba que un nombre vacío o con solo espacios lance ValueError."""
    with pytest.raises(ValueError, match="no puede ser un texto vacío."):
        validar_formato_del_nombre("")
    with pytest.raises(ValueError, match="no puede ser un texto vacío."):
        validar_formato_del_nombre("   ")

def test_nombre_con_numeros():
    """Prueba que un nombre con números lance ValueError."""
    with pytest.raises(ValueError, match="solo debe contener letras y espacios"):
        validar_formato_del_nombre("Teclado 3.0")

def test_nombre_solo_numeros():
    """Prueba que un nombre que es solo números lance ValueError."""
    with pytest.raises(ValueError, match="no puede ser un número."):
        validar_formato_del_nombre("12345")

def test_nombre_con_caracteres_especiales():
    """Prueba que un nombre con caracteres especiales lance ValueError."""
    with pytest.raises(ValueError, match="solo debe contener letras y espacios"):
        validar_formato_del_nombre("Mouse@")

# --- Pruebas para validar_formato_del_precio ---
def test_precio_valido_entero_y_decimal():
    """Prueba con precios válidos (enteros y decimales)."""
    assert validar_formato_del_precio("15000") == 15000.0
    assert validar_formato_del_precio("19.99") == 19.99

def test_precio_negativo():
    """Prueba que un precio negativo lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un número positivo"):
        validar_formato_del_precio("-10")
    with pytest.raises(ValueError, match="debe ser un número positivo"):
        validar_formato_del_precio("-0.01")

def test_precio_no_numerico():
    """Prueba que una cadena no numérica lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un número"):
        validar_formato_del_precio("abc")

def test_precio_con_caracteres_especiales():
    """Prueba que un precio con caracteres especiales lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un número"):
        validar_formato_del_precio("10$")

def test_precio_vacio():
    """Prueba que una cadena vacía lance ValueError."""
    with pytest.raises(ValueError, match="debe ser un número"):
        validar_formato_del_precio("")

# --- Pruebas para validar_contenido_productos ---
def test_contenido_productos_valido():
    """Prueba una lista de productos con contenido válido."""
    productos = [
        {"nombre": "Laptop", "precio": 1200.00},
        {"nombre": "Mouse", "precio": 25.50}
    ]
    try:
        validar_contenido_productos(productos)
        assert True
    except:
        assert False, "No se esperaba una excepción."

def test_producto_sin_clave():
    """Prueba que un producto sin la clave 'nombre' o 'precio' lance ValueError."""
    productos = [{"nombre": "Laptop"}]
    with pytest.raises(ValueError, match="debe tener las claves 'nombre' y 'precio'"):
        validar_contenido_productos(productos)

def test_producto_duplicado():
    """Prueba que un producto con nombre duplicado lance ValueError."""
    productos = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "laptop", "precio": 1500}
    ]
    with pytest.raises(ValueError, match="está duplicado."):
        validar_contenido_productos(productos)

# --- Pruebas para procesar_productos (integra todas las validaciones) ---
def test_procesar_productos_valido():
    """Prueba que la función principal procese correctamente una lista válida."""
    productos = [
        {"nombre": "Laptop", "precio": 1000},
        {"nombre": "Mouse", "precio": 20},
    ]
    diccionario_esperado = {"Laptop": 1190.00, "Mouse": 23.80}
    assert procesar_productos(productos) == diccionario_esperado

def test_procesar_productos_lista_vacia():
    """Prueba que una lista vacía lance ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacía"):
        procesar_productos([])

def test_procesar_productos_limite_superado():
    """Prueba que una lista que supera el límite lance ValueError."""
    productos = [{"nombre": f"Producto{i}", "precio": 10} for i in range(LIMITE_PRODUCTOS + 1)]
    with pytest.raises(ValueError, match="No se pueden procesar más de"):
        procesar_productos(productos)