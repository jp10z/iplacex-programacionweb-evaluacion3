"""Fichero principal del proyecto flask.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio() -> str:
    """Retorna el render de la página de inicio.

    Returns:
        str: Página renderizada.
    """
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET"])
def ejercicio1() -> str:
    """Retorna el render de la página del ejercicio 1.

    Returns:
        str: Página renderizada.
    """
    # retornar template
    return render_template("ejercicio1.html", formulario=["", "", "", ""])

@app.route("/ejercicio1", methods=["POST"])
def ejercicio1_action() -> str:
    """Retorna el render de la página del ejercicio 1.
    Este método se llama como POST y hará el calculo del promedio y lo mostrará
    junto al renderizado.

    Returns:
        str: Página renderizada.
    """
    # obtener valores del formulario
    form = request.form
    nota_1 = form["nota1"]
    nota_2 = form["nota2"]
    nota_3 = form["nota3"]
    asistencia = form["asistencia"]
    formulario = [nota_1, nota_2, nota_3, asistencia]
    # validaciones
    try:
        # que sean numeros
        nota_1 = int(nota_1)
        nota_2 = int(nota_2)
        nota_3 = int(nota_3)
        asistencia = int(asistencia)
        # que estén dentro de sus rangos correctos
        if not (10 <= nota_1 <= 70): raise Exception("Nota fuera de rango")
        if not (10 <= nota_2 <= 70): raise Exception("Nota fuera de rango")
        if not (10 <= nota_3 <= 70): raise Exception("Nota fuera de rango")
        if not (0 <= asistencia <= 100): raise Exception("Asistencia fuera de rango")
    except:
        # respuesta en caso que alguna validacion falle
        respuesta = "Por favor valide que haya escrito correctamente los valores requeridos"
    else:
        # calcular promedio
        promedio = (nota_1 + nota_2 + nota_3) / 3
        if promedio >= 40 and asistencia >= 75:
            respuesta = "APROBADO"
        else:
            respuesta = "REPROBADO"
    # retornar template
    return render_template("ejercicio1.html", promedio=promedio, respuesta=respuesta, formulario=formulario)

@app.route("/ejercicio2")
def ejercicio2() -> str:
    """Retorna el render de la página del ejercicio 2.

    Returns:
        str: Página renderizada.
    """
    # retornar template
    return render_template("ejercicio2.html")

# Inicializar app
if __name__ == '__main__':
    app.run(debug=True)