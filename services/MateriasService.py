from services.services import dataTableMysql

class CrudMateriasService:
    def getData(self):
        try:
            data = dataTableMysql("SELECT * FROM materias")
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'id': col[0],
                    'nombre_materia': col[1],
                    'profesor': col[2]
                })
            return jsonResponse
        except :
            return [{'id': -1, 'nombre_materia': 'Not found data', 'profesor': -1}]

    def addData(self, nombre_materia, profesor):
        try:
            return dataTableMysql("INSERT INTO materias(nombre_materia, profesor) VALUES('{}', '{}')".format(nombre_materia, profesor), "rowcount")
        except :
            return False

    def changeData(self, nombre_materia, profesor, id):
        try:
            return dataTableMysql("UPDATE materias SET nombre_materia = '{}', profesor = '{}' WHERE id = '{}'".format(nombre_materia, profesor, id), "rowcount")
        except :
            return False

    def deleteData(self, id):
        try:
            return dataTableMysql("DELETE FROM materias WHERE id = '{}'".format(id), "rowcount")
        except:
            return False