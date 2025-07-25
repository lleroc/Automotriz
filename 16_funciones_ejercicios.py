#1. Calcula el área de un triángulo pidiendo base y altura al usuario.
def area(base, altura):
    print((base * altura)/2)

        #print("Programa para calcular la base y la altura de un triango")
        #base = float(input("Ingrese la base: "))
        #altura = float(input("Ingrese la altura: "))
        #area(base, altura)

#2. Convierte grados Celsius a Fahrenheit con una fórmula simple.
def conversion(temp):
    return (temp * (9/5))+32

        #tem = float(input("Ingrese la temperatura a transofmrar: "))
        #print(f"La temperatura es {conversion(tem)}")

#3. Determina si un número es par o impar.
def numero(num):
    if num%2==0:
        print("Es par")
    else:
        print("Es impar")

                #numero(int(input("Ingrese un numero: ")))

#4. Pide un número al usuario y muestra su tabla de multiplicar (hasta el 10).
def tabla(numero):
    for num in range(1,11):
        print(f"{numero} * {num} = {num * numero}")

#print(tabla(int(input("Ingrese un numero: "))))

#5. Cuenta cuántas vocales hay en una palabra introducida por el usuario.
def palabra(pal):
    contador=0
    for vocal in pal:
        if vocal=="a"or vocal=="e"or vocal=="i" or vocal=="o" or vocal=="u":
            contador=contador+1
    print("el numero de vocales es",contador)
#palabra(input("Ingrese una palabra"))

#6. Solicita dos números y muestra el mayor usando una estructura condicional.
def numeros(numero1,numero2):
    if numero1>numero2:
        print("Es mayor: ", numero1)
    else: 
        print("Es mayor: ", numero2)
#numero1=int(input("Ingrese el primer numero: "))
#numero2=int(input("Ingrese el segundo numero: "))
#numeros(numero1,numero2)

#7. Verifica si una palabra es un palíndromo (como “oso” o “reconocer”).
#8. Simula un cajero automático que permita al usuario depositar, 
# retirar y consultar saldo.
def depositar(dinero, saldo):
    return dinero + saldo
def retirar(dinero, saldo):
    if dinero > saldo:
        return "Saldo Insufiente"
    else:
        return saldo - dinero 
def consultar(saldo):
    return saldo

#saldo = 0
#while True:
#    print("Bienvenido al sistema Bancario")
#    print("1.- Depositar")
#    print("2.- Retirar")
#    print("3.- Consultar")
#    print("4.- Salir")
#    opcion = int(input("Ingrese una opcion: "))
#    if opcion == 1:
#        print("Depositar Dinero")
#        cantidad = float(input("Ingrese el valor a depositar: "))
#        saldo = depositar(cantidad, saldo)
#        print(f"Su saldo es: {saldo}")
#    elif opcion == 2:
#        print("Depositar Dinero")
#        cantidad = float(input("Ingrese el valor a retirar: "))
#        saldo = retirar(cantidad, saldo)
#        print(f"Su saldo es: {saldo}")
#    elif opcion == 2:
#        print("Depositar Dinero")
#        cantidad = float(input("Ingrese el valor a retirar: "))
#        saldo = consultar(saldo)
#        print(f"Su saldo es: {saldo}")
#    else:
#        print("Gracias por participar")
#        break

#9. Solicita una frase y muestra cuántas palabras tiene.
#10. Genera los primeros ‘n’ números de la secuencia Fibonacci, donde ‘n’ lo da el usuario.
#11. Crea una función que calcule el factorial de un número.
#12. Pide una lista de números y muestra solo los números positivos.
#13. Convierte una cadena de texto a minúsculas, mayúsculas y capitaliza.
#14. Simula el juego de adivinar un número entre 1 y 100, con intentos limitados.
#15. Cuenta cuántas veces aparece cada letra en una palabra o frase.


#16. Solicita al usuario su edad y dice en qué año nació.
def fechaNacimiento(edad):
    print(2025-edad)
#edad=int(input("Ingrese su edad: "))
#fechaNacimiento(edad)


#17. Solicita cinco notas y calcula el promedio, indicando si el estudiante 
# aprueba.

def promedio(calificacion):
    return calificacion / 5
def calificacion():
    promedio = 0
    for _ in range(5):
        promedio= promedio + float(input("Ingrese la calificacion: "))
    return promedio
sumacalificacion = 0
while True:
    sumacalificacion= calificacion()
    print(promedio(sumacalificacion))
    opcion = input("Desea ingresar otra vez")
    if opcion.upper() =="NO":
        break
        





#18. Crea una lista con los números del 1 al 10 y multiplícalos por 2 usando bucles.
#19. Simula un generador de contraseñas usando letras, números y símbolos al azar.
#20. Crea una función que determine si un número es primo o no.
