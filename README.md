# 🐍 Guía de Prácticas de Laboratorio: Python - Módulo 2

---

### **Programa de Formación**
**Tecnólogo en Análisis y Desarrollo de Software**

---

### **Temática**
**Python Módulo 2: Lógica y Control de Flujo** 🧠

Este repositorio contiene la solución a los ejercicios propuestos en el Módulo 2 del curso de Python, centrados en la **lógica de programación, control de flujo y manipulación de datos iterables**. Cada ejercicio está diseñado para reforzar conceptos clave y aplicar buenas prácticas de desarrollo.

---

### **📝 Criterios Esenciales de Entrega**
Para cada ejercicio, es fundamental que se cumplan los siguientes criterios:

* **Git**: Utiliza un solo repositorio. Emplea un archivo `.gitignore` para excluir archivos innecesarios. Realiza **commits descriptivos** por cada ejercicio resuelto.
* **Entorno Virtual**: Gestiona el proyecto con `uv`. Asegúrate de que el archivo `pyproject.toml` esté configurado correctamente para gestionar las dependencias.
* **Pruebas Unitarias**: Crea un archivo de pruebas (`test_*.py`) para cada ejercicio y utiliza **`pytest`** para verificar la funcionalidad de tu código.
* **Documentación**: Todas las funciones deben incluir **`docstrings`** que expliquen su propósito, parámetros y valor de retorno.
* **Validación de Tipos**: Usa **validaciones de tipado** en las firmas de las funciones (`parámetros` y `valor de retorno`) para mejorar la legibilidad y evitar errores.
* **Estilo de Código**: El código debe ser legible y seguir las guías de estilo de **PEP 8**.

---

### **Bloque 1: Lógica Condicional Avanzada y Bucles (Ejercicios 1-5)**
Estos ejercicios se centran en la toma de decisiones complejas y el uso de bucles para validación y repetición controlada.

#### **Ejercicio 1: Sistema de Precios de Entradas de Cine**
Crea un programa que calcule el precio de una entrada de cine.

* **Reglas**:
    * **Niños** (< 12 años): $10.000.
    * **Jóvenes** (12-17 años): $15.000.
    * **Adultos** (≥ 18 años): $20.000.
    * **Estudiantes**: 10% de descuento (independientemente de la edad).
* **Conceptos**: `if/elif/else`, `and`, `or`, `input()`, `int()`, `lower()`, `f-strings`.

#### **Ejercicio 2: Intérprete de Comandos Sencillo**
Simula un menú de consola con `match-case` que procese comandos como "guardar", "cargar" y "salir".

* **Conceptos**: `while`, `match-case`, `input()`, `lower()`.

#### **Ejercicio 3: Validador de Contraseñas**
Valida una contraseña en un bucle `while` hasta que cumpla con los siguientes criterios:

* **Criterios**: Mínimo 8 caracteres, al menos una letra mayúscula y al menos un número.
* **Conceptos**: `while True`, `if/elif/else`, `len()`, métodos de string (`isupper()`, `isdigit()`, etc.), `break`.

#### **Ejercicio 4: Juego de Piedra, Papel o Tijeras**
Implementa el clásico juego contra la computadora. El primero en llegar a 3 victorias gana.

* **Conceptos**: `random.choice()`, bucles `while`, contadores, `if/elif/else`.

#### **Ejercicio 5: Clasificador de Números (Par/Impar con Ternario)**
Clasifica un número como "Par" o "Impar" usando un **operador ternario**.

* **Conceptos**: Operador ternario, operador módulo (`%`), `if`.

---

### **Bloque 2: Manipulación Iterativa y Herramientas Avanzadas (Ejercicios 6-10)**
Estos ejercicios aplican herramientas avanzadas de iteración para escribir código más "Pythónico", conciso y legible.

#### **Ejercicio 6: Analizador de Posiciones de Letras con `enumerate`**
Crea una función que devuelva los índices de todas las apariciones de una letra en una frase.

* **Conceptos**: `funciones`, `enumerate()`, `for`, `list.append()`.

#### **Ejercicio 7: Combinador de Listas con `zip`**
Combina dos listas (nombres y notas) en un diccionario usando `zip()`.

* **Conceptos**: `funciones`, `zip()`, `dict()`, bucle `for` sobre diccionarios.

#### **Ejercicio 8: Filtrado de Datos con `List Comprehensions`**
A partir de una lista de números, usa comprensiones de listas para crear nuevas listas filtradas o transformadas.

* **Conceptos**: `List comprehensions`, operador ternario.

#### **Ejercicio 9: Transformación de Datos con `Dictionary Comprehensions`**
Transforma una lista de diccionarios de productos en un nuevo diccionario usando una comprensión.

* **Conceptos**: `Dictionary comprehensions`.

#### **Ejercicio 10: Transposición de una Matriz**
Crea una función que transpose una matriz (lista de listas).

* **Conceptos**: Listas anidadas, bucles anidados, `list comprehensions` anidadas.

---

### **Bloque 3: Algoritmos y Proyectos de Lógica Aplicada (Ejercicios 11-15)**
Estos ejercicios integran todos los conceptos del módulo para resolver problemas algorítmicos más complejos.

#### **Ejercicio 11: Validador de Cédula (Algoritmo Simple)**
Valida un número de cédula basado en una regla simple: la suma de sus dígitos debe ser un número par.

* **Conceptos**: `funciones`, `while`, `for`, conversión de tipos (`str` a `int`).

#### **Ejercicio 12: Simulador de Lanzamiento de Dados**
Simula el lanzamiento de dos dados 10,000 veces y cuenta la frecuencia de cada posible suma.

* **Conceptos**: `random.randint()`, bucles, diccionarios como contadores, `get()`.

#### **Ejercicio 13: Aventura de Texto Simple**
Diseña un pequeño juego de aventura basado en texto con decisiones y estados.

* **Conceptos**: `while`, `if/elif/else`, `input()`.

#### **Ejercicio 14: Juego del Ahorcado (Hangman)**
Implementa una versión de consola del juego del Ahorcado.

* **Conceptos**: `random.choice()`, listas, manipulación de strings, bucles, `if/else`, funciones.

#### **Ejercicio 15: Proyecto Final - Batalla Naval Simplificada**
Crea una versión del juego "Batalla Naval" en una cuadrícula de 5x5.

* **Conceptos**: Listas anidadas (matrices), `while`, `for`, `if/else`, `random`.
* 