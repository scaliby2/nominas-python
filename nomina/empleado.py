from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__()
    
    @abstractmethod
    def calcular_pago(self):
        pass
    
    @property
    def nombre(self):
        return self._nombre 
    
    @nombre.setter
    def nombre(self,valor):
        if valor == "":
            raise ValueError("Cadena Vacia, por favor ingresa un nombre")
        self._nombre = valor
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,valor):
        if valor == "":
            raise ValueError("Cadena Vacia, por favor ingresa un nombre")
        self._apellido = valor
    