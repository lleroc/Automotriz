class clase_recetas:
    def __init__(self, nombre, ingredientes=None, preparacion=None, RestauranteId=None, 
                 clienteId=None):
        self.nombre = nombre
        if ingredientes is None:
            self.ingredientes = []
        else:
            self.ingredientes = ingredientes
        if preparacion is None:
            self.preparacion = []
        else:
            self.preparacion = preparacion
        self.RestauranteId = RestauranteId
        self.clienteId = clienteId

    def agregar_ingredientes(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def agregar_preparacion(self, preparacion):
        self.preparacion.append(preparacion)

    def mostrar_receta(self):
        print("Nombre: ", self.nombre)
        print("Ingredientes: ", self.ingredientes)
        print("Preparación: ", self.preparacion)

    def asignar_restaurante(self, RestauranteId):
        self.RestauranteId = RestauranteId

    def agregar_cliente(self, clienteId):
        self.clienteId = clienteId
    
    def __str__(self):
        return f"Receta: {self.nombre} Ingredientes: {self.ingredientes}  Preparación: {self.preparacion}  RestauranteId: {self.RestauranteId}  ClienteId: {self.clienteId}"