from services.services import dataTableMysql

class CrudNotasService:
    def getData(self):
        try:
            data = dataTableMysql("SELECT * FROM notas")
            jsonResponse = []
            for col in data:
                jsonResponse.append({
                    'id': col[0],
                    'nota1': col[1],
                    'nota2': col[2],
                    'nota3': col[3],
                    'nota4': col[4],
                    'estudiante': col[5],
                    'materia': col[6],
                    'promedio': (col[1] + col[2] + col[3] + col[4]) / 4
                })
            return jsonResponse
        except :
            return [{'id': -1,'nota1': -1,'nota2': -1, 'nota3': -1, 'nota4': -1, 'estudiante': -1, 'materia': -1, 'promedio': -1}]

    def addData(self, nota1, nota2, nota3, nota4, estudiante, materia):
        try:
            return dataTableMysql("INSERT INTO notas(nota1, nota2, nota3, nota4, estudiante, materia) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(nota1, nota2, nota3, nota4, estudiante, materia), "rowcount")
        except :
            return False

    def changeData(self, nota1, nota2, nota3, nota4, estudiante, materia, id):
        try:
            return dataTableMysql("UPDATE notas SET nota1 = '{}', nota2 = '{}', nota3 = '{}', nota4 = '{}', estudiante = '{}', materia = '{}' WHERE id = '{}'".format(nota1, nota2, nota3, nota4, estudiante, materia, id), "rowcount")
        except :
            return False

    def deleteData(self, id):
        try:
            return dataTableMysql("DELETE FROM notas WHERE id = '{}'".format(id), "rowcount")
        except:
            return False