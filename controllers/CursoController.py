from flask.views import MethodView
from flask import jsonify, request
from services import CursoService
from services.services import fixStringClient

class CursoControllers(MethodView):
    def get(self):
        serviceData = CursoService.CrudCursoService()
        return jsonify(serviceData.getData()), 200

    def post(self):
        serviceData = CursoService.CrudCursoService()
        try:
            jsonRequest = request.get_json(force=True)
            profesor_encargado = fixStringClient(jsonRequest['profesor_encargado'])
            grado = fixStringClient(jsonRequest['grado'])
            inserted = serviceData.addData(profesor_encargado, grado)
            
            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200
        
    def put(self):
        serviceData = CursoService.CrudCursoService()
        try:
            jsonRequest = request.get_json(force=True)
            profesor_encargado = fixStringClient(jsonRequest['profesor_encargado'])
            grado = fixStringClient(jsonRequest['grado'])
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.changeData(profesor_encargado, grado, id)

            return jsonify(serviceData.getData()), 200
        except :
            return jsonify(serviceData.getData()), 200

    def delete(self):
        serviceData = CursoService.CrudCursoService()
        try:
            jsonRequest = request.get_json(force=True)
            id = fixStringClient(jsonRequest['id'])
            inserted = serviceData.deleteData(id)

            return jsonify(serviceData.getData()), 200
        except:
            return jsonify(serviceData.getData()), 200
