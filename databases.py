from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SERVER = "SCALIBY\\SQLEXPRESS"
DATABASE = "Nominas" 

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def probar_conexion():
    try:
        with engine.connect() as connection:
            print("✅ Conexion exitosa a Sql Server")
    except Exception as e:
        print(f"❌ Error al conectarte a la base de datos: {e}")
    
if __name__ == "__main__":
    probar_conexion()