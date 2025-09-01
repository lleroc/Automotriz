from archivo_registro_baterias import clase_registro_bateria
while True:
    print("1. Ingresar valores")
    print("2. Mostrar registro")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    registro_bateria = clase_registro_bateria()
    if opcion == 1:
        registro_bateria.ingreso_valores()
        registro_bateria.agegar_registro()
    elif opcion == 2:
        registro_bateria.mostrar_registro()
    elif opcion == 3:
        registro_bateria.actualizar_registro()
    elif opcion == 4:
        registro_bateria.eliminar_registro()
    elif opcion == 5:
        break
    else:
        print("Opción inválida")

 