from sqlalchemy.orm import Session
from typing import List, Optional

# Importamos tanto el modelo de dominio como el modelo de la BD
from app.domain.models.movie import Movie
from app.infrastructure.database.db_models import MovieDB

class MovieRepository:
    """
    El Repositorio se encarga de la comunicación directa con la base de datos.
    Actúa como un traductor entre los objetos de dominio (Movie) y los
    modelos de la base de datos (MovieDB).
    """
    def __init__(self, db: Session):
        self.db = db

    def create(self, movie: Movie) -> Movie:
        # 1. TRADUCCIÓN: Convertimos el objeto de dominio 'Movie'
        #    en un objeto de base de datos 'MovieDB'.
        db_movie = MovieDB(
            title=movie.title,
            director=movie.director,
            year=movie.year,
            rating=movie.rating
        )
        
        # 2. PERSISTENCIA: Usamos SQLAlchemy para guardar en la BD.
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)
        
        # 3. DEVOLUCIÓN: Devolvemos el objeto de dominio original,
        #    ahora actualizado con el ID de la base de datos.
        movie.id = db_movie.id
        return movie

    def get_by_id(self, movie_id: int) -> Optional[Movie]:
        # 1. CONSULTA: Buscamos en la base de datos el objeto MovieDB.
        db_movie = self.db.query(MovieDB).filter(MovieDB.id == movie_id).first()
        if not db_movie:
            return None
        
        # 2. TRADUCCIÓN: Si lo encontramos, lo convertimos a nuestro
        #    objeto de dominio 'Movie'.
        return Movie(
            id=db_movie.id,
            title=db_movie.title,
            director=db_movie.director,
            year=db_movie.year,
            rating=db_movie.rating
        )

    def get_all(self) -> List[Movie]:
        db_movies = self.db.query(MovieDB).all()
        
        # Convertimos cada MovieDB de la lista en un objeto Movie de dominio
        return [
            Movie(
                id=db_movie.id,
                title=db_movie.title,
                director=db_movie.director,
                year=db_movie.year,
                rating=db_movie.rating
            ) for db_movie in db_movies
        ]