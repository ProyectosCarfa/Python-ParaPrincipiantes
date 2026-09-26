# Día 50 — `reduce()` en Python

> Serie: Python desde 0
> Tema: Combinar datos con `reduce()`
> Conceptos: `reduce()` · `lambda` · listas · `map()` · `filter()`

---

## ¿Qué aprenderemos?

En esta lección aprenderemos a utilizar la función `reduce()` de Python para **combinar varios elementos y obtener un solo resultado**.

En las lecciones anteriores aprendimos:

```text
map()
  ↓
Transforma elementos

filter()
  ↓
Selecciona elementos

reduce()
  ↓
Combina elementos
  ↓
Un solo resultado
````

Al finalizar la lección podrás:

* ✓ Entender qué hace `reduce()`.
* ✓ Importar `reduce()` desde `functools`.
* ✓ Utilizar `reduce()` con `lambda`.
* ✓ Sumar los elementos de una lista.
* ✓ Multiplicar los elementos de una lista.
* ✓ Entender cómo `reduce()` combina los valores.
* ✓ Utilizar `reduce()` junto con `filter()`.
* ✓ Diferenciar `map()`, `filter()` y `reduce()`.

---

## Contenido

1. [¿Qué es `reduce()`?](#1-qué-es-reduce)
2. [Importar `reduce()`](#2-importar-reduce)
3. [Sintaxis de `reduce()`](#3-sintaxis-de-reduce)
4. [¿Cómo funciona `reduce()`?](#4-cómo-funciona-reduce)
5. [¿Qué significa `lambda a, b`?](#5-qué-significa-lambda-a-b)
6. [Sumar elementos](#6-sumar-elementos)
7. [Multiplicar elementos](#7-multiplicar-elementos)
8. [Ejemplo con precios](#8-ejemplo-con-precios)
9. [`reduce()` con otras operaciones](#9-reduce-con-otras-operaciones)
10. [`map()`, `filter()` y `reduce()`](#10-map-filter-y-reduce)
11. [`filter()` + `reduce()`](#11-filter--reduce)
12. [Programa completo](#12-programa-completo)
13. [¿Qué aprendimos?](#13-qué-aprendimos)
14. [Reto](#reto)

---

# 1. ¿Qué es `reduce()`?

`reduce()` es una función que permite **combinar varios elementos de una colección hasta obtener un solo resultado**.

Por ejemplo, tenemos:

```python
numeros = [10, 20, 30, 40]
```

Queremos sumar todos los números.

El resultado sería:

```text
10 + 20 + 30 + 40
        ↓
      100
```

Con `reduce()` podemos realizar esta operación de forma progresiva.

### Idea principal

```text
Lista
  │
  ▼
[10, 20, 30, 40]
  │
  ▼
Combinar elementos
  │
  ▼
Un solo resultado
  │
  ▼
100
```

> `reduce()` toma varios elementos y los combina hasta obtener un único resultado.

---

# 2. Importar `reduce()`

A diferencia de `map()` y `filter()`, `reduce()` no está disponible directamente.

Tenemos que importarlo desde `functools`.

```python
from functools import reduce
```

Después podemos utilizarlo:

```python
from functools import reduce

numeros = [10, 20, 30, 40]
```

Ahora nuestro programa ya puede utilizar `reduce()`.

---

# 3. Sintaxis de `reduce()`

La estructura básica es:

```python
reduce(funcion, lista)
```

Por ejemplo:

```python
from functools import reduce

numeros = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numeros)

print(total)
```

### Salida en consola

```text
100
```

En este caso:

```python
lambda a, b: a + b
```

indica la operación que queremos realizar entre los elementos.

---

# 4. ¿Cómo funciona `reduce()`?

Tenemos:

```python
numeros = [10, 20, 30, 40]
```

Y:

```python
total = reduce(lambda a, b: a + b, numeros)
```

Python combina los valores progresivamente.

Primero:

```text
10 + 20
   ↓
  30
```

Después utiliza ese resultado:

```text
30 + 30
   ↓
  60
```

Y finalmente:

```text
60 + 40
   ↓
 100
```

Por lo tanto:

```text
[10, 20, 30, 40]

10 + 20 → 30

30 + 30 → 60

60 + 40 → 100
```

El resultado final es:

```text
100
```

### Visualmente

```text
        [10, 20, 30, 40]
                 │
                 ▼
             10 + 20
                 │
                 ▼
                30
                 │
                 ▼
             30 + 30
                 │
                 ▼
                60
                 │
                 ▼
             60 + 40
                 │
                 ▼
               100
```

---

# 5. ¿Qué significa `lambda a, b`?

Observemos esta parte:

```python
lambda a, b: a + b
```

Tenemos dos valores:

```text
a → primer valor
b → segundo valor
```

Y después indicamos qué queremos hacer:

```python
a + b
```

Por ejemplo:

```text
a = 10
b = 20

10 + 20
   ↓
  30
```

Después `reduce()` utiliza ese resultado para continuar con el siguiente elemento.

### Podemos verlo así

```text
lambda a, b: a + b
      │  │       │
      │  │       └── Operación
      │  │
      │  └── Segundo valor
      │
      └── Primer valor
