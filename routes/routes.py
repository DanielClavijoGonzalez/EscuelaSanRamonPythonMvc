from controllers.ProfesorController import ProfesorControllers
from controllers.EstudianteController import EstudianteControllers
from controllers.CursoController import CursoControllers
from controllers.MateriasController import MateriasControllers
from controllers.NotasController import NotasControllers
from controllers.DirectorGInfoController import DirectorGInfoControllers
from controllers.NotasEstudiantesController import NotasEstudiantesControllers

profesor = {
    "profesor_route": "/api/v1/profesor", "profesor_controllers": ProfesorControllers.as_view("profesor_api"),
    "director_g_info_route": "/api/v1/directorginfo", "director_g_info_controllers": DirectorGInfoControllers.as_view("director_g_info_api")
}

estudiante = {
    "estudiante_route": "/api/v1/estudiante", "estudiante_controllers": EstudianteControllers.as_view("estudiante_api")
}

curso = {
    "curso_route": "/api/v1/curso", "curso_controllers": CursoControllers.as_view("curso_api")
}

materias = {
    "materias_route": "/api/v1/materias", "materias_controllers": MateriasControllers.as_view("materias_api")
}

notas = {
    "notas_route": "/api/v1/notas", "notas_controllers": NotasControllers.as_view("notas_api"),
    "notas_estudiantes_route": "/api/v1/notasestudiantes", "notas_estudiantes_controllers": NotasEstudiantesControllers.as_view("notas_estudiantes_api")
}