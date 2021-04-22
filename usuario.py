
# public class Usuario
class usuario:

    # public usuario (int id, String nombre, String user_name, String user_pass)
    def __init__(self, id, nombre, user_name, user_pass, rol):
        
        self.id = id
        self.nombre = nombre
        self.user_name = user_name
        self.user_pass = user_pass
        self.rol = rol


    def actualizar_datos(self, nombre, user_name, user_pass, rol):
        
        self.nombre = nombre
        self.user_name = user_name
        self.user_pass = user_pass
        self.rol = rol


    def autenticar(self, user_name, user_pass):
        
        return self.user_name == user_name and self.user_pass == user_pass


    def dump(self):
        
        return {

            'id': self.id,
            'nombre': self.nombre,
            'user_name': self.user_name,
            'rol': self.rol
        }

    
    def __str__(self):
     return f'usuario [ id: {self.id}, nombre: {self.nombre}, user_name: {self.user_name}, user_pass: {self.user_pass}, rol: {self.rol}  ]'
