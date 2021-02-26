from flask.views import MethodView
from flask import jsonify, request
from services import MateriasService
from services.services import fixStringClient

class MateriasControllers(MethodView):
    def get(self):
        serviceData = MateriasService.CrudMateriasService()
        return jsonify(serviceData.getData()), 200

    def post(self):
        serviceData = MateriasService.CrudMateriasService()
        try:
            jsonRequest = request.get_json(force=True)
            nombre_materia = fixStringClient(jsonRequest['nombre_materia'])
            profesor = fixStringClient(jsonRequest['profesor'])
            inserted = serviceData.addData(nombre_materia, profesor)
            
            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200
        
    def put(self):
        serviceData = MateriasService.CrudMateriasService()
        try:
            jsonRequest = request.get_json(force=True)
            nombre_materia = fixStringClient(jsonRequest['nombre_materia'])
            profesor = fixStringClient(jsonRequest['profesor'])
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.changeData(nombre_materia, profesor, id)

            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200

    def delete(self):
        serviceData = MateriasService.CrudMateriasService()
        try:
            jsonRequest = request.get_json(force=True)
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.deleteData(id)

            return jsonify(serviceData.getData()), 200
        except:
            return jsonify(serviceData.getData()), 200
