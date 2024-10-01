#Saludo ="Hola Mundo"
#print (Saludo)

temperatura = float(input ("Ingrese la temperatura que desea convertir:  "))
escala = input (" Es Fahreinheit (F) o es Celsius (C): "). lower()

if escala == "f":
    celsius = (temperatura -32) * 5/9
    print (f" La temperatura en Celsius es {celsius} grados")
elif escala =="c":
    fahreinheit = temperatura * 1.8 + 32
    print (f"La temperatura en Fahreinheit es {fahreinheit} grados")
else:
    print ("Escala incorrecta")

