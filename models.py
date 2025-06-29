from pydantic import BaseModel
from typing import Optional


class Estudiante(BaseModel):
    """Modelo de datos para estudiantes"""
    id: Optional[int] = None
    nombre: str
    carrera: str
    año_ingreso: int
    promedio: float
