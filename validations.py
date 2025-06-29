from datetime import datetime
from models import Estudiante


def validar_estudiante(estudiante: Estudiante) -> str:
    if len(estudiante.nombre.split()) < 2:
        return "Nombre inválido: debe contener nombre y apellido"

    año_actual = datetime.now().year
    if estudiante.año_ingreso < 1950:
        return "Año de ingreso inválido: la universidad fue fundada en 1950"
    if estudiante.año_ingreso > año_actual:
        return f"Año de ingreso inválido: no puede ser mayor a 2025"

    if estudiante.promedio < 0:
        return "Promedio inválido: no puede ser negativo"
    if estudiante.promedio > 5.0:
        return "Promedio inválido: escala máxima es 5.0"

    # Validar carrera
    carreras_validas = ["Ingeniería Informática", "Medicina", "Derecho", "Administración"]
    if estudiante.carrera not in carreras_validas:
        return f"Carrera inválida. Opciones válidas: {', '.join(carreras_validas)}"

    return None
