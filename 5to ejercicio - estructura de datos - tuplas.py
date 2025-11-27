# Las tuplas son una estrutura de datos inmutable y ordenada en Python.
# Se utilizan para almacenar múltiples elementos en una sola variable.
# A diferencia de las listas, las tuplas no pueden ser modificadas después de su creación.

# Crear una tupla
punto = (3, 4)
print("Tupla punto:", punto)
print("Tipo de dato de punto:", type(punto))

# Acceder a elementos de una tupla
print("Primer elemento de la tupla punto:", punto[0])
print("Segundo elemento de la tupla punto:", punto[1])

"""
Métodos de una tupla
count(elemento): devuelve el número de veces que aparece un elemento en la tupla.
 
index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 

len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
""" 

mi_tupla = (1, 2, 3, 2, 4, 2)
print("Tupla mi_tupla:", mi_tupla)  
print("Número de veces que aparece el 2 en mi_tupla:", mi_tupla.count(2))
print("Índice de la primera aparición del 3 en mi_tupla:", mi_tupla.index(3))
print("Longitud de mi_tupla:", len(mi_tupla))
