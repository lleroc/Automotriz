from restaurante import Clase_Restaurante
from recetas import clase_recetas
from clientes import clase_clientes

res = Clase_Restaurante(1,"El Restaurante XXX","Solo carnes")
print(res)

cliente = clase_clientes("Juan", "Pujar","1234567890","0987654321","Ahi mimso")

print(cliente)

res1 = clase_recetas("Papas Fritas",["papas","aceite", "sachcichas","sal"],
                     ["1.- Pelamos las papas","2.- Llenamos las papas con aceite",
                      "3.- Llenamos las papas con sachcichas",
                      "4.- Llenamos las papas con sal"],1)
print(res1)

res2 = clase_recetas("Hamburguesas")
print(res2)
res2.agregar_ingredientes(["pan","carne molida","sal"])
print(res2)
res2.agregar_preparacion(["1.- Cortamos la carne","2.- Cortamos el pan","3.- Cortamos la sal"])
print(res2)
res2.agregar_cliente(1234567890)
res2.asignar_restaurante(1)

print(res2.mostrar_receta())
print("*"*20)
print(res2)
