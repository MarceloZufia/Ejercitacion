def saludo():
    print("¡Hola! Bienvenido al programa.") 
    
saludo()  # Llamada a la función saludo

def saludo(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al programa.")  
    
saludo("María")  # Llamada a la función saludo con argumento
saludo("Marcelo")  # Llamada a la función saludo con argumento

def sumar(a, b):
    return a + b    

resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado) 

def potencia(base, exponente):
    return base ** exponente    

resultado = potencia(2, 3)
print("El resultado de la potencia es:", resultado)

def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función


variable_global = 20


def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20

