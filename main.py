from random import Random
import numpy as np

class hello:
    
    def crear_matriz(self):
        filas = 3
        columnas = 3
        self.matriz = np.zeros((filas, columnas))
        print(self.matriz)

    def __init__(self):
        #print("Hello World")
        bienvenida="""
        **************************************
        *---Bienvenido a escape del bloque---*
        **************************************"""
        print(bienvenida)

        self.crear_matriz()
        
    

objeto = hello()