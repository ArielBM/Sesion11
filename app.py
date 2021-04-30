from datetime import datetime as dt
from flask import Flask, request, render_template
from flask_cors import CORS
from usuario import usuario
from UsuarioController import UsuarioController

mis_usuarios = UsuarioController()
mis_usuarios.crear("Ariel","abautista","1234",1)

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


@app.route("/inicio-sesion",methods=['POST'])
def inicio_sesion():

    if request.method == 'POST':

        user_name = request.json['user_name']
        user_pass = request.json['user_pass']

        mi_usuario = mis_usuarios.login(user_name,user_pass)

        if mi_usuario != None:

            return {

                'status' : 200,
                'info' : mi_usuario

            }

        else: 
            return {
                'status' : 400,
                'info' : 'Usuario no válido'
            }

    return{
        'status' : 500,
        'info' : 'Bad request'
    } 


@app.route("/usuario",methods=['GET','POST','PUT','DELETE'])
def usuario_crear():

    response = {}
    
    if request.method == 'POST':

        nombre = request.json['nombre']
        user_name = request.json['user_name']
        user_pass = request.json['user_pass']
        rol = 2

        new_user = mis_usuarios.crear(nombre,user_name,user_pass,rol)

        if new_user != None:

            response['status'] = 200
            response['info'] = 'Usuario creado correctamente\nID: ' + str(new_user)

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


@app.route("/obtener-usuarios",methods=['GET'])
def obtener_usuarios():

    return {
        'status' : 200,
        'info' : mis_usuarios.retornar_usuarios()
    }

if __name__ == "__main__":
    app.run(threaded=True, port=5001, debug=True)

