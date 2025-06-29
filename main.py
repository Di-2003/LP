import asyncio
import services
import sys


async def main():
    try:
        nuevo_estudiante = await services.crear_estudiante(
            nombre="juan rodriguez",
            carrera="Ingeniería Informática",
            año_ingreso=2021,
            promedio=4.3
        )
        print(f"Estudiante creado: ID={nuevo_estudiante.id}, Nombre={nuevo_estudiante.nombre}")

        estudiante_actualizado = await services.actualizar_estudiante(
            id=nuevo_estudiante.id,
            nombre="Juan Carlos Rodríguez",
            carrera="Ingeniería Informática",
            año_ingreso=2021,
            promedio=4.5
        )
        print(f"Estudiante actualizado: Nuevo promedio={estudiante_actualizado.promedio}")
        mejores = services.buscar_mejores_estudiantes(
            carrera="Ingeniería Informática",
            año_min=2020
        )
        print("\nMejores estudiantes de Ingeniería Informática:")
        for e in mejores:
            print(f"- {e.nombre}: Promedio {e.promedio}")
        resultado = await services.eliminar_estudiante(nuevo_estudiante.id)
        print(f"\n{resultado}")

    except ValueError as e:
        print(f"Error de validación: {str(e)}", file=sys.stderr)
    except Exception as e:
        print(f"Error inesperado: {str(e)}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
