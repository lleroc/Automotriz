nombre = input("Ingrese el Nombre del Animal")
especie = input("Ingrese la especie del Animal 1.- Mamifero 2.- Ave")
tipo_de_alimentación = input("Ingrese alimentacion del Animal 1. Carne 2.- Hierva")
habitat = input("Ingrese el habitad del Animal 1.- Tierra 2.- Aire")
habitos = input("Ingrese los habitos del Animal 1.- Comen Carne 2.- Comen hierva")
atencion = input("Requiere atencion urgente 1. Si 2. No")
print(f"El nombre del animal es: {nombre}")
if especie == 1:
    print("El animal es mamifero")
else:
    print("El animal es ave")
if tipo_de_alimentación == 1:
    print("El animal se alimenta de carne")
else:
    print("El animal se alimenta de hieva")
if habitat == 1:
    print("El animal vive en la tierra")
else:
    print("El animal vive en el aire")
if habitos == 1:
    print("El animal como carne")
else:
    print("El animal como hierva")
if atencion == 1:
    print("El animal requiere atencion urgente")
else:
    print("El animal no requiere atencion")


