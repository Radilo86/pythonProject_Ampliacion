''' Ejercicio 1
    Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas.
    Objetivo:
        - Aprender a utilizar librerías sencillas (en este caso, os) y sus funciones.
        - Aprender a utilizar los bucles y los condicionales.

    El algoritmo del ejercicio es el siguiente:
        - Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas
        una función existente en la librería os (Sistema Operativo) de Python.
        - Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo,
        con un bucle for.
        - Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también
        necesitas una función existente en os. '''

import os

def listarFicheros_Y_Directorios(ruta):
    contenido = os.listdir(ruta)
    '''
    print("El contenido total del directorio es: ")
    for campo in contenido:
        print(campo)
    print("\n")
    '''

    print("Mostramos solamente los ficheros (sin directorios): \n")
    for campo in contenido:
        if os.path.isfile(ruta+'\\'+campo):
            print(campo)

if __name__ == "__main__":
    ruta = input("Introduce la ruta completa. (Ejemplo --> C:\Misdocumentos\example): \n")
    # print(ruta)
    listarFicheros_Y_Directorios(ruta)
