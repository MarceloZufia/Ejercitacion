numero = 7

if numero % 2 == 0:
    resultado = "Par"
    print("El número es par.")
else:
    resultado = "Impar"
    print("El número es impar.")
    
# -------------------------------------------------------
    
def multiplicar (a, b):  
    return a * b

resultado = multiplicar (5, 3) + multiplicar (2, 4)
print("El resultado de la suma de las multiplicaciones es:", resultado)