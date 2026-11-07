from flask_restful import Resource 
from app.models import Planet 
from flask import request,make_response 
from app.db import db 

class Planets(Resource):
    def get(self):
        planets=[planet.to_dict(rules=("-missions",)) for planet in Planet.query.all()]

        return make_response(planets,200)

class PlanetById(Resource):
    def get(self,id):
        planet=Planet.query.filter_by(id=id).first()

        if planet is None:

            return {"error":"Planet not found"},404

        response=planet.to_dict()

        return make_response(response,200)