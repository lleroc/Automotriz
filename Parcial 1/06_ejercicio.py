#Los tramos impuesto para la declaración de la renta en un determinado 
# país son los siguientes:
#Renta	Tipo            impuesto
#Menos de 10000€	    5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	        45%
#Escribir un programa que pregunte al usuario su renta anual y 
# muestre por pantalla el tipo impuesto que le corresponde.

renta = int(input("Ingrese el valor del impuesto a la renta: "))
if renta <= 10000:
    print(f"El valor es del 5%: {renta * 0.05}")
elif renta >10000 and renta <= 20000:
    print(f"El valor es del 15%: {renta * 0.15}")
elif renta >20000 and renta <= 35000:
    print(f"El valor es del 20%: {renta * 0.2}")
elif renta >35000 and renta <= 60000:
    print(f"El valor es del 35%: {renta * 0.35}")
else: 
    print(f"El valor es del 45%: {renta * 0.45}")