from flask_restful import Resource 
from app.models import Planet 
from flask import request,make_response 
from app.db import db 

class Planets(Resource):
    def get(self):
        planets=[planet.to_dict(rules=("-missions",)) for planet in Planet.query.all()]

        return make_response(planets,200)