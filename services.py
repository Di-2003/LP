from typing import List, Optional
from models import Estudiante
import database
import validations
from functools import reduce

estudiantes_cache = []
async def cargar_cache():
    global estudiantes_cache
    estudiantes_db=await database.obtener_todos_estudiantes()
    estudiantes_cache.clear()
    estudiantes_cache.extend(estudiantes_db)
def normalizar_nombre(nombre: str) -> str:
    return " ".join(part.capitalize() for part in nombre.split())

def calcular_promedio_general(estudiantes: List[Estudiante]) -> float:
    if not estudiantes:
        return 0.0
    total = reduce(lambda acc, e: acc + e.promedio, estudiantes, 0.0)
    return total / len(estudiantes)


def buscar_estudiante_por_id(id: int, estudiantes: List[Estudiante]) -> Optional[Estudiante]:
    def buscar_rec(lista, index=0):
        if index >= len(lista):
            return None
        if lista[index].id == id:
            return lista[index]
        return buscar_rec(lista, index + 1)

    return buscar_rec(estudiantes)


def estudiantes_con_promedio_alto(estudiantes: List[Estudiante]) -> List[Estudiante]:
    return list(filter(lambda e: e.promedio >= 4.0, estudiantes))
async def crear_estudiante(
        nombre: str,
        carrera: str,
        año_ingreso: int,
        promedio: float
):
    global estudiantes_cache
    estudiante = Estudiante(
        nombre=nombre,
        carrera=carrera,
        año_ingreso=año_ingreso,
        promedio=promedio
    )
    estudiante.nombre = normalizar_nombre(estudiante.nombre)
    error = validations.validar_estudiante(estudiante)
    if error:
        raise ValueError(error)

    id_generado = await database.guardar_estudiante(estudiante)

    estudiante.id = id_generado

    estudiantes_cache.append(estudiante)
    return estudiante


async def actualizar_estudiante(
        id: int,
        nombre: str,
        carrera: str,
        año_ingreso: int,
        promedio: float
):
    global estudiantes_cache
    estudiante_existente = buscar_estudiante_por_id(id, estudiantes_cache)
    if not estudiante_existente:
        raise ValueError("Estudiante no encontrado")

    estudiante_actualizado = Estudiante(
        id=id,
        nombre=nombre,
        carrera=carrera,
        año_ingreso=año_ingreso,
        promedio=promedio
    )
    estudiante_actualizado.nombre = normalizar_nombre(estudiante_actualizado.nombre)
    error = validations.validar_estudiante(estudiante_actualizado)
    if error:
        raise ValueError(error)

    await database.actualizar_estudiante(estudiante_actualizado)
    for i, e in enumerate(estudiantes_cache):
        if e.id == id:
            estudiantes_cache[i] = estudiante_actualizado
            break

    return estudiante_actualizado


async def eliminar_estudiante(id: int):
    global estudiantes_cache
    estudiante = buscar_estudiante_por_id(id, estudiantes_cache)
    if not estudiante:
        raise ValueError("Estudiante no encontrado")
    await database.eliminar_estudiante(id)
    estudiantes_cache = [e for e in estudiantes_cache if e.id != id]
    return f"Estudiante {estudiante.nombre} eliminado"


def estudiantes_por_carrera(carrera: str) -> List[Estudiante]:
    return list(filter(
        lambda e: e.carrera.lower() == carrera.lower(),
        estudiantes_cache
    ))


def buscar_mejores_estudiantes(
        carrera: str = None,
        año_min: int = 2020
) -> List[Estudiante]:
    resultados = estudiantes_cache
    if carrera:
        resultados = filter(lambda e: e.carrera.lower() == carrera.lower(), resultados)
    resultados = filter(lambda e: e.año_ingreso >= año_min, resultados)
    resultados = filter(lambda e: e.promedio >= 4.0, resultados)
    return sorted(resultados, key=lambda e: e.promedio, reverse=True)
