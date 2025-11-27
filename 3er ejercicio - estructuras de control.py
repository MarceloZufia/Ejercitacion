edad = 70
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
elif edad > 15:
    print("Eres mayor de 15 años.")
    if edad >= 65:
        print("Eres adulto mayor.")
        
        
calificacion = 85


if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")