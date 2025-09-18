from app.infrastructure.database.session import SessionLocal
from app.infrastructure.repositories.movie_repository import MovieRepository
from app.services.movie_service import MovieService

def get_movie_service():
    """
    Función de inyección de dependencias.
    Crea todas las dependencias necesarias (sesión de BD, repositorio)
    y las provee al servicio.
    """
    db_session = SessionLocal()
    try:
        repo = MovieRepository(db_session)
        service = MovieService(repo)
        yield service
    finally:
        db_session.close()