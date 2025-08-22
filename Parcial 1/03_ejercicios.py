opcion_ve =""
opcion_no = ""
print("Hola, Bievenido a Bella Napoli Pizza")
print ("Ofrece pizzas  y no vegetarianas")
print("1.- Vegetarianas")
print("2.- No Vegetarianas")
opcion = input("Cual desea Usted (1/2):")
ve_ingrediente_1 = "Pimiento"
ve_ingrediente_2 = "Tofu"
no_ingrediente_1 = "Peperoni"
no_ingrediente_2 = "Jamón"
no_ingrediente_3 = "Salmón"

if opcion == "1":
    print("Elija un ingrediente para su pizza:")
    print(f"1.- {ve_ingrediente_1}")
    print(f"2.- {ve_ingrediente_2}")
    opcion_ve = input("Ingrese su opcion: ")
elif opcion == "2":
    print("Elija un ingrediente para su pizza:")
    print(f"1.- {no_ingrediente_1}")
    print(f"2.- {no_ingrediente_2}")
    print(f"3.- {no_ingrediente_3}")
    opcion_no = input("Ingrese su opcion: ")
else:
    print("No disponemos de esa opcion")
    
if opcion == "1":
    print("Su opcion es una pizza Vegetariana")
    print("Los Ingredientes son:")
    print("1.- Mozzarella ")
    print("2.- Tomate ")
    if opcion_ve == "1":
        print("3.- Pimientos")
    else:
        print("4.- Tofu")
else:
    print("Su opcion es una pizza NO Vegetariana")
    print("Los Ingredientes son:")
    print("1.- Mozzarella ")
    print("2.- Tomate ")
    if opcion_no == "1":
        print("3.- Peperoni")
    elif opcion_no == "2":
        print("3.- Jamón")
    else:
        print("3.- Salmón")
    
print("Su orden estara lista en 10 minutos")
print("Gracias por su compra")