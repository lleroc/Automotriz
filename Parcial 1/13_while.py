# => Solicita números al usuario hasta que ingrese un número negativo. 
# Al final, muestra cuántos números positivos ingresó.
#contador = 0
#while True:
#    numero = int(input("Ingrese un numero: "))
#    if numero < 0:
#        print("Gracias por participar")
#        break
#    else:
#        contador +=1
#print(f"El total de numero positivos es {contador}")


# => Pide al usuario una contraseña hasta que la escriba correctamente. 
# Si se equivoca más de 3 veces, muestra un mensaje de bloqueo.
#pwd = "123"
#contador = 0
#print("Bienvenidos al Sistema")
#while True:
#    contrasenia = input("Ingrese el password: ")
#    if contrasenia == pwd:
#        print("Acceso Exitoso")
#        break
#    else:
#        contador +=1
#        if contador == 3:
#            print("Se bloqueo el accesso, intente mas tarde")
#            break
#        else:
#            print(f"Intento fallido, le quedan {3 - contador}")


# => Lee números enteros hasta que la suma total supere 100. Imprime cuántos 
# números fueron necesarios para alcanzar ese total.

#total = 0
#contador = 0
#while total <= 100:
#    suma = int(input("Ingrese un numero"))
#    total += suma
#    contador +=1

#print(f"El total de numeros ingresados fue: {contador}")

# => Solicita al usuario letras hasta que escriba una vocal. Indica si cada 
# letra es mayúscula o minúscula.

while True:
    letra = input("Ingrese una letra: ")
    if letra.isupper():
        print("La letra es MAYÚSCULA.")
    else:
        print("La letra es minúscula.")

    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Has ingresado una vocal. Fin del programa.")
        break

# => Muestra un menú de opciones (1. Saludar, 2. Despedirse, 3. Salir) y 
# repite hasta que el usuario elija salir.

while True:
    print("Menu de Opciones")
    print("1.- Saludar")
    print("2.- Despedirse")
    print("3.- Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("Hola mundo")
    elif opcion == 2:
        print("Adios mundo")
    elif opcion == 3:
        print("Saliendo del Sistema...")
        break
    else:
        print("Opcion no valida")



# => Solicita nombres al usuario hasta que escriba "FIN". Si el nombre 
# tiene más de 5 letras, imprímelo en mayúsculas.

# => Pide una edad al usuario. Si es menor de 18, dile que no puede 
# continuar y vuelve a preguntar. Solo termina si se ingresa una edad mayor o igual a 18.

# => Pide números hasta que el usuario escriba 0. Luego muestra 
# cuántos de esos números fueron pares.

# => Solicita palabras hasta que el usuario escriba una palabra que 
# comience con la letra “z”. Ignora mayúsculas o minúsculas.

# => Simula un cajero automático: el usuario ingresa un monto inicial, 
# luego puede retirar dinero mientras tenga saldo. Si intenta retirar 
# más de lo disponible, muestra un error.

# => Solicita una lista de calificaciones hasta que se ingrese -1. 
# Muestra la cantidad de notas aprobadas (mayores a 7).

# => Pregunta al usuario un número secreto entre 1 y 10. 
# El programa repite hasta que adivine. Si el número es mayor o menor, 
# indica la pista.

# => Simula una contraseña con 3 intentos. Si se falla, 
# muestra "acceso denegado"; si acierta antes, "acceso concedido".

# => Pide palabras hasta que la longitud total de todas las palabras 
# supere 20 caracteres. Muestra el total acumulado.

# => Solicita al usuario un número entero positivo. Luego imprime los 
# números impares desde 1 hasta ese número usando while e if.

# => Lee números hasta que el usuario escriba uno que sea múltiplo de 5. 
# Muestra cuántos números no múltiplos se ingresaron.

# => Pide una lista de números y acumula la suma solo de los que 
# sean mayores que 50. Termina cuando se ingresa un número negativo.

# => Simula un login pidiendo usuario y contraseña. Solo permite el 
# acceso si ambos son correctos, si no, repite.

# => Solicita números hasta que el usuario escriba dos números 
# consecutivos iguales. Muestra cuántos intentos hizo.

# => Lee números enteros hasta que la suma de los pares y la de los 
# impares sea igual. Al finalizar, muestra ambas sumas.