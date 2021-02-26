from services.services import dataTableMysql

class CrudEstudianteService:
    def getData(self):
        try:
            data = dataTableMysql("SELECT * FROM estudiantes")
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'id': col[0],
                    'nombres': col[1],
                    'curso': col[2],
                    'documento_identidad': col[3]
                })
            return jsonResponse
        except :
            return [{'id': -1, 'nombres': 'Not found data', 'curso': -1, "documento_identidad": -1}]

    def addData(self, nombres, curso, documento_identidad):
        try:
            return dataTableMysql("INSERT INTO estudiantes(nombres, curso, documento_identidad) VALUES('{}', '{}', '{}')".format(nombres, curso, documento_identidad), "rowcount")
        except :
            return False

    def changeData(self, nombres, curso, documento_identidad, id):
        try:
            return dataTableMysql("UPDATE estudiantes SET nombres = '{}', curso = '{}', documento_identidad = '{}' WHERE id = '{}'".format(nombres, curso, documento_identidad, id), "rowcount")
        except :
            return False

    def deleteData(self, id):
        try:
            return dataTableMysql("DELETE FROM estudiantes WHERE id = '{}'".format(id), "rowcount")
        except:
            return False