from datetime import datetime as dt
from flask import Flask
from flask_cors import CORS
from models.usuario import usuario

usuario_admin = usuario(0,"Ariel","abautista","1234",1)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "<H1>BIENVENIDOS ESTUDIANTES DE IPC1</H1>"


@app.route("/saludar")
def saludar():
    return "<H1>HOLA</H1>"


@app.route("/datetime")
def datetime():
    now_utc = dt.now()
    return "<H1>" + str(now_utc) + "</H1>"


@app.route("/who-is-admin")
def datetime():
    return "<H1>" + usuario_admin.nombre + " is admin</H1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5001, debug=True)

