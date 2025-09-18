from app.domain.models.movie import Movie
from app.domain.schemas.movie_schemas import MovieSchemaCreate
from app.infrastructure.repositories.movie_repository import MovieRepository

class MovieService:
    """
    Esta clase contiene la lógica de negocio de la aplicación (casos de uso).
    Orquesta las operaciones, utilizando el repositorio para el acceso a datos
    y los modelos de dominio para representar la lógica de negocio.
    """
    def __init__(self, movie_repository: MovieRepository):
        # El servicio DEPENDE de una abstracción (el repositorio),
        # no de una implementación concreta. Esto es la "D" de SOLID.
        self.movie_repository = movie_repository

    def create_movie(self, movie_data: MovieSchemaCreate) -> Movie:
        """
        Caso de uso: Crear una nueva película.
        """
        # 1. Creamos una entidad de dominio a partir de los datos del schema.
        #    La validación de negocio ocurre dentro del modelo Movie.
        new_movie = Movie(
            title=movie_data.title,
            director=movie_data.director,
            year=movie_data.year,
            rating=movie_data.rating
        )
        
        # 2. Le pedimos al repositorio que persista la nueva película.
        return self.movie_repository.create(new_movie)

    def get_movie_by_id(self, movie_id: int) -> Movie | None:
        """
        Caso de uso: Obtener una película por su ID.
        """
        return self.movie_repository.get_by_id(movie_id)
    
    def get_all_movies(self) -> list[Movie]:
        """Caso de uso: Obtener todas las películas."""
        return self.movie_repository.get_all()