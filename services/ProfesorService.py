from services.services import dataTableMysql

class CrudProfesorService:
    def getData(self):
        try:
            data = dataTableMysql("SELECT * FROM profesores")
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'id': col[0],
                    'nombre': col[1],
                    'asignatura': col[2]
                    })
            return jsonResponse
        except :
            return [{'id': -1, 'nombre': 'Not found data', 'asignatura': 'Not found data'}]

    def addData(self, nombre, asignatura):
        try:
            return dataTableMysql("INSERT INTO profesores(nombre, asignatura) VALUES('{}','{}')".format(nombre, asignatura), "rowcount")
        except :
            return False

    def changeData(self, nombre, asignatura, id):
        try:
            return dataTableMysql("UPDATE profesores SET nombre = '{}', asignatura = '{}' WHERE id = '{}'".format(nombre, asignatura, id), "rowcount")
        except :
            return False

    def deleteData(self, id):
        try:
            return dataTableMysql("DELETE FROM profesores WHERE id = '{}'".format(id), "rowcount")
        except:
            return False