class clase_estudiante:
    def __init__(self, nombre, apellido, edad, carrera, semestre):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
        self.semestre = semestre
        print("Se creo un estudiante")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
    
    def __del__(self):
        print(f"Se elimino el estudiante: {self.nombre}")
        