import mi_modulo
import operaciones
import utilidades

mi_modulo.saludar("Juan")
resultado = mi_modulo.calcular_suma(7,3)

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")