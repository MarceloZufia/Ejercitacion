"""
    Conjunto (set) en Python
    Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos.   
    Los conjuntos se encierran entre llaves {} o se crean utilizando la función set().


"""
# Crear un conjunto
numeros = {1, 2, 3, 4, 5}
print("Conjunto numeros:", numeros)
print("Tipo de dato de numeros:", type(numeros))

frutas = set(["manzana", "banana", "cereza"])
print("Conjunto frutas:", frutas)
print("Tipo de dato de frutas:", type(frutas))  

# Unir dos conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
union_conjuntos = conjunto_a | conjunto_b
print("Unión de conjunto_a y conjunto_b:", union_conjuntos)

# Intersección de dos conjuntos
interseccion_conjuntos = conjunto_a & conjunto_b
print("Intersección de conjunto_a y conjunto_b:", interseccion_conjuntos)   

diferencia_conjuntos = conjunto_a - conjunto_b
print("Diferencia de conjunto_a y conjunto_b:", diferencia_conjuntos)   

diferencia_simetrica = conjunto_a ^ conjunto_b
print("Diferencia simétrica entre conjunto_a y conjunto_b:", diferencia_simetrica)  

"""
Métodos de un conjunto

Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

add(elemento): agrega un elemento al conjunto.
remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
clear(): elimina todos los elementos del conjunto.

"""

frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()
