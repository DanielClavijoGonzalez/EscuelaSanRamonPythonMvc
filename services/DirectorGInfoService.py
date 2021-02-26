from services.services import dataTableMysql

class CrudDirectorGInfoService:
    def getData(self, id):
        try:
            data = dataTableMysql("SELECT p.nombre AS nombre_profesor, p.asignatura, c.grado AS grado_encargado FROM profesores p, cursos c WHERE c.profesor_encargado = p.id and p.id = '{}'".format(id))
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'nombre_profesor': col[0],
                    'asignatura': col[1],
                    'grado_encargado': col[2]
                })
            return jsonResponse
        except :
            return [{'nombre_profesor': 'Not found data', 'asignatura': 'Not found data', 'grado_encargado': -1}]
