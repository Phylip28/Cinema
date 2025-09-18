from pydantic import BaseModel, Field, ConfigDict

class MovieSchemaBase(BaseModel):
    """ Schema base para no repetir código."""
    title: str = Field(..., min_length=1)
    director: str = Field(..., min_length=1)
    year: int = Field(..., gt=1888)
    rating: float = Field(..., ge=0.0, le=10.0)

class MovieSchemaCreate(MovieSchemaBase):
    """
    Este es el 'formulario' para CREAR una película.
    El cliente no nos envía el id.
    """
    pass

class MovieSchema(MovieSchemaBase):
    """
    Este es el formulario para MOSTRAR una película.
    Este sí incluye el 'id', porque ya existe en el sistema.
    """
    id: int
    
    # Esto le permite a Pydantic leer datos desde nuestro objeto Movie
    model_config = ConfigDict(from_attributes=True)