
# public class Usuario
class usuario:

    # public usuario (int id, String nombre, String user_name, String user_pass)
    def __init__(self, id, nombre, user_name, user_pass, rol):
        
        self.id = id
        self.nombre = nombre
        self.user_name = user_name
        self.user_pass = user_pass
        self.rol = rol

    def autenticar(self, user_name, user_pass):
        
        self.saludar()
        return self.user_name == user_name and self.user_pass == user_pass


    def saludar(self):
        print("hola")


nuevo_usuario = usuario(1,"nombre","user","pass","admin")

print(nuevo_usuario.user_name)
nuevo_usuario.user_name = "user_nuevo"
print(nuevo_usuario.user_name)
        