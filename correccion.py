class Producto:
    def __init__(self, nombre: str, precio: int, cantidad: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: int) -> None:
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> int:
        return self.precio * self.cantidad

# Pedir información al usuario
nombre = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio = int(input("Ingrese el precio $ "))

# Crear una instancia de Producto
mi_producto = Producto(nombre, precio, cantidad)

# Actualizar el precio o la cantidad si es necesario (ejemplo)
nuevo_precio = int(input("Ingrese el nuevo precio $ "))
mi_producto.actualizar_precio(nuevo_precio)

nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
mi_producto.actualizar_cantidad(nueva_cantidad)

# Calcular y mostrar el valor total
valor_total = mi_producto.calcular_valor_total()
print(f"El valor total de {mi_producto.nombre} es: ${valor_total}")
