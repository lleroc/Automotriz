productos={}
id_autonumerico =0

def agregar_producto():
    global id_autonumerico
    producto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    productos[id_autonumerico] = {"nombre": producto, "precio": precio}
    id_autonumerico += 1
    print("Se guardo con exito")

def actualziar_producto():
    mostrar_todos_productos()
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    for producto in productos.items():
        if producto[1]["nombre"] == nombre:
            precio = input("Ingrese el nuevo precio del producto: ")
            productos[1]["precio"] = precio
            print(f"Nombre: {producto[1]["nombre"]} Precio: {producto[1]["precio"]}")
            break


def mostrar_todos_productos():
    for un_producto in productos.items():
        print(f"# {un_producto[0] + 1} | Nombre: {un_producto[1]["nombre"]} ")

def un_producto():
    producto = input("Ingrese el nombre del producto: ")
    if producto != "":
        for un_producto in productos.items():
            if un_producto[1]["nombre"] == producto:
              print(f"Nombre: {un_producto[1]["nombre"]} Precio: {un_producto[1]["precio"]}")

def eliminar_producto():
    mostrar_todos_productos()
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    for producto in productos.items():
        if producto[1]["nombre"] == nombre:
            del productos[producto[0]]

print("Sistema de Registro de Prodcutos")
print("Bienvenido")
while True:
    print("Menu Principal")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Mostrar todos los productos")
    print("4. Mostrar un producto")
    print("5. Eliminar producto")
    print("6. Salir")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        actualziar_producto()
    elif opcion == 3:
        mostrar_todos_productos()
    elif opcion == 4:
        un_producto()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opcion invalida, por favor intente de nuevo")
    

    
    
    
