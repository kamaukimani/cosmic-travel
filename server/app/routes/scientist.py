from flask_restful import Resource 
from app.models import Scientist 
from flask import request,make_response 
from app.db import db  

class Scientists(Resource):
    def get(self):
        scientists=[scientist.to_dict(rules=("-missions",)) for scientist in Scientist.query.all()]

        return make_response(scientists,200)

    def post(self):

        scientist=Scientist()
        data=request.get_json()

        if "name" in data and "field_of_study" in data:
            allowed_fields=["name","field_of_study"]
            for attr,value in data.items():
                if attr in allowed_fields:
                    setattr(scientist,attr,value)
            db.session.add(scientist)
            db.session.commit()

            response=scientist.to_dict()

            return make_response(response,201)
        return {"errors": ["validation errors"]},422


class ScientistById(Resource):
    def get(self,id):
        scientist=Scientist.query.filter(Scientist.id == id).first()

        if scientist:

            response=scientist.to_dict()

            return make_response(response,200)

        return {"error": "Scientist not found"},404

    def patch(self,id):
        scientist=Scientist.query.filter_by(id=id).first()

        if scientist is None:

            return {"error": "Scientist not found"},404

        data=request.get_json()

        allowed_fields=["name","field_of_study"]

        for attr,value in data.items():
            if attr in allowed_fields:
                setattr(scientist,attr,value)
        db.session.commit()

        response=scientist.to_dict()

        return make_response(response,202)
    def delete(self,id):
        scientist=Scientist.query.filter_by(id=id).first()

        if scientist is None:

            return {"error": "Scientist not found"},404

        db.session.delete(scientist)
        db.session.commit()

        return {},204