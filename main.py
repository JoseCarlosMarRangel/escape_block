from time import sleep
from numpy import random as rd
import situaciones as s
import os


class hello:

    def crear_matriz(self):
        filas = 5
        columnas = 5
        a = rd.randint(0, 2, (filas, columnas))

        self.bloquerey = 2

        a[2][0] = self.bloquerey

        print(a)

        s.buscar_valores(a)

    def limpiar_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def __init__(self):
        #print("Hello World")
        bienvenida = """
        **************************************
        *---Bienvenido a escape del bloque---*
        **************************************"""
        print(bienvenida)
        sleep(2)
        self.limpiar_console()
        self.crear_matriz()


objeto = hello()
