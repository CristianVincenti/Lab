# Escriba un progrma que me permita ingresar valores y que corte cuando e lusuario envie A

contador = 0
seguir = True
letra = "a"
letra.islower()

while seguir:
    ingresa_valor = input (" Ingresa un valor  ")
    contador +=1
    if ingresa_valor == letra:
        seguir= False   
        contador -=1
print (f" Se ejecuto correctamemte  {contador} ")

## otra alternativa

contador = 0
seguir = True

while seguir:
    ingresa_valor = input (" Ingresa un valor  ")
    ingresa_valor = ingresa_valor.upper()
    contador +=1
    if ingresa_valor == "A":
        seguir= False   
    
print (f" Se ejecuto correctamemte  {contador} ")


# DEBUGGER ## ELIMINADOR DE ERRORES
#BUG'S##