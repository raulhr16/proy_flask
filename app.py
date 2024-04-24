from flask import Flask, render_template, request, abort
app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/listado')
def listado():
    return render_template("listado.html")

app.run("0.0.0.0",5000,debug=True)