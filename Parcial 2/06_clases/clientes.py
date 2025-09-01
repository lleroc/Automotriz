class clase_clientes:
    def __init__(self, nombre, apellido, cedula, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Cedula: {self.cedula}, Telefono: {self.telefono}, Direccion: {self.direccion}"

    