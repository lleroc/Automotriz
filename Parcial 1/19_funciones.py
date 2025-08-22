#Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. 
#Cuando leas una fracción debes simplificarla.
def Leer_fracción():
    numerador = int(input("Ingrese el numerador de la fracción: "))
    denominador = int(input("Ingrese el denominador de la fracción: "))

    for i in range(2,numerador):
        if numerador %i ==0 and denominador %i == 0:
            numerador = numerador // i
            denominador = denominador // i
    return numerador, denominador

#Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1,
#  se muestra sólo el numerador.
def Escribir_fracción(numerador, denominador):
    if denominador == 1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")
#Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.

def Calcular_mcd(a, b):
    a = abs(a)
    b = abs(b)
    if b>a:
        a, b=b, a
    while b:
        a, b = b, a % b
    print(a)
    return a

#Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir 
# numerador y dominador por el MCD del numerador y denominador.
def Simplificar_fracción(num, den):
    mcd = Calcular_mcd(num, den)
    print(num // mcd,"/", den // mcd)

fraccion = Leer_fracción()
Escribir_fracción(fraccion[0], fraccion[1])
Calcular_mcd(fraccion[0], fraccion[1])
Simplificar_fracción(fraccion[0], fraccion[1])