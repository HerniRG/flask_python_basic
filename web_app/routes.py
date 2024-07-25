from web_app import app
from flask import render_template

@app.route("/")
def indice():
    return render_template("index.html")

@app.route("/adios")
def adios():
    return render_template("adios.html")

@app.route("/peliculas")
def pelis():
    return render_template("peliculas.html")