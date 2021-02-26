from flask import Flask
from routes.routes import *
from flask_cors import CORS
from config import SECRET_KEY

app = Flask(__name__)

CORS(app, resources={
    r"/*": {"origins": "*"},
    r"/*": {
        "origins": ["*"],
        "methods": ["OPTIONS", "POST"],
        "allow_headers": ["Authorization", "Content-Type"],
        }
    })

app.secret_key = SECRET_KEY

app.add_url_rule(profesor["profesor_route"], view_func=profesor["profesor_controllers"])

app.add_url_rule(estudiante["estudiante_route"], view_func=estudiante["estudiante_controllers"])

app.add_url_rule(curso["curso_route"], view_func=curso["curso_controllers"])

app.add_url_rule(materias["materias_route"], view_func=materias["materias_controllers"])

app.add_url_rule(notas["notas_route"], view_func=notas["notas_controllers"])

app.add_url_rule(profesor["director_g_info_route"], view_func=profesor["director_g_info_controllers"])

app.add_url_rule(notas["notas_estudiantes_route"], view_func=notas["notas_estudiantes_controllers"])