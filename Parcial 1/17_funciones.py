
#1.  Calculadora de Propina: Crea una función llamada `calcular_propina` que reciba 
# el total de una cuenta y un porcentaje de propina. La función debe devolver el monto 
# total a pagar (cuenta + propina). Asegúrate de que el porcentaje de propina tenga 
# un valor por defecto del 15%.

def calcular_propina(total_pagar, propina = 15):
    iva = total_pagar * 0.15
    subtotal = total_pagar + iva
    if propina == 15 or propina == 1:
        valor_propina = subtotal * 0.15
        return (subtotal + valor_propina,subtotal, valor_propina)
    else: 
        valor_propina = (subtotal * propina)/100
        return (subtotal + valor_propina,subtotal, valor_propina)

        #print("Bienvenido al Sistema de Propinas")
        #valor_sin_iva=float(input("Ingrese el valor de pedido: "))
        #print("Opciones de Propina")
        #print("1.- 15%")
        #print("2.- 17%")
        #print("3.- 20%")
        #print("4.- 25%")
        #opcion_propina = int(input("Ingrese la opcion de la propina: "))
        #valores = calcular_propina(valor_sin_iva, opcion_propina)

        #print("Detalle de Pedido")
        #print(f"    Sub Total:  {valores[1]}")
        #print(f"      Propina:  {valores[2]}")
        #print(f"Total a Pagar:  {valores[0]} ")
#2.  Generador de Saludos Personalizados: Diseña una función `saludar` 
# que acepte un nombre y un idioma (`'es'` para español, `'en'` para inglés). 
# La función debe devolver un saludo apropiado (ej. "Hola, [nombre]" o "Hello, [nombre]"). 
# Si el idioma no se especifica, usa español por defecto.

#def saludar(idioma, nombre):
   # if idioma == 1:
   #     return f"Hola, {nombre}"
  #  else:
 #       return f"Hello, {nombre}"

#print(" Generador de Saludos Personalizados ")
#nombre = input("Ingrese su nombre: ")
#print("Elija el idioma:")
#print("1.- Español")
#print("2.- Ingles")
#idioma = int("Ingrese una opcion: ")
#print(saludar(idioma, nombre))
#3.  Contador de Vocales: Escribe una función `contar_vocales` que tome una cadena 
# de texto como argumento y devuelva el número total de vocales 
# (a, e, i, o, u, mayúsculas y minúsculas) en la cadena.
def contar_vocales(texto):
    contador=0
    contador1=0
    for i in texto:
        if i in "aeiou":
            contador+=1
        elif i in "AEIOU":
            contador1+=1
    print("La cantidad de vocales minusculas es: ", contador)
    print("La cantidad de vocales mayusculas es: ", contador1)
#texto=input("Ingrese su texto: ")
#contar_vocales(texto)
 
#4.  Inversión de Cadena: Crea una función `invertir_cadena` que reciba una 
# cadena de texto y devuelva la misma cadena pero invertida.

def invertir_cadena(cadena):
    vector = []
    for i in cadena:
        vector.append(i)
    for i in range(len(vector) - 1 ,-1,-1):
        print(vector[i], end=" ")

#invertir_cadena("Hola Mundo")


#6.  Suma de Múltiples Números: Implementa una función `sumar_numeros` que pueda 
# aceptar cualquier número de argumentos numéricos y devuelva su suma total.
def sumar_numeros(lista_numeros):
    for numero in lista_numeros:
        sumador += int(numero)
    return sumador

def llenar_lista_numeros():
    lista_numeros = []
    while True:
        numero = int(input("Ingrese un numero: "))
        lista_numeros.append(numero)
        if len(lista_numeros) >1:
            print("Desea Ingresar otro numero: ")
            opcion = input("SI / NO: ")
            if opcion.upper() == "NO":
                return lista_numeros

#print("Suma de Numeros")
#lista = llenar_lista_numeros()
#sumar_numeros(lista)

#7.  Calculador de Área de Figuras: Escribe una función `calcular_area` 
# que tome un argumento obligatorio para el tipo de figura 
# ('circulo', 'rectangulo', 'triangulo') y 
# argumentos adicionales con palabra clave (`radio`, `base`, `altura`, `lado1`, `lado2`) 
# según sea necesario para calcular y devolver el área. Maneja casos donde faltan 
# argumentos necesarios para la figura seleccionada.

def calcular_area(figura, base, altura, radio):
    if figura == 1:
        print(3.1416*radio**2)
    elif figura == 2:
        print(base*altura)
    elif figura == 3: 
        print((base*altura)/2)
while True:
    print("Calculadora de Areas")
    print("Elija una Opcion: ")
    print("1.- Circulo")
    print("2.- Rectangulo")
    print("3.- Triangulo")
    print("4.- Salir")
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        radio = float(input("Ingrese el radio: "))
        calcular_area(1,0,0,radio)
    elif opcion == 2:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        calcular_area(2, base, altura, 0)
    elif opcion ==3: 
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        calcular_area(3, base, altura, 0)
    elif opcion ==4: 
        break
    else:
        print("Error al ingresar la opcion")





#14. Validación de Contraseña: Escribe una función `validar_contrasena` que reciba una 
# cadena y devuelva `True` si la contraseña cumple con ciertos criterios 
# (ej. al menos 8 caracteres, al menos una mayúscula, una minúscula y un número), 
# y `False` en caso contrario.


#15. Conversor de Temperaturas: Desarrolla una función `convertir_temperatura` que reciba un valor numérico y una unidad de origen ('C' para Celsius, 'F' para Fahrenheit). La función debe devolver una tupla con el valor convertido y la nueva unidad (ej. `(32.0, 'F')` si se convierte de Celsius a Fahrenheit, o `(0.0, 'C')` si es al revés).

#16. Eliminador de Duplicados: Crea una función `eliminar_duplicados` que reciba una lista y devuelva una nueva lista sin elementos duplicados, manteniendo el orden original.

#17. Cifrado César Básico: Escribe una función `cifrar_cesar` que tome una cadena de texto y un número entero (el "desplazamiento"). La función debe devolver la cadena cifrada utilizando el cifrado César. Considera solo letras del alfabeto inglés (mayúsculas y minúsculas).

#18. Calculadora de IMC (Índice de Masa Corporal): Implementa una función `calcular_imc` que reciba el peso (en kg) y la altura (en metros) de una persona y devuelva su IMC. Luego, crea otra función `clasificar_imc` que reciba el IMC y devuelva una cadena con la clasificación (ej. "Bajo peso", "Normal", "Sobrepeso", "Obesidad").

#19. Promedio con Excepciones: Diseña una función `calcular_promedio_seguro` que reciba una lista de números. La función debe calcular y devolver el promedio. Si la lista está vacía, debe devolver 0.0 y no generar un error.

#20. Unir Diccionarios: Crea una función `unir_diccionarios` que pueda aceptar cualquier número de argumentos de diccionario y devuelva un nuevo diccionario que contenga la unión de todos ellos. Si hay claves duplicadas, el valor del último diccionario prevalece.