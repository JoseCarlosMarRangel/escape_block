from numpy import ma


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
                matriz[2][1] = matriz[2][0]
                print("El bloque rey se mueve a la derecha")
                #print("el valor de la casilla 2,1 es: "  + str(matriz[2][1]))
                print("")
                matriz[2][0] = 0
                print(matriz)
        else:
                matriz[2][1] = 0
                print(matriz)     