```

La operación puede cambiar.

Por ejemplo:

```python
lambda a, b: a + b
```

suma.

Mientras que:

```python
lambda a, b: a * b
```

multiplica.

---

# 6. Sumar elementos

Uno de los usos más sencillos de `reduce()` es sumar todos los elementos de una lista.

```python
from functools import reduce

numeros = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numeros)

print(total)
```

### Salida en consola

```text
100
```

El proceso es:

```text
10 + 20 → 30
30 + 30 → 60
60 + 40 → 100
```

Por eso obtenemos:

```text
100
```

---

# 7. Multiplicar elementos

También podemos utilizar `reduce()` para multiplicar.

Tenemos:

```python
numeros = [2, 3, 4]
```

Utilizamos:

```python
from functools import reduce

numeros = [2, 3, 4]

resultado = reduce(lambda a, b: a * b, numeros)

print(resultado)
```

### Proceso

```text
2 × 3
  ↓
  6

6 × 4
  ↓
 24
```

### Salida en consola

```text
24
```

Aquí cambiamos:

```python
a + b
```

por:

```python
a * b
```

Por lo tanto:

```text
+ → suma
* → multiplicación
```

---

# 8. Ejemplo con precios

Ahora vamos a utilizar una situación más parecida a un programa real.

Tenemos los precios de varios productos:

```python
precios = [50, 80, 120, 100]
```

Queremos obtener el total de todos los precios.

Podemos utilizar:

```python
from functools import reduce

precios = [50, 80, 120, 100]

total = reduce(lambda a, b: a + b, precios)

print(f"Total de la compra: S/. {total}")
```

### Salida en consola

```text
Total de la compra: S/. 350
```

### ¿Qué ocurrió?

Python hizo:

```text
50 + 80
   ↓
 130

130 + 120
    ↓
  250

250 + 100
    ↓
  350
```

Por lo tanto:

```text
Total de la compra: S/. 350
```

Aquí estamos tomando varios precios:

```text
[50, 80, 120, 100]
```

y convirtiéndolos en un único resultado:

```text
350
```

---

# 9. `reduce()` con otras operaciones

La operación que realiza `reduce()` depende de lo que coloquemos en `lambda`.

### Sumar

```python
reduce(lambda a, b: a + b, numeros)
```

Resultado:

```text
10 + 20 + 30
```

### Multiplicar

```python
reduce(lambda a, b: a * b, numeros)
```

Resultado:

```text
10 × 20 × 30
```

También podemos utilizar condiciones.

Por ejemplo, podemos utilizar `reduce()` para encontrar el número mayor:

```python
from functools import reduce

numeros = [15, 80, 42, 100, 35]

mayor = reduce(
    lambda a, b: a if a > b else b,
    numeros
)

print(mayor)
```

### Salida

```text
100
```

En este caso, `reduce()` va comparando los valores.

```text
15 vs 80
   ↓
80

80 vs 42
   ↓
80

80 vs 100
   ↓
100

100 vs 35
    ↓
100
```

El resultado final es:

```text
100
```

---

# 10. `map()`, `filter()` y `reduce()`

Ahora tenemos tres herramientas diferentes.

```text
map()
  ↓
Transforma

filter()
  ↓
Selecciona

reduce()
  ↓
Combina
```

## `map()`

`map()` se utiliza para transformar los elementos.

Por ejemplo:

```python
numeros = [10, 20, 30]

resultado = list(
    map(lambda numero: numero * 2, numeros)
)

print(resultado)
```

Salida:

```text
[20, 40, 60]
```

Los elementos fueron transformados.

---

## `filter()`

`filter()` se utiliza para seleccionar los elementos que cumplen una condición.

```python
numeros = [10, 20, 30, 40]

resultado = list(
    filter(lambda numero: numero > 20, numeros)
)

print(resultado)
```

Salida:

```text
[30, 40]
```

Los elementos no fueron modificados.

Simplemente seleccionamos algunos.

---

## `reduce()`

`reduce()` combina los elementos hasta obtener un solo resultado.

```python
from functools import reduce

numeros = [10, 20, 30, 40]

resultado = reduce(
    lambda a, b: a + b,
    numeros
)

print(resultado)
```

Salida:

```text
100
```

### Diferencia principal

```text
┌──────────┬────────────────────────────┐
│ Función  │ ¿Qué hace?                 │
├──────────┼────────────────────────────┤
│ map()    │ Transforma elementos       │
│ filter() │ Selecciona elementos       │
│ reduce() │ Combina elementos          │
└──────────┴────────────────────────────┘
```

---

# 11. `filter()` + `reduce()`

También podemos combinar lo aprendido en las lecciones anteriores.

Supongamos que tenemos:

```python
precios = [50, 120, 80, 200, 150]
```

Primero podemos utilizar `filter()` para obtener únicamente los precios mayores a `100`.

```python
precios_filtrados = list(
    filter(lambda precio: precio > 100, precios)
)
```

El resultado será:

```text
[120, 200, 150]
```

Ahora podemos utilizar `reduce()` para sumar esos precios:

```python
from functools import reduce

