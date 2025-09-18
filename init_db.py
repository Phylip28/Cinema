import sys
from app.infrastructure.database.db_models import Base
from app.infrastructure.database.session import engine

def init_database():
    """
    Crea las tablas en la base de datos, pidiendo confirmación primero.
    """
    # 1. Pide confirmación al usuario
    confirm = input("¿Estás seguro de que deseas inicializar la base de datos y crear las tablas? (y/n): ")

    # 2. Verifica la respuesta
    if confirm.lower().strip() == 'y':
        print("Creando tablas en la base de datos...")
        # La función create_all no recreará tablas que ya existen, es segura.
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas exitosamente.")
    else:
        print("Operación cancelada por el usuario.")
        sys.exit() # 3. Cancela la ejecución si no se confirma

if __name__ == "__main__":
    init_database()