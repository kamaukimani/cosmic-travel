from flask_restful import Resource 
from app.models import Scientist 
from flask import request,make_response   

class Scientists(Resource):
    def get(self):
        scientists=[scientist.to_dict(rules=("-missions",)) for scientist in Scientist.query.all()]

        return make_response(scientists,200)