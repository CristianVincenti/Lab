continuar = 0
var = input("Ingrese un numero: ")
print (f" Ingrese un numero: {continuar}")

contador = 1
continuar = True

if var.isdigit():
    print (f" El numero ingresado es: {var}  en el intento numero: {contador}")
else:
    continuar = False
    print (f" Incorrecto, vuelva a ingresar un numero: {continuar} , esta es su {contador} oportunidad ")
    contador =+1
    var = input("Ingrese un numero: ")

if not continuar:
    if var.isdigit():
        print (f" El numero ingresado es: {var}  en el intento numero: {contador}")
        continuar = True
    else:
        print (f" Incorrecto, vuelva a ingresar un numero: {continuar}, esta es su {contador} oportunidad|  ")
        contador =+1
        var = input("Ingrese un numero: ")
        continuar = False

if not continuar:
    if var.isdigit():
        print (f" El numero ingresado es: {var}  en el intento numero: {contador}")
        continuar = True
    else:
        continuar = False
        print (f" Esta fue su ultima oportunidad  ")