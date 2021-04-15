from datetime import datetime as dt
from flask import Flask, request
from flask_cors import CORS
from usuario import usuario
from UsuarioController import UsuarioController

mis_usuarios = UsuarioController()
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
def who_is_admin():
    return "<H1>" + usuario_admin.nombre + " is admin</H1>"


@app.route("/usuario",methods=['GET','POST','PUT','DELETE'])
def usuario_crear():

    response = {}
    
    if request.method == 'POST':

        nombre = request.form.get('nombre')
        user_name = request.form.get('user_name')
        user_pass = request.form.get('user_pass')
        rol = request.form.get('rol')

        if mis_usuarios.crear(nombre,user_name,user_pass,rol):

            response['stauts'] = 200
            response['info'] = 'Usuario creado correctamente'

        else:

            response['status'] = 400
            response['info'] = 'Ocurrió un error al crear el usuario'

    elif request.method == 'GET':

        id = int(request.args.get("id",None))
        return mis_usuarios.devolver_usuario(id)

    elif request.method == 'DELETE':

        id = int(request.args.get("id",None))
        if mis_usuarios.eliminar(id):

            response['status'] = 200
            response['info'] = 'Usuario eliminado correctamente'

        else:

            response['status'] = 400
            response['info'] = 'Ocurrió un error al elimiar al usuario'


    return response

if __name__ == "__main__":
    app.run(threaded=True, port=5001, debug=True)

