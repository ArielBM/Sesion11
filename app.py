from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "<H1>BIENVENIDOS ESTUDIANTES DE IPC1</H1>"


@app.route("/saludar")
def saludar():
    return "<H1>HOLA</H1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5001, debug=True)

