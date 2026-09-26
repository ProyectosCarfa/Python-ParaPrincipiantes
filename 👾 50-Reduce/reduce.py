from functools import reduce

precios = []

cantidad = int(input("¿Cuántos productos deseas registrar?: "))

for i in range(cantidad):
    print(f"\nProducto {i + 1}")

    nombre = input("Nombre: ")
    precio = float(input("Precio: S/. "))

    producto = {
        "nombre": nombre,
        "precio": precio
    }

    precios.append(producto)

print("\nProductos registrados:")

for producto in precios:
    print(f"- {producto['nombre']} - S/. {producto['precio']:.2f}")

productos_filtrados = list(
    filter(
        lambda producto: producto["precio"] > 100,
        precios
    )
)

print("\nProductos mayores a S/. 100:")

if productos_filtrados:
    for producto in productos_filtrados:
        print(f"- {producto['nombre']} - S/. {producto['precio']:.2f}")

    total = reduce(
        lambda a, b: a + b,
        map(lambda producto: producto["precio"], productos_filtrados)
    )

    print(f"\nTotal de los productos filtrados: S/. {total:.2f}")

else:
    print("No hay productos que cumplan la condición.")