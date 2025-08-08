#crear una lista de productos mediante funciones, las cuales puedan 
# crear, modificar, listar o eliminar un producto   => CRUD
lista_productos = []
def crear(nombre, codigobarras, cantidad, fecha_caducidad):    #nombre, codigobarras, cantidad, fecha_caducidad
    lista_productos.append([nombre, codigobarras, cantidad, fecha_caducidad])
    print("Producto creado con exito")
    
def modificar():
    listar()
    codigobarras = input("Ingrese el codigo de barras del producto a modificar:")
    for producto in lista_productos:
        if producto[1] == codigobarras:
            nombre = input("Ingrese el nuevo nombre del producto:")
            cantidad = input("Ingrese la nueva cantidad del producto:")
            fecha_caducidad = input("Ingrese la nueva fecha de caducidad del producto:")
            producto[0] = nombre
            producto[2] = cantidad
            producto[3] = fecha_caducidad
            print("Producto modificado con exito")

    
def listar():
    print("Lista de Productos: ")
    contador = 0
    for fila in lista_productos:
        print(f"#: {contador + 1} | Nombre: {fila[0]} | Codigo de Barras: {fila[1]} | Cantidad: {fila[2]} | Fecha: {fila[3]}")
        contador +=1

def eliminar():
    listar()
    codigobarras = input("Ingrese el codigo de barras del producto a eliminar: ")
    for producto in lista_productos:
        if producto[1] == codigobarras:
            lista_productos.remove(producto)
            print("Producto eliminado con exito")
            break
    

print("Bienvenido al Sistema de Registros de Productos")
while True:
    print("Menu Principal")
    print("1. Crear producto")
    print("2. Modificar producto")
    print("3. Listar productos")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Ingrese la opcion que desee: ")
    if opcion == "5":
        print("Tenga un buen dia")
        break
    elif opcion == "1":
        print("Crear producto")
        nombre = input("Ingrese el nombre del producto: ")
        codigobarras = input("Ingrese el codigo de barras del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        fecha_caducidad = input("Ingrese la fecha de caducidad del producto: ")
        producto = crear(nombre, codigobarras, cantidad, fecha_caducidad)
    elif opcion == "2":
        print("Modificar producto")
        modificar()
    elif opcion == "3":
        print("Lista de productos")
        listar()
    elif opcion == "4":
        print("Eliminar producto")
        eliminar()
    elif opcion =="5":
        print("Tenga un buen dia")
        break
    else:
        print("Opcion invalida, por favor intente de nuevo")
