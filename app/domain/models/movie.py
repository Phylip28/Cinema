from dataclasses import dataclass
from typing import Optional
import datetime

# Excepción personalizada para errores de negocio
class MovieValidationError(Exception):
    pass

@dataclass
class Movie:
    """
    Esta clase representa la ENTIDAD 'Película'.
    Su ÚNICA RESPONSABILIDAD es definir qué es una película y
    cuáles son sus reglas de negocio.
    """
    title: str
    director: str
    year: int
    rating: float
    id: Optional[int] = None # El ID no existe hasta que se guarda

    def __post_init__(self):
        """ Se asegura que una película nunca pueda tener datos inválidos. """
        if not self.title or not self.director:
            raise MovieValidationError("El título y el director no pueden estar vacíos.")
        if not (1888 <= self.year <= datetime.date.today().year + 2):
            raise MovieValidationError(f"Año inválido: {self.year}.")
        if not (0.0 <= self.rating <= 10.0):
            raise MovieValidationError(f"La calificación debe estar entre 0.0 y 10.0.")