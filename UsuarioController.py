from usuario import usuario
import json

class UsuarioController:

    #CONSTRUCTOR
    def __init__(self):
        self.usuarios = []
        self.contador_id = 0


    #MÉTODO PARA HACER LOGGIN
    def login(self, user_name, user_pass):

        for usr in self.usuarios:

            if usr.autenticar(user_name,user_pass):

                return usr.dump()
        
        return None

        


    #MÉTODO PARA CREAR USUARIOS
    def crear(self, nombre, user_name, user_pass, rol):

        for usr in self.usuarios:

            if usr.user_name == user_name:
                print(f'El nombre de usuario: "{user_name}" ya está en uso.')
                return None
        
        self.usuarios.append(
            usuario(self.contador_id,nombre,user_name,user_pass,rol)
        )
        
        print(f'Se creó al usuario: "{user_name}" con el id: "{self.contador_id}" de forma correcta.')
        self.contador_id += 1

        return self.contador_id-1


    #MÉTODO PARA DEVOLVER UN USUARIO MEDIANTE SU ID
    def devolver_usuario(self, id):
         
        for usr in self.usuarios:

            if usr.id == id:

                return usr.dump()

        return {}


    #MÉTODO PARA ELIMINAR UN USUARIO
    def eliminar(self,id):

        for usr in self.usuarios:

            if usr.id == id:

                print(f'El usuario: "{usr.user_name}" ha sido eliminado con éxito')
                self.usuarios.remove(usr)
                return True

        print(f'El usuario con id: "{ id }" no ha sido encontrado.')
        return False
                


    def listar(self):

        for usr in self.usuarios:

            print(usr)


    def retornar_usuarios(self):

        return json.dumps([usr.dump() for usr in self.usuarios])

