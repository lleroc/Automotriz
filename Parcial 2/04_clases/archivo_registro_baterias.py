class clase_registro_bateria:
    lista_registros = []
    def __init__(self, voltaje=None, denominacion=None, marca=None, tiempo_de_uso=None,
                 estado=None,recargable=None):
        self.voltaje = voltaje
        self.denominacion = denominacion
        self.marca = marca
        self.tiempo_de_uso = tiempo_de_uso
        self.estado = estado
        self.recargable = recargable
    
    def agegar_registro(self):
        self.lista_registros.append(self)
    
    def mostrar_registro(self):
        for registros in enumerate(self.lista_registros):
            print("---------------------------------------------------")
            print(f"Registro # {int(registros[0]) + 1} ")
            print(f"Voltaje: {registros[1].voltaje} ")
            print(f"Denominacion: {registros[1].denominacion} ")
            print(f"Marca: {registros[1].marca} ")
            print(f"Tiempo de uso: {registros[1].tiempo_de_uso} ")
            print(f"Estado: {registros[1].estado} ")
            print(f"Recargable: {registros[1].recargable} ")
            print("---------------------------------------------------")
    
    def ingreso_valores(self):
        self.voltaje = input("Ingrese el voltaje de la bateria: ")
        self.denominacion = input("Ingrese la denominacion de la bateria: ")
        self.marca = input("Ingrese la marca de la bateria: ")
        self.tiempo_de_uso = input("Ingrese el tiempo de uso de la bateria: ")
        self.estado = input("Ingrese el estado de la bateria (Nuevo o Usado): ")
        self.recargable = input("Ingrese si la bateria es recargable (Si o No): ")
    
    def actualizar_registro(self):
        self.mostrar_registro()
        registro = int(input("Ingrese el numero del registro a actualizar: "))
        self.lista_registros[registro - 1].voltaje = input("Ingrese el nuevo voltaje de la bateria: ")
        self.lista_registros[registro - 1].denominacion = input("Ingrese la nueva denominacion de la bateria: ")
        self.lista_registros[registro - 1].marca = input("Ingrese la nueva marca de la bateria: ")
        self.lista_registros[registro - 1].tiempo_de_uso = input("Ingrese el nuevo tiempo de uso de la bateria: ")
        self.lista_registros[registro - 1].estado = input("Ingrese el nuevo estado de la bateria (Nuevo o Usado): ")
        self.lista_registros[registro - 1].recargable = input("Ingrese si la nueva bateria es recargable (Si o No): ")
    
    def eliminar_registro(self):
        self.mostrar_registro()
        registro = int(input("Ingrese el numero del registro a eliminar: "))
        self.lista_registros.pop(registro - 1)
        print("Registro eliminado con exito!")

