from numpy import random as rd
import situaciones as s
class hello:
    
    def crear_matriz(self):
        filas = 5
        columnas = 5
        a = rd.randint(0,2,(filas,columnas))

        self.bloquerey = 2

        a[2][0] = self.bloquerey

        print(a)

        s.buscar_valores(a)

        


    def __init__(self):
        #print("Hello World")
        bienvenida="""
        **************************************
        *---Bienvenido a escape del bloque---*
        **************************************"""
        print(bienvenida)

        self.crear_matriz()
        
    

objeto = hello()