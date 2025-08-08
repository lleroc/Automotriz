#Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si 
# la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección 
# se considerará válida si contiene el símbolo "@".
def nombre_funcion(email):
    #if "@" in email:
    #    print("El correo es valido")
    #else:
    #    print("El correo no es valido")
    contador = 0
    for letra in email:
        if letra == "@":
           contador +=1
    if contador > 0:
        print("El correo es valido")
    else:
        print("El correo no es valido")
    
print("Validacion de Correo Electronico")
email = input("Ingrese el correo electronico: ")
nombre_funcion(email)  # Llama a la función con el parámetro email

