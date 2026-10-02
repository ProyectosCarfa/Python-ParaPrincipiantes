from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "func_web_2026_pro"

LECCIONES = [
    {
        "id": 1,
        "icono": "def",
        "titulo": "Estructura básica de def",
        "descripcion": "Aprende a declarar tu primera función en Python",
        "ruta": "funciones"
    },
    {
        "id": 2,
        "icono": "( )",
        "titulo": "Parámetros y argumentos",
        "descripcion": "Pasa datos a tus funciones para hacerlas flexibles",
        "ruta": "parametros"
    },
    {
        "id": 3,
        "icono": "→",
        "titulo": "Ejemplos prácticos",
        "descripcion": "Funciones listas para usar en tus programas",
        "ruta": "ejemplos"
    },
]

EJEMPLOS = [
    {
        "titulo": "Función sin parámetros",
        "codigo": 'def saludar():\n    print("¡Hola, mundo!")\n\nsaludar()',
        "salida": "¡Hola, mundo!",
        "explicacion": "La función más simple: se define con def, se llama por su nombre."
    },
    {
        "titulo": "Función con un parámetro",
        "codigo": 'def saludar(nombre):\n    print(f"¡Hola, {nombre}!")\n\nsaludar("Ana")',
        "salida": "¡Hola, Ana!",
        "explicacion": "El parámetro 'nombre' permite personalizar la salida cada vez."
    },
    {
        "titulo": "Función con retorno",
        "codigo": 'def sumar(a, b):\n    return a + b\n\nresultado = sumar(3, 5)\nprint(resultado)',
        "salida": "8",
        "explicacion": "return devuelve el resultado para usarlo en otras partes del programa."
    },
    {
        "titulo": "Parámetro con valor por defecto",
        "codigo": 'def saludar(nombre, saludo="Hola"):\n    print(f"{saludo}, {nombre}!")\n\nsaludar("Luis")\nsaludar("Luis", "Buenos días")',
        "salida": "Hola, Luis!\nBuenos días, Luis!",
        "explicacion": "Si no se envía el segundo argumento, se usa 'Hola' por defecto."
    },
]


@app.route("/")
def inicio():
    return render_template("index.html", lecciones=LECCIONES)


@app.route("/funciones")
def funciones():
    return render_template("funciones.html", ejemplos=EJEMPLOS[:2])


@app.route("/parametros")
def parametros():
    return render_template("parametros.html", ejemplos=EJEMPLOS[2:])


@app.route("/ejemplos")
def ejemplos():
    return render_template("ejemplos.html", ejemplos=EJEMPLOS)


if __name__ == "__main__":
    app.run(debug=True, port=5000)