#Escribir un programa que almacene la cadena de caracteres contraseña en 
# una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

superkey = "123"
contra = input("Ingrese su contraseña: ")
if superkey == contra.lower():
    print("Las contraseñas son correctas")
else:
    print("Las constraseñas no coincides")
