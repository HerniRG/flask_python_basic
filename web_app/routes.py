from web_app import app

@app.route("/")
def indice():
    return "Flask Funciona"

@app.route("/adios")
def adios():
    return "Pues adios"
