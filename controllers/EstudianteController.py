from flask.views import MethodView
from flask import jsonify, request
from services import EstudianteService
from services.services import fixStringClient

class EstudianteControllers(MethodView):
    def get(self):
        serviceData = EstudianteService.CrudEstudianteService()
        return jsonify(serviceData.getData()), 200

    def post(self):
        serviceData = EstudianteService.CrudEstudianteService()
        try:
            jsonRequest = request.get_json(force=True)
            nombres = fixStringClient(jsonRequest['nombres'])
            curso = fixStringClient(jsonRequest['curso'])
            documento_identidad = fixStringClient(jsonRequest['documento_identidad'])
            inserted = serviceData.addData(nombres, curso, documento_identidad)
            
            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200
        
    def put(self):
        serviceData = EstudianteService.CrudEstudianteService()
        try:
            jsonRequest = request.get_json(force=True)
            nombres = fixStringClient(jsonRequest['nombres'])
            curso = fixStringClient(jsonRequest['curso'])
            documento_identidad = fixStringClient(jsonRequest['documento_identidad'])
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.changeData(nombres, curso, documento_identidad, id)

            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200

    def delete(self):
        serviceData = EstudianteService.CrudEstudianteService()
        try:
            jsonRequest = request.get_json(force=True)
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.deleteData(id)

            return jsonify(serviceData.getData()), 200
        except:
            return jsonify(serviceData.getData()), 200
