from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.domain.schemas.movie_schemas import MovieSchemaCreate, MovieSchema
from app.api.deps import get_movie_service

# Creamos un 'Blueprint' de Flask para organizar nuestras rutas
movie_router = Blueprint('movies', __name__)

@movie_router.route('/movies', methods=['POST'])
def create_movie_endpoint():
    """
    Endpoint para crear una nueva película.
    """
    # 1. Obtenemos el servicio con todas sus dependencias
    service_generator = get_movie_service()
    movie_service = next(service_generator)
    
    try:
        # 2. Validamos los datos de entrada con el schema
        movie_data = MovieSchemaCreate.model_validate(request.json)
        
        # 3. Llamamos al servicio para ejecutar el caso de uso
        new_movie = movie_service.create_movie(movie_data)
        
        # 4. Convertimos la respuesta a un schema de salida y la devolvemos
        return jsonify(MovieSchema.model_validate(new_movie).model_dump()), 201

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Cerramos el generador y la sesión de la base de datos
        next(service_generator, None)