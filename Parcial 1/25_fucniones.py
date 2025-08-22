#Diseña un sistema para manejar reservas de un hotel. 
#Cada fila será: [ID, NombreCliente, Habitación, Noches].

#crear_reserva() → registra una nueva reserva.
#listar_reservas() → imprime todas las reservas.
#actualizar_reserva() → cambia el número de noches de una reserva existente.
#eliminar_reserva() → elimina la reserva según el ID.
lista_reservas = []
id = 1
def crear_reserva ():
    global id
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    habitacion = input("Ingrese el numero de habitacion: ")
    noches = int(input("Ingrese el numero de noches: "))
    reserva = {
        "id": id,
        "nombre_cliente":nombre_cliente,
        "habitacion":habitacion,
        "noches":noches
    }
    lista_reservas.append(reserva)
    id +=1
    print("Se ingreso con exito")
    print("-" * 50)

def listar_reservas():
    for fila in lista_reservas:
        for clave, valor in fila.items():
            print(f"{(clave.upper())} : {valor}", end=" ")
        print("")
    
def actualizar_reserva(id):
    for fila in lista_reservas:
        for clave, valor in fila.items():
            if clave == "id" and valor == id:
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                habitacion = input("Ingrese el numero de habitacion: ")
                noches = int(input("Ingrese el numero de noches: "))
            else:
                contador = 1
    if contador == 1:
        print("No se pudo actualizar el registro")
        return ""
    else:
        lista_reservas[id]["nombre_cliente"] = nombre_cliente
        lista_reservas[id]["habitacion"] = habitacion
        lista_reservas[id]["noches"] = noches

        print("Se ingreso con exito")
        print("-" * 50)

def eliminar_reserva(id):
    reserva_elimana = lista_reservas.pop(id)
    print(f"La reserav se elimno con exxito: {reserva_elimana}")


while True:
    print("Sistema de Reservas")
    print("1. Ingresar reserva")
    print("2. Listar reservas")
    print("3. Actualizar reserva")
    print("4. Eliminar reserva")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        crear_reserva()
    elif opcion == 2:
        listar_reservas()
    elif opcion == 3:
        listar_reservas()
        id_reserva = int(input("Ingrese el ID de la reserva: "))
        actualizar_reserva(id_reserva)
    elif opcion == 4:
        listar_reservas()
        id_reserva = int(input("Ingrese el ID de la reserva: "))
        eliminar_reserva(id_reserva)
    elif opcion == 5:
        print("Gracias por ingresar")
        break
    else:
        print("Opcion no valida")


