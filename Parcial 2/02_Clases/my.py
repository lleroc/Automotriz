from archivo_alumno import clase_alumno
alumno = clase_alumno()
while True:
    print("1.- Crear alumno")
    print("2.- Listar Alumnos")
    print("3.- Salir")
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        direccion = input("Ingrese el direccion: ")
        telefono = input("Ingrese el telefono: ")
        alumno = clase_alumno(nombre, apellido, direccion, telefono)
        alumno.crear_alumno()
    elif opcion == 2:
        alumno.todos_alumnos()
    elif opcion == 3:
        break



