""" Ejercicio 1
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
        necesitas una función existente en os.

    Ampliación:
        - Lista los tamaños de los ficheros en formato humano.
        - Recorre de manera recursiva todos los directorios desde tu carpeta personal
            y muestra los ficheros de cada directorio y su tamaño.
"""
# Radilo86
import os

def listarFicheros_Y_Directorios(ruta):
    """
    contenido = os.listdir(ruta)
    print("El contenido total del directorio es: ")
    for campo in contenido:
        print(campo)
    print("\n")

    print("\nMostramos solamente los ficheros (sin directorios): ")
    for campo in contenido:
        if os.path.isfile(ruta + '\\' + campo):
            Obtenemos el tamaño y lo convertimos de bytes a Megabytes, redondeado a 2 decimales.
            volumen = str(round((os.path.getsize(ruta + '\\' + campo) / 1024), 2))+"Mb."
            Devolvemos los archivos y su tamaño (convertido en String)
            print("Archivo: " + campo + " --> tamaño: " + volumen)

    print("\n\n\n")
    """

    print("Mostramos de manera recursiva los directorios de mi carpeta personal:")
    for directorios, dirs, ficheros in os.walk(ruta):
        print(directorios)
        for nombreFichero in ficheros:
            volumen = str(round((os.path.getsize(directorios + '\\' + nombreFichero) / 1024), 2)) + "Mb."
            print("\t" + "Archivo: " + nombreFichero + " --> " + volumen)


if __name__ == "__main__":
    ruta = input("Introduce la ruta completa. (Ejemplo --> C:\Misdocumentos\example): \n")
    # print(ruta)
    listarFicheros_Y_Directorios(ruta)
