import funciones as f

#numero_1 = f.validar_numero()
#numero_2 = f.validar_numero()

nombre = f.validar_texto("Ingrese su nombre:") or f.validad_vacio()
apellido = f.validar_texto("Ingrese su apellido:") or f.validad_vacio()
localidad = f.validar_texto("Ingrese su localidad:")
provincia = f.validar_texto("Ingrese su provincia:")
telefono = f.validar_texto ("Ingrese su numero de telefono:")

print(f"Los datos del cliente son: \n nombre: {nombre}\n apellido {apellido}\n localidad {localidad}\n provincia{provincia}\n telefono{telefono}")


