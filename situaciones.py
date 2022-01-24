import os
from time import sleep


def limpiar_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def buscar_valores(matriz):
    print("")
    #print("Hola soy situaciones")
    print("")
    print(matriz)
    print("")
    b = matriz[2][0]
    print("Este es el valor del rey: " + str(b))
    print("")
    sleep(2)
    limpiar_console()
    avance_valores(matriz)


cont = 1


def avance_valores(matriz):
    global cont
    if matriz[2][cont] == 0:
        print("No hay nada en la casilla")
        print("")
        matriz[2][cont] = matriz[2][cont-1]
        print("El rey se mueve 1 casilla")
        print("")
        matriz[2][cont-1] = 0
        cont = cont + 1
        # print(cont)
        print(matriz)
        sleep(2)
        limpiar_console()

        if matriz[2][4] != 2:
            avance_valores(matriz)
        else:
            print("")
            print("El bloque rey ha ganado")
            print("")
            print(matriz)

    else:
        print("")
        print("La casilla esta ocupada")
        print("")
        print(matriz[1][cont])
        print("contador: " + str(cont))
        print("")
        if matriz[1][cont] == 0:
            print("No hay nada en la casilla")
            print("")
            matriz[1][cont] = matriz[2][cont]
            matriz[2][cont] = 0
            print(matriz)
            sleep(2)
            limpiar_console()
            avance_valores(matriz)
        else:
            print("")
            print("La casilla esta ocupada")
            print("")
            print(matriz[0][cont])
            print("contador: " + str(cont))
            print("")
            if matriz[0][cont] == 0:
                print("No hay nada en la casilla")
                print("")
                matriz[0][cont] = matriz[1][cont]
                matriz[1][cont] = 0
                print(matriz)
                sleep(2)
                limpiar_console()
                avance_valores(matriz)
            else:
                print("")
                print("La casilla esta ocupada")
                print("")
                if matriz[3][cont] == 0:
                    print("Soy de la casilla 3 a 4")
                    print("")
                    matriz[3][cont] = matriz[2][cont]
                    matriz[2][cont] = 0
                    print(matriz)
                    sleep(2)
                    limpiar_console()
                    avance_valores(matriz)
                else:
                    print("")
                    print("La casilla esta ocupada")
                    print("")
                    if matriz[4][cont] == 0:
                        print("Soy de la casilla 4 a 5")
                        print("")
                        matriz[4][cont] = matriz[3][cont]
                        matriz[3][cont] = 0
                        print(matriz)
                        sleep(2)
                        limpiar_console()
                        avance_valores(matriz)
