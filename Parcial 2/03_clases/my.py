from vehiculos import clase_vehiculo

print("Bienvenido al Sistema de Invetario de Vehiculos")
while True:
    print("MENU PRINCIPAL")
    print("1.- Lista de Vehiculos")
    print("2.- Agregar un vehiuclo")
    print("3.- Actualizar informacion de vehiculo")
    print("4.- Eliminar vehiculo")
    print("5.- Salir")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        print("Lista de Vehiculos")
        clase_vehiculo.todos_vehiculos()
    elif opcion == 2:
        print("Ingreso de un Vehiuclo")
        numero_motor = input("Ingrese el numero de motor: ")
        numero_chasis = input("Ingrese el numero de chasis: ")
        numero_ruedas = input("Ingrese el numero de ruedas: ")
        color = input("Ingrese el color: ")
        placa = input("Ingrese la placa: ")
        cilindrage = input("Ingrese el cilindrage: ")
        anio_fabriciacion = input("Ingrese el año de fabricacion: ")
        clase_vehiculo.crear_vehiculo(numero_motor,numero_chasis,numero_ruedas,color, placa,cilindrage,anio_fabriciacion)
    elif opcion == 3:
        print("Actualizar informacion de un Vehiuclo")
        clase_vehiculo.todos_vehiculos()
        id = int(input("Ingrese el numero del vehiculo: "))
        numero_motor = input("Ingrese el numero de motor: ")
        numero_chasis = input("Ingrese el numero de chasis: ")
        numero_ruedas = input("Ingrese el numero de ruedas: ")
        color = input("Ingrese el color: ")
        placa = input("Ingrese la placa: ")
        cilindrage = input("Ingrese el cilindrage: ")
        anio_fabriciacion = input("Ingrese el año de fabricacion: ")
        clase_vehiculo.actualziar_vehiculo(id,numero_motor,numero_chasis,numero_ruedas,color, placa,cilindrage,anio_fabriciacion)
    elif opcion ==4:
        print("Eliminar informacion de un Vehiuclo")
        clase_vehiculo.eliminar_vehiculo()
    elif opcion == 5:
        print("Gracias, programa cerrando")
    else:
        print("Opcion no valida")
        

