productos = []

cantidad = int(input("¿Cuántos productos deseas registrar?: "))

for i in range(cantidad):
    print(f"\nProducto {i + 1}")

    nombre = input("Nombre: ")
    precio = float(input("Precio: S/. "))

    producto = {
        "nombre": nombre,
        "precio": precio
    }

    productos.append(producto)

print("\nProductos registrados:")

for producto in productos:
    print(f"- {producto['nombre']} - S/. {producto['precio']:.2f}")

# Filtrar productos mayores a 100 soles

productos_filtrados = list(
    filter(
        lambda producto: producto["precio"] > 100,
        productos
    )
)

print("\nProductos mayores a S/. 100:")

if productos_filtrados:
    for producto in productos_filtrados:
        print(f"- {producto['nombre']} - S/. {producto['precio']:.2f}")
else:
    print("No hay productos que cumplan la condición.")

# Aplicar un aumento de 10 soles utilizando map()

precios_actualizados = list(
    map(
        lambda producto: producto["precio"] + 10,
        productos_filtrados
    )
)

print("\nPrecios con aumento de S/. 10:")

for i in range(len(productos_filtrados)):
    nombre = productos_filtrados[i]["nombre"]
    precio = precios_actualizados[i]

    print(f"- {nombre}: S/. {precio:.2f}")