Sí. Para el repositorio queda mejor **sin emojis**, usando símbolos e iconos de texto como `→`, `✓`, `✗`, `│`, `├──`, `└──`, `◆`, `►`, etc.

# Día 49 — `filter()` en Python

> Serie: Python desde 0
> Tema: Filtrar datos con `filter()`
> Conceptos: `filter()` · `lambda` · listas · diccionarios

---

## ¿Qué aprenderemos?

En esta lección aprenderemos a utilizar la función `filter()` de Python para **seleccionar elementos de una lista que cumplen una determinada condición**.

También utilizaremos `lambda`, que nos permitirá escribir esa condición de una forma sencilla.

Al finalizar la lección podrás:

* ✓ Entender qué hace `filter()`.
* ✓ Utilizar `filter()` con listas de números.
* ✓ Utilizar `filter()` junto con `lambda`.
* ✓ Filtrar información almacenada en diccionarios.
* ✓ Convertir el resultado de `filter()` nuevamente en una lista.
* ✓ Diferenciar `map()` de `filter()`.

---

## Contenido

1. [¿Qué es `filter()`?](#1-qué-es-filter)
2. [Sintaxis de `filter()`](#2-sintaxis-de-filter)
3. [¿Cómo funciona `filter()`?](#3-cómo-funciona-filter)
4. [¿Por qué utilizamos `lambda`?](#4-por-qué-utilizamos-lambda)
5. [Convertir el resultado en una lista](#5-convertir-el-resultado-en-una-lista)
6. [Ejemplo con productos](#6-ejemplo-con-productos)
7. [¿Qué significa `producto["precio"]`?](#7-qué-significa-productoprecio)
8. [`filter()` con otra condición](#8-filter-con-otra-condición)
9. [`filter()` con números pares](#9-filter-con-números-pares)
10. [`filter()` vs `map()`](#10-filter-vs-map)
11. [Diferencia visual](#11-diferencia-visual)
12. [Programa completo](#12-programa-completo)
13. [¿Qué aprendimos?](#13-qué-aprendimos)
14. [Reto](#reto)

---

# 1. ¿Qué es `filter()`?

`filter()` es una función incorporada de Python que nos permite **filtrar elementos de una colección**.

Esto significa que podemos recorrer una lista y conservar solamente los elementos que cumplen una condición.

### Ejemplo

Tenemos estos precios:

```python
precios = [50, 120, 80, 200, 150]
```

Supongamos que solamente queremos obtener los precios mayores a `100`.

El resultado que buscamos sería:

```text
[120, 200, 150]
```

Podemos hacerlo utilizando `filter()`.

### Idea principal

```text
Lista completa
      │
      ▼
Se comprueba una condición
      │
      ▼
Solo quedan los elementos que cumplen
```

---

# 2. Sintaxis de `filter()`

La estructura básica es:

```python
filter(condicion, lista)
```

Por ejemplo:

```python
numeros = [50, 120, 80, 200, 150]

resultado = filter(lambda numero: numero > 100, numeros)
```

La condición utilizada es:

```python
lambda numero: numero > 100
```

Esto significa:

> Para cada número, comprueba si es mayor que `100`.

### Descomponiendo la expresión

```text
lambda numero: numero > 100
      │              │
      │              └── Condición
      │
      └── Elemento actual
```

---

# 3. ¿Cómo funciona `filter()`?

Tenemos:

```python
numeros = [50, 120, 80, 200, 150]
```

Y utilizamos:

```python
resultado = filter(lambda numero: numero > 100, numeros)
```

Python analiza cada elemento:

```text
┌──────────┬─────────────────┬───────────┐
│ Número   │ ¿Mayor que 100? │ Resultado │
├──────────┼─────────────────┼───────────┤
│ 50       │ 50 > 100        │ ✗ False   │
│ 120      │ 120 > 100       │ ✓ True    │
│ 80       │ 80 > 100        │ ✗ False   │
│ 200      │ 200 > 100       │ ✓ True    │
│ 150      │ 150 > 100       │ ✓ True    │
└──────────┴─────────────────┴───────────┘
```

Por lo tanto, solamente conserva:

```text
120
200
150
```

Y finalmente obtenemos:

```text
[120, 200, 150]
```

---

# 4. ¿Por qué utilizamos `lambda`?

En este ejemplo:

```python
lambda numero: numero > 100
```

`lambda` nos permite crear una pequeña función directamente dentro de `filter()`.

Podemos entenderla como:

```python
numero > 100
```

La condición devuelve:

```text
True
```

si el número cumple la condición.

O:

```text
False
```

si no la cumple.

### Ejemplo

```text
120 > 100 → True
50 > 100  → False
```

Por lo tanto:

```text
filter()
   │
   ├── True  → ✓ conserva
   │
   └── False → ✗ descarta
```

> `filter()` conserva los elementos cuya condición devuelve `True`.

---

# 5. Convertir el resultado en una lista

Si hacemos:

```python
resultado = filter(lambda numero: numero > 100, numeros)
```

`resultado` no es directamente una lista.

Es un objeto de tipo `filter`.

Por eso, si queremos obtener una lista, utilizamos:

```python
list()
```

### Ejemplo

```python
numeros = [50, 120, 80, 200, 150]

resultado = filter(lambda numero: numero > 100, numeros)

resultado = list(resultado)

print(resultado)
```

### Salida en consola

```text
[120, 200, 150]
```

También podemos hacerlo directamente:

```python
resultado = list(
    filter(lambda numero: numero > 100, numeros)
)

print(resultado)
```

### Salida

```text
[120, 200, 150]
```

---

# 6. Ejemplo con productos

Ahora vamos a utilizar una situación más parecida a un programa real.

Tenemos una lista de productos:

```python
productos = [
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 120},
    {"nombre": "Audifonos", "precio": 150},
    {"nombre": "USB", "precio": 40}
]
```

Queremos obtener solamente los productos que cuestan más de `100` soles.

Podemos utilizar:

```python
productos_caros = list(
    filter(lambda producto: producto["precio"] > 100, productos)
)
```

Ahora tenemos únicamente los productos que cumplen la condición.

Podemos mostrarlos utilizando un `for`:

```python
for producto in productos_caros:
    print(f"{producto['nombre']} - S/. {producto['precio']}")
```

### Salida en consola

```text
Teclado - S/. 120
Audifonos - S/. 150
```

### ¿Qué ocurrió?

```text
PRODUCTOS
   │
   ├── Mouse → S/. 80       ✗
   ├── Teclado → S/. 120    ✓
   ├── Audifonos → S/. 150  ✓
   └── USB → S/. 40         ✗
                             
             │
             ▼
             
     PRODUCTOS FILTRADOS
             │
             ├── Teclado
             └── Audifonos
```

---

# 7. ¿Qué significa `producto["precio"]`?

Cada elemento de nuestra lista es un diccionario.

Por ejemplo:

```python
{
    "nombre": "Mouse",
    "precio": 80
}
```

Para acceder al precio utilizamos:

```python
producto["precio"]
```

Por lo tanto:

```python
lambda producto: producto["precio"] > 100
```

significa:

> Comprueba si el precio del producto es mayor que `100`.

### Podemos verlo así:

```text
producto
   │
   ├── "nombre" → "Mouse"
   │
   └── "precio" → 80
                    │
                    ▼
             producto["precio"]
                    │
                    ▼
                   80
```

---

# 8. `filter()` con otra condición

No solamente podemos buscar precios mayores a `100`.

También podemos utilizar otras condiciones.

### Productos menores a 100

```python
productos_baratos = list(
    filter(lambda producto: producto["precio"] < 100, productos)
)
```

### Productos que cuestan exactamente 120

```python
productos_120 = list(
    filter(lambda producto: producto["precio"] == 120, productos)
)
```

La condición depende de lo que necesitemos buscar.

---

# 9. `filter()` con números pares

También podemos utilizar `filter()` para trabajar con números.

Por ejemplo:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
```

Queremos obtener solamente los números pares.

Podemos utilizar:

```python
pares = list(
    filter(lambda numero: numero % 2 == 0, numeros)
)

print(pares)
```

### Salida en consola

```text
[2, 4, 6, 8]
```

La condición:

```python
numero % 2 == 0
```

comprueba si el número es divisible entre `2`.

### Ejemplo

```text
1 % 2 → 1  ✗
2 % 2 → 0  ✓
3 % 2 → 1  ✗
4 % 2 → 0  ✓
```

Por eso se conservan:

```text
[2, 4, 6, 8]
```

---

# 10. `filter()` vs `map()`

Es importante no confundir estas dos funciones.

## `map()`

`map()` se utiliza principalmente para **transformar elementos**.

Por ejemplo:

```python
precios = [50, 100, 150]

nuevos_precios = list(
    map(lambda precio: precio + 10, precios)
)

print(nuevos_precios)
```

### Salida

```text
[60, 110, 160]
```

Los elementos originales fueron transformados.

---

## `filter()`

`filter()` se utiliza para **seleccionar elementos que cumplen una condición**.

```python
precios = [50, 100, 150, 200]

precios_filtrados = list(
    filter(lambda precio: precio > 100, precios)
)

print(precios_filtrados)
```

### Salida

```text
[150, 200]
```

Los elementos no fueron modificados.

Simplemente seleccionamos algunos.

---

# 11. Diferencia visual

### `map()`

```text
             MAP()
               │
               ▼
       TRANSFORMA ELEMENTOS
               │
               ▼
      [50, 100, 150]
               │
             + 10
               │
               ▼
      [60, 110, 160]
```

### `filter()`

```text
            FILTER()
               │
               ▼
       SELECCIONA ELEMENTOS
               │
               ▼
   [50, 100, 150, 200]
               │
          precio > 100
               │
               ▼
         [150, 200]
```

### Forma sencilla de recordarlo

```text
map()    → transforma
filter() → selecciona
```

---

# 12. Programa completo

Vamos a juntar lo aprendido en un pequeño programa de productos.

```python
productos = [
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Teclado", "precio": 120},
    {"nombre": "Audifonos", "precio": 150},
    {"nombre": "USB", "precio": 40},
    {"nombre": "Monitor", "precio": 500}
]

productos_caros = list(
    filter(lambda producto: producto["precio"] > 100, productos)
)

print("PRODUCTOS MAYORES A S/. 100")
print()

for producto in productos_caros:
    print(f"{producto['nombre']} - S/. {producto['precio']}")
```

### Salida en consola

```text
PRODUCTOS MAYORES A S/. 100

Teclado - S/. 120
Audifonos - S/. 150
Monitor - S/. 500
```

---

# 13. ¿Qué aprendimos?

En esta lección aprendimos que:

```python
filter()
```

nos permite seleccionar elementos que cumplen una condición.

Una estructura común es:

```python
list(
    filter(lambda elemento: condicion, lista)
)
```

Por ejemplo:

```python
numeros = [10, 20, 30, 40, 50]

mayores = list(
    filter(lambda numero: numero > 25, numeros)
)

print(mayores)
```

### Salida

```text
[30, 40, 50]
```

### Diferencia principal

```text
┌──────────┬──────────────────────┐
│ Función  │ ¿Qué hace?           │
├──────────┼──────────────────────┤
│ map()    │ Transforma datos     │
│ filter() │ Filtra datos         │
└──────────┴──────────────────────┘
```

---

# Reto

Tenemos la siguiente lista:

```python
productos = [
    {"nombre": "Laptop", "precio": 2500},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Monitor", "precio": 900},
    {"nombre": "Teclado", "precio": 150},
    {"nombre": "USB", "precio": 40}
]
```

## Objetivo

Utiliza `filter()` para obtener solamente los productos cuyo precio sea mayor a `500`.

El resultado esperado debe contener:

```text
Laptop
Monitor
```

### Pistas

Necesitarás:

```python
filter()
```

y:

```python
lambda
```

La condición deberá comprobar el precio:

```python
producto["precio"]
```

---

# Resumen

```text
                 filter()
                    │
                    ▼
          Recibe una colección
                    │
                    ▼
        Comprueba una condición
                    │
             ┌──────┴──────┐
             ▼             ▼
           True           False
             │             │
             ▼             ▼
        ✓ Conserva     ✗ Descarta
```

Una forma común de utilizarlo:

```python
resultado = list(
    filter(lambda numero: numero > 100, numeros)
)
```

Y recuerda:

```text
map()    → transforma datos
filter() → selecciona datos
```

> `filter()` es especialmente útil cuando necesitamos trabajar con listas y quedarnos solamente con los datos que cumplen determinadas condiciones.

**Día 49 completado.**
