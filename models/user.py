from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int
    userName: str
    email: str
    name: str
    lastName: str
    birthDate: date