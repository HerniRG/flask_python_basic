from flask import Flask

app = Flask(__name__)

@app.route('/')
def indice():
    return 'Hola, Mundo!'

@app.route("/adios")
def adios():
    return 'Adios'
