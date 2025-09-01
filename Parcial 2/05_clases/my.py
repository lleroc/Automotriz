from archivo_estudiante import clase_estudiante
from archivo_profesor import clase_profesor
import gc

est1 = clase_estudiante("Luis","Llerena",32,"Software", "Segundo")
est2 = clase_estudiante("Pepito","Perez",22,"Software", "Primero")
profe = clase_profesor("Juan","Zurita",35,"Chef","005")
print("---Impresion de Informacion")
print(est1.mostrar_info())
print(est2.mostrar_info())
print(profe)
print("Eliminar los objetos")
del est1
del est2
del profe
print("Garbage Collector")
gc.collect()
print("Fin")