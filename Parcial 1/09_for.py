#nombre = "Luis"
#for letra in nombre :
#    print(letra)

#tupla   ()
# vectores / matrcies    []
# diccionarios {} 
#for me sirve para recorrer vectores
#lista_de_numero = (1,2,3,4,5,6,7,8,9,0)
#for numero in lista_de_numero:
#    print(numero)
#contar los caracteres de la variable nombre
nombre = "David Alejandro Atiaja Jacome"
contador = 0
for letra in nombre:
    if letra == " ":
        contador = contador + 0
    else: 
        contador = contador + 1

print(contador)