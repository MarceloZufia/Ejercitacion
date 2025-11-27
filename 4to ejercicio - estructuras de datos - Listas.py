# Vamos a trabajar con listas en Python.
frutas = ["manzana", "banana", "cereza"]

# Imprimimos cada fruta por separado. Empezando desde el índice 0. Es el primer elemento.  
print ("Imprimimos cada fruta por separado. Empezando desde el índice 0. Es el primer elemento.")
print (frutas[0])
print (frutas[1])
print (frutas[2])

# Imprimimos cada fruta por separado. Empezando desde el índice -1. Es el último elemento.  
print ("Imprimimos cada fruta por separado. Empezando desde el índice -1. Es el último elemento.")
print (frutas[-1])
print (frutas[-2])
print (frutas[-3])

"""_
Métodos de listas
Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:

append(elemento): agrega un elemento al final de la lista.
insert(indice, elemento): inserta un elemento en una posición específica de la lista.
remove(elemento): elimina la primera aparición de un elemento en la lista.
pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
sort(): ordena los elementos de la lista en orden ascendente.
reverse(): invierte el orden de los elementos en la lista.    
    
"""
# Agregamos una fruta al final de la lista.
print ("Agregamos un elemento a la lista.")
frutas.append("naranja")
print (frutas)

# Insertamos una fruta en la posición 1 (segunda posición).
print ("Insertamos un elemento en la posición 1 (segunda posición).")
frutas.insert(1, "kiwi")
print (frutas) 

# Eliminamos la fruta "banana" de la lista.
print ("Eliminamos el elemento 'banana' de la lista.")
frutas.remove("banana")
print (frutas)      

# Eliminamos y devolvemos el elemento en la posición 2 (tercera posición).
print ("Eliminamos y devolvemos el elemento en la posición 2 (tercera posición).")
fruta_eliminada = frutas.pop(2)
print ("Fruta eliminada:", fruta_eliminada)
print (frutas)      

# Ordenamos las frutas en orden ascendente.
print ("Ordenamos las frutas en orden ascendente.")
frutas.sort()
print (frutas)  

# Invertimos el orden de las frutas en la lista.
print ("Invertimos el orden de las frutas en la lista.")
frutas.reverse()
print (frutas)

#Listas por comprensión
# Creamos una lista de cuadrados de números del 0 al 9 utilizando listas por comprensión.
print ("Creamos una lista de cuadrados de números del 0 al 9 utilizando listas por comprensión.")
cuadrados = [x**2 for x in range(10)]
print (cuadrados)

