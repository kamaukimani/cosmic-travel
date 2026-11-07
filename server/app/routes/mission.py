from flask import request,make_response 
from flask_restful import Resource 
from app.db import db 
from app.models import Mission 

class Missions(Resource):
    def get(self):
        missions=[mission.to_dict(rules=("-planet","-scientist",)) for mission in Mission.query.all()]

        return make_response(missions,200)

    def post(self):
        data=request.get_json()

        allowed_fields=["name","scientist_id","planet_id"]

        if "name" in data and "scientist_id" in data and "planet_id" in data:
            mission=Mission()

            for attr in data:
                if attr in allowed_fields:
                    setattr(mission,attr,data[attr])
            db.session.add(mission)
            db.session.commit()

            response=mission.to_dict()

            return make_response(
                response,
                201
            )

        return {"errors": ["validation errors"]},422