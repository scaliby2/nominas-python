from nomina.empleado import Empleado
class Freelancer(Empleado):
    def __init__(self, nombre, apellido,horas_trabajadas,tarifa_hora):
        super().__init__(nombre, apellido)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
    
    @property
    def horas_trabajadas(self):
        return self._horas_trabajadas
    
    @horas_trabajadas.setter
    def horas_trabajadas(self,valor):
        if valor < 0:
            raise ValueError("Valores incorrectos, por favor ingrese valores mayores a 0")
        self._horas_trabajadas = valor
    
    @property
    def tarifa_hora(self):
        return self._tarifa_hora
    
    @tarifa_hora.setter
    def tarifa_hora(self,valor):
        if valor < 0:
            raise ValueError("Valores incorrectos, por favor ingrese valores mayores a 0")
        self._tarifa_hora = valor
    
    def calcular_pago(self):
        return f"Hola, mi nombre es:{self.nombre} y gane {self.horas_trabajadas * self.tarifa_hora}."
        