class clase_alumno:
    def __init__(self, nombre ="", apellido="", direccion="", telefono=""):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.lista_alumnos = []
    
    def crear_alumno(self):
        alumno = {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "direccion":self.direccion,
            "telefono": self.telefono
        }
        self.lista_alumnos.append(alumno)
        print(f"El alumno {self.nombre} {self.apellido} se creo con exito")
    
    def todos_alumnos(self):
        for alumno in self.lista_alumnos:
            print(f"Nombre: {alumno["nombre"]} Apellido: {alumno["apellido"]}")
    
    
    
