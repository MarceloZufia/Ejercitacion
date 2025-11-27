"""
    Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. 
    Los diccionarios se encierran entre llaves {}, y los pares clave-valor se separan por comas._
"""
# Crear un diccionario
persona = {"Nombre": "Marcelo", "Edad": 56, "Ciudad": "Mendoza"}    
print("Diccionario persona:", persona)
print("Tipo de dato de persona:", type(persona))    

# Acceder a elementos de un diccionario
print("Nombre de la persona:", persona["Nombre"])
print("Edad de la persona:", persona["Edad"])
print("Ciudad de la persona:", persona["Ciudad"])

""" 
Métodos de un diccionario

get(clave): devuelve el valor asociado a la clave especificada. 

keys(): devuelve una vista de todas las claves del diccionario.

values(): devuelve una vista de todos los valores del diccionario.

items(): devuelve una vista de todos los pares clave-valor del diccionario.

update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.

""" 

print  ("Claves del diccionario persona:", persona.keys())
print  ("Valores del diccionario persona:", persona.values())
print  ("Pares clave-valor del diccionario persona:", persona.items())

# Actualizar el diccionario
persona.update({"Edad": 57, "Profesión": "Ingeniero"})
print("Diccionario persona actualizado:", persona)  
