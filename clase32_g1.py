import funciones as fp

class Contador:
    """
    Clase Contador:
    
    Metodos:
    \n incrementa(): Al llamarlo suma uno a la variable interna cuenta.
    \n decrementar(): Al llamarlo resta uno a la variable interna cuenta.
    \n mostrar_contador(): Al llamarlo imprime por consola el valor actual del contador.
    \n reiniciar(): Al llamarlo vuelve el valor de la variable interna cuenta a 0.
    """
    def __init__(self) -> None:
        self.cuenta = 0 
        
    def incrementar (self):
        self.cuenta += 1
        return
    
    def decrementar (self):
        if self.cuenta > 0:
            self.cuenta -= 1
        else:
            print (f"  ERROR!!!! El contador esta {self.cuenta} ")
        return
    
    def mostrar_contador (self):
        print (f" El valor de contador es: {self.cuenta}")
        return
    
    def reiniciar (self):
        self.cuenta = 0
        return

#Objetivo: Crear una clase llamada Producto 
# que tenga tres atributos: nombre, precio y cantidad. 
# Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total, 
#el primero modificara el precio del producto,
# el segundo la cantidad 
# y el ultimo debera multiplicar la cantidad por el precio del producto seleccionado para saber el valor total del inventario. 
import funciones as fs 


class Producto:
    def __init__(self, nombre: str, precio: int, cantidad: int, calcula_valor: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.calcular_valor_total=calcula_valor
        pass
    def actualizar_precio(self):
        self.actualizar_precio= precio
        return
    def actualizar_cantidad(self):
        self.actualizar_cantidad=cantidad
        return
    def calcular_valor_total(self):
        self.calcular_valor_total= calcula_valor
        return

nombre = fs.validar_texto("Ingrese el nombre del producto: ")
cantidad = int(input( "Ingrese la cantidad: "))
precio = int(input( "Ingrese el precio $ "))
calcula_valor = cantidad * precio

print(nombre)    
mi_producto = Producto()
mi_producto.actualizar_precio()
mi_producto.actualizar_cantidad()
mi_producto.calcular_valor_total()


