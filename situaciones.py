def buscar_valores(matriz):
        print("")
        print("Hola soy situaciones")
        print("")
        print(matriz)
        print("")
        b = matriz[2][0]
        print("Este es el valor del rey: " + str(b))
        print("")

        avance_valores(matriz)        

def  avance_valores(matriz):
        if matriz[2][1] == 0:
                print("el valor de la casilla es matriz: " + matriz[2][1])