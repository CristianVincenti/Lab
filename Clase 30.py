# Ejercicio 1
# Crear una clase llamada Rectangullo
# Que tenga 2 atributos: ancho y alto.
# Que tenga 2 metodos: area y perimetro.

""" 
class MiClase:
    def __init__(self) -> None:
        pass
    def mi_funcion(self):
        variable = " Hola Mundo"
        return variable
    
#variable = mi_funcion()
objeto = MiClase()
print (objeto.mi_funcion().capitalize())

"""
import funciones as f
class Rectangulo:
    def __init__(self)-> None:
        self.alto = f.numero (" Ingrese el alto: ")
        self.ancho = f.numero ( " Ingrese el ancho: ")
        pass

    def area (self):
        calculo_area = self.ancho * self.alto
        return calculo_area 
    
    def perimetro (self):
        calculo_perimetro = (self.ancho + self.alto) * 2
        return calculo_perimetro
    
    def caracteristica (self):
        print (f" El alto del rectangulo es {self.alto} y el ancho del rectangulo es {self.ancho}")
        print (f" El area del rectangulo es {self.area()} y el perimetro del rectangulo es {self.perimetro()}")
        return

Valores_rectangulo = Rectangulo ()
Valores_rectangulo.caracteristica()


