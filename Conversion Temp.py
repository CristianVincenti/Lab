"""import funciones as f

celsius = f.validar_numero
fahrenheit = f.validar_numero

temp = input(" Ingrese la temperatura que desea convertir")

#celsius = input (" Ingrese los grados que desea convertir: ")
#fahrenheit = input (" Ingrese los grados que desea convertir: ")


def temperatura (numero: int)-> int:
    
    
    return celsius


celsius = temperatura()

print(f" Ela temperatura en grados Celsius es: {temperatura}")
"""


def convertir_temperatura(valor, unidad):
    if unidad == 'C':
        # Convertir de Fahrenheit a Celsius
        resultado = (valor - 32) * 5/9
        return f"{valor}°F es igual a {resultado:.2f}°C"
    elif unidad == 'F':
        # Convertir de Celsius a Fahrenheit
        resultado = (valor * 9/5) + 32
        return f"{valor}°C es igual a {resultado:.2f}°F"
    else:
        return "Unidad no reconocida. Usa 'C' para Celsius o 'F' para Fahrenheit."

# Ejemplos de uso:
temp = int(input(" Ingrese la temperatura que desea convertir:  "))
    
print(convertir_temperatura(temp, 'C'))  # Convertir 100°F a °C
print(convertir_temperatura(temp, 'F'))    # Convertir 0°C a °F

