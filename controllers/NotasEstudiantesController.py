from flask.views import MethodView
from flask import jsonify, request
from services import NotasEstudiantesService
from services.services import fixStringClient

class NotasEstudiantesControllers(MethodView):
    def post(self):
        serviceData = NotasEstudiantesService.CrudNotasEstudiantesService()
        jsonResponse = request.get_json(force=True)
        id = fixStringClient(jsonResponse['id'])
        inserted = serviceData.getData(id)
        return jsonify(serviceData.getData(id)), 200
