#Objetivo: Crear una clase llamada Contador
#que tenga un atributo cuenta que empieza en 0. 
#Y que posea 4 metodos,
#Incrementar (sumara 1)
# Decrementar (restara 1, no admite negayivos osea hasta maximo 0). 
#Mostar Contador (debera devolver el valor actual de contador)
#Reiniciar (volvera a cero el contador)

class Contador:
    def __init__(self) -> None:
        self.cuenta = 0
        self.cantidad_usado = 0
        
    def incrementar (self):
        self.cuenta += 1
        self.cantidad_usado +=1
        return
    
    def decrementar (self):
        self.cantidad_usado +=1
        if self.cuenta > 0:
            self.cuenta -= 1
        else:
            print(f" Error !!!El contador esta en {self.cuenta}")
        return
    
    def mostrar_contador (self):
        self.cantidad_usado +=1
        print( f" El valor actual del contador es {self.cuenta}")
        return

    def reiniciar (self):
        self.cantidad_usado +=1
        self.cuenta=0
        return
    
    def mostrar_cantidad_usado(self):
        print(f"La cantidad de veces que se utilizo fue {self.cantidad_usado}")
        return
    
    
    
mi_contador = Contador()
mi_contador.decrementar()   
mi_contador.mostrar_contador()
mi_contador.incrementar()
mi_contador.mostrar_contador()
mi_contador.incrementar()
mi_contador.mostrar_contador()
mi_contador.decrementar()
mi_contador.mostrar_contador()
mi_contador.decrementar()
mi_contador.mostrar_contador()
mi_contador.reiniciar()
mi_contador.mostrar_cantidad_usado()