total = reduce(
    lambda a, b: a + b,
    precios_filtrados
)

print(total)
```

### Salida

```text
470
```

### Proceso completo

```text
PRECIOS
[50, 120, 80, 200, 150]
          │
          ▼
       filter()
          │
          │ precio > 100
          ▼
[120, 200, 150]
          │
          ▼
       reduce()
          │
          │ suma
          ▼
         470
```

Aquí estamos utilizando dos herramientas con diferentes objetivos:

```text
filter()
→ selecciona

reduce()
→ combina
```

---

# 12. Programa completo

Ahora vamos a juntar lo aprendido en un pequeño programa.

El usuario podrá ingresar varios precios.

Después:

```text
1. Guardamos los precios.
2. Mostramos los precios.
3. Utilizamos filter().
4. Mostramos los precios filtrados.
5. Utilizamos reduce().
6. Obtenemos el total.
```

```python
from functools import reduce

precios = []

cantidad = int(input("¿Cuántos productos deseas registrar?: "))

for i in range(cantidad):
    print(f"\nProducto {i + 1}")

    precio = float(input("Precio: S/. "))

    precios.append(precio)

print("\nPrecios registrados:")

for precio in precios:
    print(f"- S/. {precio:.2f}")

precios_filtrados = list(
    filter(
        lambda precio: precio > 100,
        precios
    )
)

print("\nProductos mayores a S/. 100:")

for precio in precios_filtrados:
    print(f"- S/. {precio:.2f}")

if precios_filtrados:
    total = reduce(
        lambda a, b: a + b,
        precios_filtrados
    )

    print(f"\nTotal de productos mayores a S/. 100: S/. {total:.2f}")
else:
    print("\nNo hay productos mayores a S/. 100.")
```

### Salida de ejemplo

```text
¿Cuántos productos deseas registrar?: 5

Producto 1
Precio: S/. 50

Producto 2
Precio: S/. 120

Producto 3
Precio: S/. 80

Producto 4
Precio: S/. 200

Producto 5
Precio: S/. 150

Precios registrados:
- S/. 50.00
- S/. 120.00
- S/. 80.00
- S/. 200.00
- S/. 150.00

Productos mayores a S/. 100:
- S/. 120.00
- S/. 200.00
- S/. 150.00

Total de productos mayores a S/. 100: S/. 470.00
```

### ¿Qué está haciendo el programa?

```text
                 PRECIOS
                    │
                    ▼
             [50, 120, 80,
              200, 150]
                    │
                    ▼
                filter()
                    │
                    │ > 100
                    ▼
             [120, 200, 150]
                    │
                    ▼
                reduce()
                    │
                    │ +
                    ▼
                   470
```

---

# 13. ¿Qué aprendimos?

En esta lección aprendimos que:

```python
reduce()
```

nos permite **combinar varios elementos hasta obtener un solo resultado**.

Una estructura común es:

```python
from functools import reduce

resultado = reduce(
    lambda a, b: operacion,
    lista
)
```

Por ejemplo:

```python
from functools import reduce

numeros = [10, 20, 30, 40]

total = reduce(
    lambda a, b: a + b,
    numeros
)

print(total)
```

### Salida

```text
100
```

### Diferencia entre las tres funciones

```text
┌──────────┬────────────────────────────┐
│ Función  │ ¿Qué hace?                 │
├──────────┼────────────────────────────┤
│ map()    │ Transforma datos            │
│ filter() │ Selecciona datos            │
│ reduce() │ Combina datos               │
└──────────┴────────────────────────────┘
```

Una forma sencilla de recordarlo:

```text
map()
  ↓
transforma

filter()
  ↓
selecciona

reduce()
  ↓
combina
```

---

# Reto

Tenemos la siguiente lista:

```python
precios = [30, 80, 120, 40, 100]
```

## Objetivo

Utiliza `filter()` para obtener solamente los precios mayores a `50`.

Después utiliza `reduce()` para sumar los precios filtrados.

El resultado esperado es:

```text
Precios mayores a S/. 50:
[80, 120, 100]

Total:
S/. 300
```

### Pistas

Primero necesitarás:

```python
filter()
```

y:

```python
lambda
```

La condición deberá comprobar:

```python
precio > 50
```

Después necesitarás:

```python
reduce()
```

para combinar los precios filtrados.

La operación será:

```python
a + b
```

---

# Resumen

```text
                       REDUCE()
                          │
                          ▼
                 Recibe varios valores
                          │
                          ▼
                 Combina los elementos
                          │
                          ▼
                    Un resultado
                          │
                          ▼
                         100
```

Ejemplo:

```python
from functools import reduce

numeros = [10, 20, 30, 40]

resultado = reduce(
    lambda a, b: a + b,
    numeros
)

print(resultado)
```

Salida:

```text
100
```

Y recuerda:

```text
map()    → transforma datos
filter() → selecciona datos
reduce() → combina datos
```

> `reduce()` es útil cuando necesitamos tomar varios valores y convertirlos en un único resultado.

**Día 50 completado.**

