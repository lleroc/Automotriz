class clase_profesor:
    def __init__(self, nombre, apellido, edad, profesion, id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion
        self.id = id

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Profesion: {self.profesion}, ID: {self.id}"
    
    def __del__(self):
        print("Se ha eliminado el objeto")