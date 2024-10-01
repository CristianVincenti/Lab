"""
variable = " Hola como estas"

cuit = "20-24878390-8"

lista = [ "Holas", " cpmp" , " estas"]

lista_apartir_variable = variable. split ()

print (lista_apartir_variable)

lista_apartir_cuit = cuit.split(".")
primer_parte_valida = ["20","22", "27","30", "24"]
print (lista_apartir_cuit)

if lista_apartir_cuit[0] ==primer_parte_valida:
    print("La primer parte es valida")
"""

cuit = input (" Escriba su cuit para validadrlo")
if len(cuit) != 13:
    print (" La longitud es distinta de 13 digitos")
if cuit[2] != '-':
    print (" Su tercer lugar no es un -")
if cuit[11] != "-":
    print(" Su doceavo lugar no es un -")
base = [ 5,4,3,2,7,6,5,4,3,2]
cuit= cuit.replace("-", "")

aux = 0
for i in range(10):
    int_cuit = int(cuit[i])
    aux += int_cuit
    valor_base = base[i]
    aux *= valor_base

aux_dividido = aux /11
aux_entero  = int(aux_dividido)
aux_multiplicado = aux_entero * 11
aux_parentesis = aux - aux_multiplicado
aux_restado = 11 - aux_parentesis


   
aux = 11 - (aux - (int(aux /11)*11))
if aux == 10:
    print (" Cuit Valido")
else:
    print ("Cuit Invalido")
    