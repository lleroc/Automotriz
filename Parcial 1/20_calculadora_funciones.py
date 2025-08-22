def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "Error, no se puede dividir por cero"
    else:
        return a/b

print("Calculadora Basica y bien Basica")
while True:
    print("Elija una opcion")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Ingrese la opcion que desee: "))

    if opcion == 5:
        print("Hasta luego")
        break

    print("Ingrese el primer valor: ")
    a = float(input())
    print("Ingrese el segundo valor: ")
    b = float(input())
    if opcion == 1:
        print("La suma de los valores es: ", suma(a,b))
    elif opcion == 2:
        print("La resta de los valores es: ", resta(a,b))
    elif opcion == 3:
        print("La multiplicacion de los valores es: ", multiplicacion(a,b))
    elif opcion == 4:
        print("La division de los valores es: ", division(a,b))
    else:
        print("La opcion no es correcta")

    
    






#crear una programa que retorne el calculo del Indice de Masa Corporal.
#Para ello debera crear una funcion que solicite lo valores necesarios
#Formula de IMC
#IMC = peso en kg / altura en metros al cuadrado
def calculo():
    peso = float(input())
    altura = float(input())
    return peso / (altura ** 2)

print("Tu IMC es: ", calculo())