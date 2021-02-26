from flask.views import MethodView
from flask import jsonify, request
from services import DirectorGInfoService
from services.services import fixStringClient

class DirectorGInfoControllers(MethodView):
    def post(self):
        serviceData = DirectorGInfoService.CrudDirectorGInfoService()
        jsonResponse = request.get_json(force=True)
        id = fixStringClient(jsonResponse['id'])
        inserted = serviceData.getData(id)
        return jsonify(serviceData.getData(id)), 200
