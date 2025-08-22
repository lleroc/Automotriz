lista_paises = []
lista_provincias = []

def crear_pais(nombre_pais, codigo_pais):
    global lista_paises
    pais = {
        "codigo":codigo_pais,
        "nombre_pais":nombre_pais
        }
    lista_paises.append(pais)
    return pais

def todos_paises():
    if not lista_paises:
        print("No existe informacion")
    else:
        for pais in lista_paises:
            print(f"Codigo: {pais['codigo']}, Nombre: {pais['nombre_pais']}")

def un_pais(codigo_pais):
    for pais in lista_paises:
        if pais['codigo'] == codigo_pais:
            return pais

def actualizar_pais(codigo_pais, nombre_pais):
    for pais in lista_paises:
        if pais['codigo'] == codigo_pais:
            pais['nombre_pais'] = nombre_pais
            return pais
    return "El pais no se actualizo"

def eliminar_pais(codigo_pais):
    for pais in lista_paises:
        if pais['codigo'] == codigo_pais:
            lista_paises.remove(pais)
            return True
    return "No existe el pais"

####################provincia
def crear_provincia(codigo_provincia, nombre_provincia, codigo_pais):
    global lista_provincias
    provincia = {
        "codigo":codigo_provincia,
        "nombre_provincia":nombre_provincia,
        "codigo_pais":codigo_pais
        }
    lista_provincias.append(provincia)
    return provincia
    
def todos_provincia(codigo_pais = None):
    for provincia in lista_provincias:
        if codigo_pais is None or provincia["codigo_pais"] == codigo_pais:
            for pais in lista_paises:
                if pais["codigo"] == provincia["codigo_pais"]:
                    print(f"Codigo: {provincia['codigo']}")
                    print(f"Nombre: {provincia['nombre_provincia']}") 
                    print(f"Pais: {pais['nombre_pais']}")


crear_pais("Ecuador","EC")
crear_pais("Peru","PE")
crear_pais("Chile","CL")
crear_pais("Argentina","AR")

crear_provincia(18,"Tungurahua","EC")
crear_provincia(19,"Pichincha","EC")
crear_provincia(20,"Guayas","EC")
crear_provincia(21,"Loja","EC")
crear_provincia(22,"Azuay","EC")
crear_provincia(23,"Cañar","EC")


crear_provincia(1,"Aguas Verdes","PE")

todos_provincia()