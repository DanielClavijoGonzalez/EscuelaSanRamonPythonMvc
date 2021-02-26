from flask.views import MethodView
from flask import jsonify, request
from services import ProfesorService
from services.services import fixStringClient

class ProfesorControllers(MethodView):
    def get(self):
        serviceData = ProfesorService.CrudProfesorService()
        return jsonify(serviceData.getData()), 200

    def post(self):
        serviceData = ProfesorService.CrudProfesorService()
        try:
            jsonRequest = request.get_json(force=True)
            nombre = fixStringClient(jsonRequest['nombre'])
            asignatura = fixStringClient(jsonRequest['asignatura'])
            inserted = serviceData.addData(nombre, asignatura)
            
            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200
        
    def put(self):
        serviceData = ProfesorService.CrudProfesorService()
        try:
            jsonRequest = request.get_json(force=True)
            nombre = fixStringClient(jsonRequest['nombre'])
            asignatura = fixStringClient(jsonRequest['asignatura'])
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.changeData(nombre, asignatura, id)

            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200

    def delete(self):
        serviceData = ProfesorService.CrudProfesorService()
        try:
            jsonRequest = request.get_json(force=True)
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.deleteData(id)

            return jsonify(serviceData.getData()), 200
        except:
            return jsonify(serviceData.getData()), 200
