#Ejercicio 1
#suma de los numero dentro de la lista
#listaNumeros = (3,6,3,45,65,68,34)
#suma = 0
#for numero in listaNumeros:
#    suma = suma + numero
#print(suma)
#Ejercicios 2
#Imprimir los números del 1 al 10 en orden ascendente.
#for numero in range(0,10):
    #print(numero)
#Imprimir los números del 1 al 10 en orden descendente.
#for numero in range(10,0, -1):
#    print(numero)
#Ejercicios 3
#Mostrar los números pares del 2 al 50.
#for numero in range(2,51,2):
#    print(numero)
#Ejercicios 3
#Calcular la suma de los primeros 10 números naturales.
#suma =0
#for numero in range(1,11):
#    suma += numero
#    print(numero)
#print(suma)
#numeros impares
#for numero in range(1,51,2):
#    print(numero)

#Mostrar la tabla de multiplicar del 5 (del 1 al 10).
#tabla = int(input("ingrese el numero de la tabla de multiplicar: "))
#for contador in range(1,13):
#    print(tabla,"*",contador,"=", tabla*contador)
#Leer 10 números y mostrar cuántos son mayores que el promedio de todos.
lista_numeros = []
suma = 0
promedio = 0
contador = 0
for numero in range(0,10):
    lista_numeros.append(input(f"Ingrese el numero {numero + 1}: "))
    suma +=numero
promedio = suma / 10
for numero in lista_numeros:
    if numero > promedio:
        print(f"El numero {numero} es mayor que le promedio")
        contador +=1

print(f"El total de numeros es {contador}")