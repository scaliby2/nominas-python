from nomina.empleado import Empleado

class Fijo(Empleado):
    def __init__(self, nombre, apellido,sueldo_base):
        super().__init__(nombre, apellido)   
        self.sueldo_base = sueldo_base

    
    @property
    def sueldo_base(self):
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self,valor):
        if valor <= 0:
            raise ValueError("El sueldo es menor o igual a 0, tienes que ingresar un valor a corde al programa")
        self._sueldo_base = valor    
        
    def calcular_pago(self):
        return f"Hola, mi nombre es {self.nombre} {self.apellido} y mi sueldo fijo es {self.sueldo_base}"
