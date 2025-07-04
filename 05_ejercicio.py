# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus 
# ingresos mensuales y muestre por pantalla si el usuario tiene que 
# tributar o no.

edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese el valor de sus ingresos: "))
if edad >= 16:
    if ingresos >= 1000:
        print("Usted esta obligado a tributar")
    else:
        print("Usted no cumple con el requisito de ingresos para tributar")
else:
    print("Usted no cumple con la edad para tributar")