nombre_y_apellido= input ("Ingrese su nombre y apellido:")
print(f" Hola, mi nombre es {nombre_y_apellido}")
num_telefono = input (" Mi contacto es:")
print(f" Te paso mi contacto {num_telefono}")
e_mail= input ("Ingrese su correo electronico:")
print(f" y mi mail es {e_mail}")
estado_de_animo = input ( "como estuvo tu dia un ")
print(f" Mi dia estuvo un  {estado_de_animo}")
estado_de_animo = int( input ("estado_de_animo"))
if estado_de_animo >= 0 and estado_de_animo <= 5:
    print ("Animo, disfrute el dia")
elif estado_de_animo > 5 and estado_de_animo < 8:
    print (" Sigas adelante")
else :
    print (" Excelente, ese es un espiritu positivo")
age = input ("Mi edad es:")
print(f" Mi edad es {age}")
ubicacion = input (" Recido en:")
print(f" Donde vivo {ubicacion}")
print (f"Donde vivo {ubicacion} y mi edad es: {age}")
bebida_favorita = input("Mi bebida favorita es")
comida = input ("Que menu prefieres?")
print (f" Mi bebida favorita es {bebida_favorita} y mi principal plato es: {comida}")
