#Realizar un programa que defina un vector llamado “vector_numeros” de 10 enteros, 1
# a continuación lo inicialice con valores aleatorios (del 1 al 10) y posteriormente 
# muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.

import random

vector_numeros = [random.randint(1,10) for _ in range(10)]
for elemento in vector_numeros:
    cuadrodo = elemento ** 2
    cubo = elemento ** 3
    #print(f"Elemento: {elemento}, Cuadrado: {cuadrodo}, Cubo: {cubo}")


#Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector 
# con datos leídos por el teclado. Copia los elementos del vector en otro vector 
# pero en orden inverso, y muéstralo por la pantalla.

vector_inicial = []
for index in range(5):
    vector_inicial.append(input("Ingrese un numero: "))

vector_inverso = []

for index in range(5,0,-1):
    vector_inverso.append(vector_inicial[index-1])

#print(vector_inicial)
#print(vector_inverso)

#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas 
# por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar 
# todas las notas, la nota media, la nota más alta que ha sacado y la menor.

calificaciones = []
for index in range(5):
    while True:
        nota = int(input(f"Ingrese la calificacion #{index + 1} para registrar: "))
        if nota >= 0 and nota <= 10:
            calificaciones.append(nota)
            break
        else:
            print("Nota fuera de rango, por favor ingrese una nota entre 0 y 10")
    
#print(f"El promedio de calificacioens es {sum(calificaciones)/len(calificaciones)}")
#print(f"La nota mas alta es {max(calificaciones)}")
#print(f"La nota mas baja es {min(calificaciones)}")

#Programa que declare un vector de diez elementos enteros y pida números para 
# rellenarlo hasta que se llene el vector o se introduzca un número negativo. 
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

vector = []
while len(vector) < 10:
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        break
    vector.append(numero)
print(vector)
