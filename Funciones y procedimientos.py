"""""
a = 5
b = 8

def operacion (nummero_1: int, numero_2: int, operacion: str ):
    resultado = a + b
    return resultado

#print (operacion(a,b)*10) #salida:13
#operacion(10,10)  # Salida: 20
numero_1 = int(input (" Ingrese el valor a sumar: "))
numero_2 = int (input (" Ingrese el valor a sumar: "))

print(operacion (numero_1, numero_2))

"""
"""
def operacion (nummero_1: int, numero_2: int, operacion: str ):
    
    if operacion == "+" or operacion == "suma":
        resultado = nummero_1 + numero_2
    return resultado


input_1 = int(input (" Ingrese el valor a sumar: "))
input_2 = int (input (" Ingrese el valor a sumar: "))
input_operacion = input (" Ingrese la operacion a realizar (+,-,*,/,\%\ o suma, resta, multiplicacion, division, modulo)")

print(operacion (input_1, input_2, input_operacion))
"""

def imprimir(parametro):
    print (parametro)
    return

imprimir(input (" Ingrese texto: "))
imprimir(" Hola Mundo")
