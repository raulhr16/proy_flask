from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/buscador', methods=['GET', 'POST'])
def buscador():
    if request.method == 'POST':
        nombre_jugador = request.form['nombre']
        return redirect(url_for('listado', nombre=nombre_jugador))
    return render_template('buscador.html')

@app.route('/listado', methods=['POST'])
def listado():
    ruta_archivo = 'static/js/nba.json'
    with open(ruta_archivo, 'r') as archivo:
        datos_json = json.load(archivo)

    nombre_jugador = request.form.get('cadena', '')
    jugadores = datos_json.get("players", [])
    resultados = []

    for jugador in jugadores:
        if 'name' in jugador and jugador['name'].startswith(nombre_jugador):
            resultados.append(jugador)

    return render_template('listado.html', resultados=resultados)


@app.route('/jugador/<int:id>')
def jugador(id):
    for jugador in jugadores['players']:
        if jugador['tid'] == id:
            return render_template('jugador.html', jugador=jugador)
    return "Jugador no encontrado"

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)


