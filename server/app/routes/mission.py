from flask import request,make_response 
from flask_restful import Resource 
from app.db import db 
from app.models import Mission 

class Missions(Resource):
    def get(self):
        missions=[mission.to_dict(rules=("-planet","-scientist",)) for mission in Mission.query.all()]

        return make_response(missions,200)

    