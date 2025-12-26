from nomina.fijo import Fijo
from nomina.freelancer import Freelancer

nombre = input("Nombre del Trabajador:")
apellido = input("Apellido del Trabajador:")
trabajo = int(input("1 Para FreeLancer y 2 para Empleado fijo"))
empleado = None
if trabajo == 1:
    sueldoFree = float(input("Ingresa tu Tarifa por hora: "))
    horasFree = float(input("Ingresa las horas laboraras "))
    empleado =Freelancer(nombre,apellido,horasFree,sueldoFree)
    empleado.calcular_pago()
elif trabajo == 2:
    sueldoFijo = float(input("Ingresa tu sueldo fijo, antes de impuestos:"))
    empleado = Fijo(nombre,apellido,sueldoFijo)
    empleado.calcular_pago()