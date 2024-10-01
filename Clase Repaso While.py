'''# Ejercicio 2 While- Realizar un programa que sume numeros hasta que ingrese 0

acumulador = 0
numero = 1
while numero != 0:
    numero = input(" Ingrese un numero")
    
    if numero.isdigit():
        numero = int(numero)
        acumulador += numero
        print (f" El numero ingresado es {numero} y el acumulado es {acumulador}")
    else:
        print (" Ingrese un numero valido")
        
'''
#! Ejercicio 3 While-- Tabla de multiplicar
continuar = True
while continuar:
    numero_usuario = input (" Ingrese un numero de la tabla de multiplicar entre el 1 al 10:   ")
    if not numero_usuario.isdigit():
        exit ("Error")
    numero_usuario = int(numero_usuario)    
    contador = 0
    while contador<10:
        contador += 1
        print( f"{contador} x {numero_usuario}= {numero_usuario*contador}")
        continuar = input (" Si desea multiplicar otro numero coloque 1 sino, 0:")
        if continuar == "1":
            continuar= True
        else:
            continuar = input(" Estas seguro que queres salirPone 1 para volver a usar la multipladora")
        if continuar == "1":
            continuar= True
        else:
            continuar = False    