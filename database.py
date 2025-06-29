import aiomysql
from models import Estudiante


async def conectar_bd():
    """Conexión asíncrona a MySQL"""
    return await aiomysql.connect(
        host='localhost',
        user='postgres',
        password='edirac-747',
        db='universidad_db',
        cursorclass=aiomysql.DictCursor
    )


async def guardar_estudiante(estudiante: Estudiante) -> int:
    """Operación asíncrona para guardar estudiante (retorna ID generado)"""
    conn = await conectar_bd()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "INSERT INTO estudiantes (nombre, carrera, año_ingreso, promedio) "
                "VALUES (%s, %s, %s, %s)",
                (estudiante.nombre, estudiante.carrera,
                 estudiante.año_ingreso, estudiante.promedio)
            )
            await conn.commit()
            return cursor.lastrowid
    except Exception as e:
        print(f"Error de base de datos: {str(e)}")
        raise
    finally:
        conn.close()


async def obtener_estudiante_por_id(id: int) -> Estudiante:
    """Obtener estudiante por ID"""
    conn = await conectar_bd()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "SELECT * FROM estudiantes WHERE id = %s",
                (id,)
            )
            resultado = await cursor.fetchone()
            return Estudiante(**resultado) if resultado else None
    finally:
        conn.close()


async def actualizar_estudiante(estudiante: Estudiante):
    """Actualización asíncrona de estudiante"""
    if not estudiante.id:
        raise ValueError("ID de estudiante requerido para actualización")

    conn = await conectar_bd()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "UPDATE estudiantes SET nombre = %s, carrera = %s, año_ingreso = %s, promedio = %s "
                "WHERE id = %s",
                (estudiante.nombre, estudiante.carrera, estudiante.año_ingreso,
                 estudiante.promedio, estudiante.id)
            )
            await conn.commit()
    finally:
        conn.close()


async def eliminar_estudiante(id: int):
    """Eliminación asíncrona de estudiante"""
    conn = await conectar_bd()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "DELETE FROM estudiantes WHERE id = %s",
                (id,)
            )
            await conn.commit()
    finally:
        conn.close()


async def obtener_todos_estudiantes() -> list:
    """Obtener todos los estudiantes"""
    conn = await conectar_bd()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM estudiantes")
            return [Estudiante(**row) for row in await cursor.fetchall()]
    finally:
        conn.close()
