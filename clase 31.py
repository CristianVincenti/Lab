# Objetivo: Implementar una clase Bancaria
# que permita a los usuarios realizar operaciones bancarias basicas
# como depositar, retirar y consultar el saldo.
import funciones as f

class CuentaBancaria:
    def __init__(self, saldo: int |None = 0, titular: str | None = "") -> None:
        self.saldo = saldo
        self.titular= titular
        pass
    def ingresar_dinero (self):
        ingreso_dinero = f.numero (" Ingrese la cantidad a ingresar")