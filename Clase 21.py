#Dado 3 numeros ver el mayor


def numero (texto_input: str | None= "Ingrese un numero: ")->int:
    while True:
        numero_1= input ("Ingrese un numero: ")
        if numero_1.isdigit():
            numero_1 = int (numero_1)
            if numero_1 > 0:
                break
            else:
                print("El valor ingresado debe ser mayor a 0")
        else:
            print(" El valor ingresado no es un Nro")
        return numero_1
def calcular(cantidad: int | None=2):
    mayor = 0
    
    for i in range(cantidad):
        
        numero_1 = numero()
        print(f" El numero ingresado es {numero_1}")
        if numero_1 > mayor:
            mayor = numero_1

cantidad = numero(" Ingrese la cantidad de veces a calcular: ")
calcular ()   


    
print(f" El numero mayor es: {mayor}")
