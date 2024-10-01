"""
Realizar un login que permita ingresar con varios usuarios y contraseñas.
"""

USUARIO = "Diego"
PASSWORD = "Diego*123"

ingrese_usuario = input("Ingrese el usuario a continuacion:")
ingrese_pass = input("Ingrese el contraseña a continuacion:")
ingrese_area = input ("Area de Administracion: ")

while True:
    if USUARIO == ingrese_usuario and PASSWORD == ingrese_pass:
        print("Credenciales Validas")
    else:
        print ("Ingrese el usuario y Contraseña Correcta: ")

print (ingrese_area)    



   