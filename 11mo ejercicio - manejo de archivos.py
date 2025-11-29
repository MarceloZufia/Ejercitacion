# Manejo de archivos en Python
# Este script demuestra cómo abrir, leer, escribir y cerrar archivos en Python.

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)