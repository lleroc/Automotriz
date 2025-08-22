class clase_dividir:
    def divide(n1,n2,n3=0,n4=0):
        if  n3 == 0:
            if n4 == 0:
                return n1 / n2
            else:
                return n1 / n2 / n4
        else:
            if n4 == 0:
                return n1 / n2/ n3
            else:
                return n1 / n2/ n3/ n4
