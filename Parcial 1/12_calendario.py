#Imprime un calendario mensual simple: muestra los días de la semana 
# en forma de tabla para 4 semanas.
#dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#semanas = 4
#dia = 1
#for dias in dias_semana:
#    print(f"{dias:>4}", end=" ")
#print()
#for semana in range(semanas):
#    for dias in dias_semana:
#        print(f"{dia:>4}", end=" ")
#        dia+=1
#    print()
#simulacion del funcionamiento de un reloj

for horas in range(12):
    for minutos in range(60):
        for segudos in range(60):
            print(f"{horas} : {minutos} : {segudos}")