from flask.views import MethodView
from flask import jsonify, request
from services import NotasService
from services.services import fixStringClient

class NotasControllers(MethodView):
    def get(self):
        serviceData = NotasService.CrudNotasService()
        return jsonify(serviceData.getData()), 200

    def post(self):
        serviceData = NotasService.CrudNotasService()
        try:
            jsonRequest = request.get_json(force=True)
            nota1 = fixStringClient(jsonRequest['nota1'])
            nota2 = fixStringClient(jsonRequest['nota2'])
            nota3 = fixStringClient(jsonRequest['nota3'])
            nota4 = fixStringClient(jsonRequest['nota4'])
            estudiante = fixStringClient(jsonRequest['estudiante'])
            materia = fixStringClient(jsonRequest['materia'])
            inserted = serviceData.addData(nota1, nota2, nota3, nota4, estudiante, materia)
            
            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200
        
    def put(self):
        serviceData = NotasService.CrudNotasService()
        try:
            jsonRequest = request.get_json(force=True)
            nota1 = fixStringClient(jsonRequest['nota1'])
            nota2 = fixStringClient(jsonRequest['nota2'])
            nota3 = fixStringClient(jsonRequest['nota3'])
            nota4 = fixStringClient(jsonRequest['nota4'])
            estudiante = fixStringClient(jsonRequest['estudiante'])
            materia = fixStringClient(jsonRequest['materia'])
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.changeData(nota1, nota2, nota3, nota4, estudiante, materia, id)

            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200

    def delete(self):
        serviceData = NotasService.CrudNotasService()
        try:
            jsonRequest = request.get_json(force=True)
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.deleteData(id)

            return jsonify(serviceData.getData()), 200
        except:
            return jsonify(serviceData.getData()), 200
