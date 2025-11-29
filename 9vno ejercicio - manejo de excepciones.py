# Ejercitación para entender el manejo de las excepciones en Python

# En este ejemplo, solicitamos al usuario que ingrese un número entero.
try:
    # Intentamos convertir una entrada del usuario a entero
    numero = int(input("Por favor, ingresa un número entero: "))
    print(f"Has ingresado el número: {numero}")
except ValueError:
    # Capturamos la excepción si la conversión falla
    print("Error: No has ingresado un número entero válido.")   
    
# Ahora, intentamos dividir 100 por el número ingresado
try:
    resultado = 100 / numero
    print(f"El resultado de dividir 100 por {numero} es: {resultado}")
except ZeroDivisionError:
    # Capturamos la excepción si el usuario ingresa cero
    print("Error: No se puede dividir por cero.")   
    
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción   
    
# Ejemplo de creación y uso de una excepción personalizada10

def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")