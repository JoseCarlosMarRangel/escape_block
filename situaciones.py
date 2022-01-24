from numpy import ma, mat
import os

def limpiar_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

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

cont = 1
def  avance_valores(matriz):
        global cont
        if matriz[2][cont] == 0:
                print("No hay nada en la casilla")
                print("")
                matriz[2][cont] = matriz[2][cont-1]
                print("El rey se mueve a la casilla 1")
                print("")
                matriz[2][cont-1] = 0
                cont = cont + 1
                #print(cont)
                print(matriz)

                if matriz[2][4] != 2:
                        avance_valores(matriz)
                else:
                        print("")
                        print("El bloque rey ha ganado")


        else:   
                print("")
                print("La casilla esta ocupada")
                print("")
                print(matriz[1][cont])
                print ("contador: " + str(cont))
                print("")
                if matriz[1][cont] == 0:
                        print("No hay nada en la casilla")
                        print("")
                        matriz[1][cont] = matriz[2][cont]
                        matriz[2][cont] = 0
                        print(matriz)
                        avance_valores(matriz)
                else:
                        print("")
                        print("La casilla esta ocupada")
                        print("")
                        print(matriz[0][cont])
                        print ("contador: " + str(cont))
                        print("")
                        if matriz[0][cont] == 0:
                                print("No hay nada en la casilla")
                                print("")
                                matriz[0][cont] = matriz[1][cont]
                                matriz[1][cont] = 0
                                print(matriz)
                                avance_valores(matriz)        

                #if matriz[3][cont] == 0:
                