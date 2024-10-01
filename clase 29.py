#Definiendo Objetos

class Vehiculo:
    """
    Clase de Vehiculo
    """
    def __init__(self,nombre_propietario:str,color: str, marca: str, modelo: str, cantidad_puertas: int | None = "Diego") -> None:
        self.nombre_propietario = nombre_propietario 
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.cantidad_puertas = cantidad_puertas

    def detalle(self) -> str:
        """
        me devuelve el detalle del vehiculo
                
        """
        print (f"El color del auto de {self.nombre_propietario} marca {self.marca} modelo {self.modelo} es: {self.color}")    
    
auto_diego = Vehiculo(" rojo", " ferrari", "testarrosa", 2, "Diego")
auto_diego.detalle()

auto_franco = Vehiculo(" verde", " ford", "taunus", 4, "Franco")
auto_franco.detalle()
propietario = auto_franco. nombre_propietario
print (f" El propietario es {propietario}")
