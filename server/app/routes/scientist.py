from flask_restful import Resource 
from app.models import Scientist 
from flask import request,make_response   

class Scientists(Resource):
    def get(self):
        scientists=[scientist.to_dict(rules=("-missions",)) for scientist in Scientist.query.all()]

        return make_response(scientists,200)


class ScientistById(Resource):
    def get(self,id):
        scientist=Scientist.query.filter(Scientist.id == id).first()

        if scientist:
            
            response=scientist.to_dict()

            return make_response(response,200)

        return {"error": "Scientist not found"},404