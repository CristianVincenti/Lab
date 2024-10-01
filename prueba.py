N1= "hola mundo"
N2= "hermosa mañana verdad?"
N1= N1 + (N2*2)
print (N1)
#####2numero1 = input ("Por favor ingrese un numero:")
numero1 = input ("Por favor ingrese un numero: ")
numero2 = input ("Por favor ingrese un numero: ")
print (f" La suma de los numeros ingresados es: {numero1 + numero2}")

# Concatenacion de funciones

numero1 = input ("Por favor ingrese un numero:")
numero1 = int (numero1)
numero2 = input ("Por favor ingrese un numero: ")
numero2 = int (numero2)
print (f" La suma de los numeros ingresados es: {numero1 + numero2}")

#print (id(numero1))
#print (id(numero2))

#Tipo de variable
numero1 = input ("Por favor ingrese un numero:")
print (type(numero1)
)
numero1 = input (numero1)
print (type(numero1))

print (type(numero1))

##### Repaso
var = "Hola"

if var.isdigit():
    print (" Es un numero")
    var = input(" Tienes otra opportunidad, Ingrese una palabra")
    var.isdigit()
        
else: 
    print(" No es un numero")
    print (var)
    
var.isalpha()
# Programa que solo ingrese palabras con 3 intenntos

var= (" Ingrese una palabra")
continuar= False

if var.isdigit():
    print(" Es un numero") 
    var=input ("Ingrese de nuevo una palabra o letra")
if var.isdigit():
    print(" Error: Es un numero")
    var=input ("Ingrese de nuevo una palabra o letra")
    if var.isdigit():
        print( "Fue tu ult imo intento")
        exit()
else: print(var)

#! Programa que solo ingrese palabras con 3 intentos

continuar= False

var = input("Ingrese una palabra")

if var.isdigit():
    print("Error, es un numero")
    continuar= True
else: 
    continuar= False

if continuar:
    var= input (" Ingrese por segunda vez una palabra")
    
if var.isdigit():
    print("Error, es un numero")
    continuar= True
else: 
    continuar= False

if continuar:
    var= input (" Ingrese por tercera vez una palabra")
    
if var.isdigit():
    print("Esta fue tu ultima oportunidad")
    exit()


