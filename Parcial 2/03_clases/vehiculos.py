class clase_vehiculo:
    lista_vehiculos = []

    def todos_vehiculos():
        for id, vehiculo in enumerate(clase_vehiculo.lista_vehiculos, start=1):
            print(f"{id}. {vehiculo["placa"]} - {vehiculo["numero_motor"]} - {vehiculo["color"]}")
    
    def crear_vehiculo(numero_motor, numero_chasis,numero_ruedas,color,placa,cilindrage, anio_fabriciacion):
        vehiculo = {
            "numero_motor":numero_motor, 
            "numero_chasis":numero_chasis,
            "numero_ruedas":numero_ruedas,
            "color":color,
            "placa":placa,
            "cilindrage":cilindrage, 
            "anio_fabriciacion":anio_fabriciacion
        }
        clase_vehiculo.lista_vehiculos.append(vehiculo)
        print("Se guardo con exito")
        print("--"*20)
    
    def actualziar_vehiculo(id,numero_motor=None, numero_chasis=None,numero_ruedas=None,color=None,placa=None
                            ,cilindrage=None, anio_fabriciacion=None):
        
        try:
            vehiculo = clase_vehiculo.lista_vehiculos[id - 1]
            if numero_motor:
                vehiculo["numero_motor"] = numero_motor
            if numero_chasis:
                vehiculo["numero_chasis"] = numero_chasis
            if numero_ruedas:
                vehiculo["numero_ruedas"] = numero_ruedas
            if color:
                vehiculo["color"] = color
            if placa:
                vehiculo["placa"] = placa
            if cilindrage:
                vehiculo["cilindrage"] = cilindrage
            if anio_fabriciacion:
                vehiculo["anio_fabriciacion"] = anio_fabriciacion
            print("Se actualizo con exito")
        except IndexError:
            print("El id no existe")

    def eliminar_vehiculo():
        clase_vehiculo.todos_vehiculos()
        id = int(input("Ingrese el id del vehiculo: "))

        try:
            vehiculo = clase_vehiculo.lista_vehiculos.pop(id - 1)
            print(f"El vehiculo de placa {vehiculo["placa"]} se elimino con exito")
        except IndexError:
            print("No existe el vehiculo")









