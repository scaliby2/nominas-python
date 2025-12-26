from fastapi import FastAPI
from nomina.fijo import Fijo
from nomina.freelancer import Freelancer

app = FastAPI()

@app.get("/")
def home():
    return{"Sistema": "Nomina v 1.0", "Estado" : "Funcionando"}

@app.get("/empleadofijo")
def Calcular_fijo(nombre: str, apellido: str, sueldo: float):
    try:
        empleado = Fijo(nombre,apellido,sueldo)
        mensaje_pago = empleado.calcular_pago()     
        return {
            "Status": "ok",
            "Tipo" : "Empleado Fijo",
            "Nombre_Completo" : f"{nombre} {apellido}",
            "Resultado" : mensaje_pago
        }
    except ValueError as e:
        return {"status" : "error", "mensaje" : str(e)}

@app.get("/empleadofree")
def calcular_free(nombre : str, apellido:str, horas: float, tarifa: float ):
    try:
        empleado = Freelancer(nombre,apellido,horas,tarifa)
        mensaje_pago = empleado.calcular_pago()
        
        return{
            "Status": "ok",
            "Tipo" : "Empleado FreeLancer",
            "Nombre Completo" : f"{nombre} {apellido}",
            "Resultado" : mensaje_pago
        }
    except ValueError as e:
        return {"Status": "error", "mensaje": str(e)}