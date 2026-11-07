from flask import Flask 
from .config import Config
from .db import db,migrate
from .models import *
from flask_restful import Api
from .routes import *


def create_app():

    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    api=Api(app)

    api.add_resource(Scientists,'/scientists',endpoint="scientists")
    api.add_resource(ScientistById,'/scientists/<int:id>',endpoint="scientist_id")
    api.add_resource(Planets,'/planets',endpoint="planets")
    api.add_resource(PlanetById,'/planets/<int:id>',endpoint="planet_id")
    api.add_resource(Missions,'/missions',endpoint="missions")


    return app