"""

edad = int(input("Cuantos años tienes?:  "))
if edad >= 18 and edad <=20:
    print (" Puedes entrar al boliche")
elif edad >= 21 and edad <= 49:
    print (" Puedes entrar al boliche y toamr alcohol")
elif edad >=50:
    print ("Andate a dormir")
else:
    print(" No puedes entrar la boliche")
"""

class Persona:
    def __init__(self, nombre: str, edad: int, profesion: str, ) -> None: #Excelente uso de decoradores
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        pass
    

    def mayor(self):
        if self.edad >= 18: #Falto el =, deberia ser >= 18 o bien > 17 ya que con 18 años sos mayor de edad.
            print(f" {self.nombre} es mayor de edad")
        else:
            print(" Es menor de edad")
    
datos_personales = Persona("Gaspar", 18, "Profesor")
datos_personales1= Persona("Diego", 45, "desarrollador de software")
datos_personales2= Persona("Cristian", 48, "Adminitrativo")
datos_personales.mayor()
datos_personales1.mayor()
datos_personales2.mayor()