"""
Ejercicio 9: Transformación de Datos con Dictionary Comprehensions

Versión refactorizada con bloques de validación especializados, incluyendo
una función robusta para validar el formato de los nombres de productos.
"""
from typing import List, Dict, Union

# Constantes
TASA_IVA = 0.19
LIMITE_PRODUCTOS = 50


# --- Bloque 3: Funciones de Validación Especializadas ---

def validar_estructura_lista(productos: List[Dict]):
    """Valida la estructura general de la lista de productos."""
    if not isinstance(productos, list):
        raise TypeError("La entrada debe ser una lista.")
    if not productos:
        raise ValueError("La lista de productos no puede estar vacía.")
    if len(productos) > LIMITE_PRODUCTOS:
        raise ValueError(f"No se pueden procesar más de {LIMITE_PRODUCTOS} productos a la vez.")


def validar_formato_del_nombre(nombre: str):
    """
    Valida que el nombre no esté vacío, no sea solo numérico y no contenga caracteres especiales.
    """
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre del producto no puede ser un texto vacío.")

    nombre_limpio = nombre.strip()
    if nombre_limpio.isdigit():
        raise ValueError(f"El nombre del producto '{nombre_limpio}' no puede ser un número.")

    if not nombre_limpio.replace(" ", "").isalpha():
        raise ValueError("El nombre solo debe contener letras y espacios.")


def validar_formato_del_precio(precio: Union[int, float, str]):
    """
    Valida que el precio sea un número positivo, ya sea entero o decimal.
    """
    try:
        precio_valido = float(precio)
    except (ValueError, TypeError):
        raise ValueError("El precio debe ser un número (entero o decimal).")

    if precio_valido < 0:
        raise ValueError("El precio debe ser un número positivo.")

    return precio_valido


def validar_contenido_productos(productos: List[Dict]):
    """Valida cada producto individual dentro de la lista."""
    nombres_vistos = set()
    for item in productos:
        if not isinstance(item, dict):
            raise TypeError(f"El elemento '{item}' no es un diccionario válido.")
        if 'nombre' not in item or 'precio' not in item:
            raise ValueError(f"El producto '{item}' debe tener las claves 'nombre' y 'precio'.")

        # Validamos el nombre usando la función especializada
        validar_formato_del_nombre(item['nombre'])

        # Validamos el precio usando la función especializada
        validar_formato_del_precio(item['precio'])

        nombre_normalizado = item['nombre'].strip().lower()
        if nombre_normalizado in nombres_vistos:
            raise ValueError(f"El nombre del producto '{item['nombre']}' está duplicado.")
        nombres_vistos.add(nombre_normalizado)


# --- Bloque 2: Función Principal de Lógica (El Director de Orquesta) ---

def procesar_productos(productos: List[Dict]) -> Dict[str, float]:
    """Orquesta la validación y transforma la lista de productos."""
    validar_estructura_lista(productos)
    validar_contenido_productos(productos)

    # Transformación de datos con dictionary comprehension
    return {
        item['nombre'].strip(): round(float(item['precio']) * (1 + TASA_IVA), 2)
        for item in productos
    }


# --- Bloque 1: Interacción con el Usuario ---

def main():
    """Gestiona la entrada del usuario, dando feedback inmediato."""
    print("🛒 Transformador de Productos con IVA 🛒")
    lista_productos = []

    print(f"\nIngrese hasta {LIMITE_PRODUCTOS} productos. Escriba 'fin' en el nombre para terminar.")

    while len(lista_productos) < LIMITE_PRODUCTOS:
        nombre_input = input(f"  - Nombre del producto #{len(lista_productos) + 1}: ").strip()
        if nombre_input.lower() == 'fin':
            break

        try:
            validar_formato_del_nombre(nombre_input)

            while True:
                precio_str = input(f"    Precio de '{nombre_input}': ")
                precio_validado = validar_formato_del_precio(precio_str)
                break

            lista_productos.append({"nombre": nombre_input, "precio": precio_validado})

        except ValueError as e:
            print(f"⚠️ Error: {e}. Intente de nuevo con este producto.")

    # Procesamiento final
    try:
        if not lista_productos:
            print("\nNo se ingresaron productos para procesar.")
            return

        print("\nLista de productos original:")
        for p in lista_productos:
            print(f" - {p['nombre']}: ${p['precio']:,.2f}")

        precios_con_iva = procesar_productos(lista_productos)

        print("\n✅ Diccionario de precios con IVA (19%):")
        for nombre_iva, precio_iva in precios_con_iva.items():
            print(f" - {nombre_iva}: ${precio_iva:,.2f}")

    except (ValueError, TypeError) as e:
        print(f"\n❌ Error de procesamiento final: {e}")


if __name__ == "__main__":
    main()