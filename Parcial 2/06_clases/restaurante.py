class Clase_Restaurante:
    def __init__(self,id, nombre, tipo_cocina):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina

    def __str__(self):
        return f"{self.nombre} es un restaurante de {self.tipo_cocina}"
   