#funciones
def suma():  #no regresa nada
    numero1 = int(input("Ingrese el primero numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    print(f"La respuesta es {numero1 + numero2}")

def resta():
    numero1 = int(input("Ingrese el primero numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    respuesta = numero1 - numero2
    print(f"La respuesta es {respuesta}")

def multiplicacion():
    numero1 = int(input("Ingrese el primero numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    respuesta = numero1 * numero2
    print(f"La respuesta es {respuesta}")

def division():
    numero1 = int(input("Ingrese el primero numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    respuesta = numero1 / numero2
    print(f"La respuesta es {respuesta}")

#calculadora
print("Bienvenido a la Calculadora Basica")

while True:
    print("Elija una opcion:")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Division")
    print("5.- Salir")
    opcion = int(input("Ingrese el numero del menu: "))
    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
       division()
    elif opcion == 5:
        print("Gracias por usar la calculadora")
        break
    else:
        print("La opcion ingresada no existe. Intente nuevamente.")

    

