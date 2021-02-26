from services.services import dataTableMysql

class CrudNotasEstudiantesService:
    def getData(self, id):
        try:
            data = dataTableMysql("SELECT e.nombres AS nombre_estudiante, n.nota1, n.nota2, n.nota3, n.nota4, m.nombre_materia, p.nombre AS profesor_encargado FROM estudiantes e, notas n, profesores p, materias m WHERE e.id = n.estudiante AND p.id = m.profesor AND n.materia = m.id AND e.documento_identidad = '{}'".format(id))
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'nombre_estudiante': col[0],
                    'nota1': col[1],
                    'nota2': col[2],
                    'nota3': col[3],
                    'nota4': col[4],
                    'nombre_materia': col[5],
                    'profesor_encargado': col[6]
                })
            return jsonResponse
        except :
            return [{'nombre_estudiante': 'Not found data',
            'nota1': -1,
            'nota2': -1,
            'nota3': -1,
            'nota4': -1,
            'nombre_materia': 'Not found data',
            'profesor_encargado': 'Not found data'}]
