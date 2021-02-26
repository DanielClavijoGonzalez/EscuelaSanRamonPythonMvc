from services.services import dataTableMysql

class CrudCursoService:
    def getData(self):
        try:
            data = dataTableMysql("SELECT * FROM cursos")
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'id': col[0],
                    'profesor_encargado': col[1],
                    'grado': col[2]
                })
            return jsonResponse
        except :
            return [{'id': -1, 'profesor_encargado': -1, 'grado': -1}]

    def addData(self, profesor_encargado, grado):
        try:
            return dataTableMysql("INSERT INTO cursos(profesor_encargado, grado) VALUES('{}', '{}')".format(profesor_encargado, grado), "rowcount")
        except :
            return False

    def changeData(self, profesor_encargado, grado, id):
        try:
            return dataTableMysql("UPDATE cursos SET profesor_encargado = {}, grado = '{}' WHERE id = '{}'".format(profesor_encargado, grado, id), "rowcount")
        except :
            return False

    def deleteData(self, id):
        try:
            return dataTableMysql("DELETE FROM cursos WHERE id = '{}'".format(id), "rowcount")
        except:
            return False