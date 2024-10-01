#Nuestas funciones

def numero (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero, 
    texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            if numero_1 > 0:
                break
            else:
                print("El valor ingresado debe ser mayor a 0")
        else:
            print("El valor ingresado no es un Nro")
    return numero_1

#Ejemplo 1: Una funcion que salude, teniendo en cuenta que puede tener doble nombre y doble apellido:

def saludo(nombre:str, apellido:str | None = " ")->str:
    print(f"Hola {nombre}{apellido}")
    return 
saludo("Eugenia", " de Escobar")


#Ejemplo 2: Calcular el área de un cuadrado:



#Funcion para validar un numero
def validar_numero ()-> int:
    """
    Este int sirve para vlaidad un numero
    """
    while True:
        numero_a_validad = input (" Ingrese un numero: ")
        if numero_a_validad.isdigit():
            numero_a_validad = int(numero_a_validad)
            break
        else:
            print ("El dato ingresado no corresponde a un numero")
    return numero_a_validad

print(validar_numero())

#Funcion para validar Texto
def validar_texto(texto_input: str |None = " Ingrese un texto")-> str:
    """
    Valida el texto
    """
    while True:
        texto = input (texto_input)
        if texto.isalpha():
            break   
        else:   
            print(" El dato no corresponde a un texto")
    return texto_input
















    